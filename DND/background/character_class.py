from background.DND_database import df_dict

class character:          # Character stats are built after calling main()
    ...
   
def main():
    character_creation()


def character_creation():
    character.name = None
    character.hp = 8
    character.condition = []
    character.level = 0
    character.xp = 0
    character.alignment = "Neutral"
    character.moral_values = 0
    character.gp = 0
    character.weapon = df_dict["weapons"].iloc[1]
    character.armor = df_dict["armor"].iloc[0]
    character.inventory = {"inventory_list": ["bandage", "food ration", "canteen", "tinder box", "None"]}
    character.skills = {"strength": 10, "dexterity": 10, "intelligence": 10, "wisdom": 10, "charisma": 10}



if __name__ == "__main__":
    main()