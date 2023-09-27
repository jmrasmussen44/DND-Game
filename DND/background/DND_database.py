import requests
import pandas as pd
import sys
import os
import background.functions_i_like as fun
# from database_save.save_location import database_save

API_BASE_URL = "https://api.open5e.com/v1/"
RESOURCE_TYPES = {
    "conditions": "conditions",
    "monsters": "monsters",
    "races": "races",
    "classes": "classes",
    "weapons": "weapons",
    "armor": "armor"}

# Retrieve data from API
def fetch_data():
    data_resources = {}
    for header, url_suffix in RESOURCE_TYPES.items():
        api_search = API_BASE_URL + url_suffix
        try:
            response = requests.get(api_search)
            response.raise_for_status()  # Raise HTTPError for bad status codes
            data = response.json()
            data_resources[header] = data['results']
        except requests.exceptions.RequestException as e:
            sys.exit(f"Error accessing {header}. Error: {e}")
    return data_resources

# Database Creation
def build_dataframes(dictionaries):
    df_dict = {}
    for key, r_list in dictionaries.items():
        r_df = pd.DataFrame(r_list)
        columns_to_drop = [col for col in r_df.columns if "slug" in col or "document" in col]
        r_df.drop(columns=columns_to_drop, inplace=True)
        df_dict[key] = r_df
    return df_dict

database_save = r"" + os.path.dirname(os.path.abspath(__file__)).replace("background", "database_save")

# Create CSV files
def create_csv_files(dataframe_dict):
    for key, df in dataframe_dict.items():
        file_name = os.path.join(database_save, f"{key}.csv")
        df.to_csv(file_name, index=False)


# Load CSV files into a dictionary
def csv_dictionary():
    df_dict = {}
    for key in RESOURCE_TYPES:
        file_name = os.path.join(database_save, f"{key}.csv")
        df = pd.read_csv(file_name)
        df_dict[key] = df
    return df_dict

# Compiler function
def compiler():
    fun.clear()
    if all(os.path.exists(os.path.join(database_save, f"{key}.csv")) for key in RESOURCE_TYPES):
        print("\nDatabase Integrity Validated.\n")
        fun.wait(0.5)
        return csv_dictionary()
    else:
        print("\nEnsure Internet Conneciton to Fetch Database.\n")
        print("Fetching Missing Database Files...")
        fun.wait(0.5)

        try:

            data_resources = fetch_data()
            dataframe_dict = build_dataframes(data_resources)
            create_csv_files(dataframe_dict)
            fun.clear()
            print("\nDatabase Integrity Validated.\n")
            return csv_dictionary()
        
        except:
            fun.clear()
            sys.exit("Error Validating Database.")
        
        

df_dict = compiler()
fun.clear(wait=1)
