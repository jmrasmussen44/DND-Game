import re
import time
import sys
from background.font_func import font_replacer as f_replace

def error_check(define_question=""):
    
    num_of_char = 2
    faulty1 = "\nInvalid Character(s)\n"
    faulty2 = "\n" + str(num_of_char) + " Characters Minimum\n"
    
    while True:
        input_to_check = input(define_question)

        if input_to_check.lower == "exit":
            return
        
        if not re.match(r"\S", input_to_check) or re.match(r"\W", input_to_check):
            print(faulty1)
            
        elif len(input_to_check) < num_of_char:
            print(faulty2)

        else:
            string_adj = [string.capitalize() for string in input_to_check.split()]
            return " ".join(string_adj)

test = "Enter your text: "  # Define the test prompt


def clear(wait=0.5):
    time.sleep(wait)
    print("\033[H\033[J")


def blink(text, blink_duration=0.5, total_blink_time=1):
    start_time = time.time()
    
    while time.time() - start_time < total_blink_time:
        sys.stdout.write("\r" + " " * len(text))  # Clear line
        sys.stdout.flush()
        time.sleep(blink_duration)
        
        sys.stdout.write("\r" + text)  # Display text
        sys.stdout.flush()
        time.sleep(blink_duration)
        
        sys.stdout.write("\r" + " " * len(text))  # Clear line
        sys.stdout.flush()
        time.sleep(blink_duration)
        
        sys.stdout.write("\r" + text)  # Display text
        sys.stdout.flush()
        time.sleep(blink_duration)

def num_response(num_of_choices, range_of_num=""): # pulls length of list on num of choices
    num_of_char = 1
    faulty1 = "\nInvalid Character(s)\n"
    faulty2 = "\n" + str(num_of_char) + " Character Minimum\n"
    faulty3 = "\nMaximum of " + str(num_of_char) + " Characters Exceeded\n"
    faulty4 = "\nInput Exceeds Available Choices\n"
    
    while True:
        input_to_check = input(range_of_num)
        
        if not re.match(r"\d", input_to_check) or re.match(r"\W", input_to_check):
            print(faulty1)
            
        elif len(input_to_check) < num_of_char:
            print(faulty2)
            
        elif len(input_to_check) > num_of_char:
            print(faulty3)
            
        elif int(input_to_check) > num_of_choices:
            print(faulty4)
            
        else:
            return input_to_check
        
def wait(duration):
    time.sleep(duration)

def display_and_type(message, string, nextline=False, pause=True, comma_wait=0.3, period_wait=0.01, end="*"):
    print(string)
    print("\n")
    if string == f_replace("scene", font=2):
        message = "* " + message + " *"
        
    typewriter(message, nextline=nextline, pause=pause, comma_wait=comma_wait, period_wait=period_wait)

def typewriter(text, delay=0.08, comma_wait=0.3, period_wait=0.01, nextline=False, scene=False, pause=True, end="*"):
    if scene == True:
         text = "* " + text + f" {end}"
    for char in text:
        if char == ",":
            print(char, end='', flush=True)
            time.sleep(comma_wait)
        elif char == ".":
            print(char, end='', flush=True)
            time.sleep(period_wait)
        else:
            print(char, end='', flush=True)
        time.sleep(delay) # Pause for a short delay
    if nextline:
        print()
        print()
        print()      # Print the character without newline
    if pause:
        print()
        print()
        pause = input("\nPress Enter to continue.")
        clear()

def yes_or_no(question):
    while True:
        answer = input(question + " (y/n): ").lower()
        if answer == "y":
            return True
        elif answer == "n":
            return False
        

def determine_article(word):
    vowels = "aeiouAEIOU"
    if word[0] in vowels:
        return "An " + word
    else:
        return "A " + word



def plural_check(item, remove_or_added):
        if remove_or_added == "added.":
                statement = "been added to your Inventory."
        else: 
                statement = "been removed from your Inventory."
        
        for letter in item:    
                pass

        if letter[-1] != 's':
                print(f"* {determine_article(item)} has {statement} *")

        else:
                print(f"* {item} have {statement} *")







if __name__ == "__main__":
    result = error_check(test)
    blink("test")
    print(result)
    typewriter("Hello, i am testing this prompt.")
    plural_check("apple", "removed")