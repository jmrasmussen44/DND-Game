import random
import functools
from background.journal import monster_class, journal
from background.character_class import character
import background.functions_i_like as fun
import background.DND_database
from background.font_func import font_replacer
import sys
import re

df_dict = background.DND_database.df_dict
log = journal()
monster = monster_class()
player = character()
f_replace = font_replacer


def dAny(num_of_dice=1, dice_range_start=1, dice_range_end=20, adv_disadv=None):
    total_list = []
    total = 0
    if adv_disadv is not None:
        num_of_dice=2
    for _ in range(int(num_of_dice)):
        if adv_disadv == "adv": 
           total_list.append(random.randint(dice_range_start, dice_range_end))
           total = max(total_list)
        elif adv_disadv == "disadv":
            total_list.append(random.randint(dice_range_start, dice_range_end))
            total = min(total_list)
        else:
            total += random.randint(dice_range_start, dice_range_end)
    return total

def dmg_dealt(attack, set_range=None):
    if set_range is None:
        if len(attack.index) == 7:

            dmg_dice = attack[3]

        else:

            dmg_dice = attack[10]
        add_val = None

        try: num_dice, dice_range, add_val = re.split('\D', dmg_dice)

        except ValueError:

            num_dice, dice_range = re.split('\D', dmg_dice)

        else: 

            num_dice, dice_range, add_val = re.split('\D', dmg_dice)
    else:
        num_dice = 1
        dice_range = set_range

    dmg = dAny(num_of_dice=int(num_dice), dice_range_end=int(dice_range))

    if add_val is not None:
        dmg = (dmg + int(add_val)) * -1

    else: 
        dmg = dmg * -1

    return dmg

def death_check():
    if player.hp <= 0:
        print(f_replace("You Died", font=1))
        fun.wait(2)
        fun.clear()
        print(f_replace("Game Over", font=1))
        fun.wait(3)
        fun.clear()
        sys.exit()

def difficulty_check(difficulty, stat, vantage=None):
    print(f_replace("Difficulty  Check", font=1))
    print(f_replace(difficulty, font=1))
    fun.wait(3)
    fun.clear()

    stat = player.skills[stat]
    check = None
    nat20 = 20
    critfail = 1
    roll_difficulty = {"ez": 0, "easy": 5, "medium": 10, "hard": 15, "very hard": 20, "extreme": 25, "impossible": 30}
    roll = dAny(adv_disadv=vantage)
    modifier = int((stat - 10) / 2) if stat % 2 == 0 else int((stat - 11) /2)
    modifier = 0 if modifier < 0 else modifier
    modified_roll = roll + modifier

    if modified_roll >= roll_difficulty[difficulty] or roll == nat20:
        check = {"Success": modified_roll} if roll != nat20 else {"Success": roll}
        for key, value in check.items():
            print(f_replace(key + " : " + str(value), font=1))
        fun.wait(3)
        xp_bonus = roll_difficulty[difficulty] / 5
        xp_calc(multiplier=xp_bonus)

    elif roll == critfail:
        check = {"Critical Failure": roll}
        for key, value in check.items():
            print(f_replace(key + " : " + str(value), font=1))
        fun.wait(3)
        xp_calc()

    else: 
        check = {"Failure": modified_roll}
        for key, value in check.items():
            print(f_replace(key + " : " + str(value), font=1))
        fun.wait(3)
        xp_calc()
    
    fun.clear()
    return check

def gp(max_gp, min_gp=1, multiplier=1, gp_loss=False):
    result = dAny(num_of_dice=multiplier, dice_range_end=max_gp, dice_range_start=min_gp)
    if gp_loss == True:
        result = result * -1
    player.gp += result
    return result

def rand_query(dictionary, type=None, size=None, alignment=None, hp=None, location=None, name_filter = None, cost=None, dmg=None, base_ac=None, weight=None, item_properties=None, category=None, damage_dice=None):
    df = df_dict[dictionary]
    conditions = []
    
    if type is not None:
        conditions.append(df.type == type.capitalize())
    if size is not None:
        conditions.append(df.size == size.capitalize())
    if alignment is not None:
        conditions.append(df.alignment == alignment.capitalize())
    if hp is not None:
        conditions.append(df.hit_points == hp)
    if category is not None:
        conditions.append(df.category == category.capitalize())
    if cost is not None:
        conditions.append(df.cost == cost)
    if dmg is not None:
        conditions.append(df.damage_dice == dmg)
    if base_ac is not None:
        conditions.append(df.base_ac == base_ac)
    if weight is not None:
        conditions.append(df.weight == weight)
    if item_properties is not None:
        item_properties = item_properties.capitalize()
        conditions.append(df["properties"].apply(lambda properties: item_properties in properties))
    if location is not None:
        location = location.capitalize()
        conditions.append(df["environments"].apply(lambda enviroment: location in enviroment))
    if name_filter is not None:
        name_filter = name_filter.capitalize()
        conditions.append(df['name'].apply(lambda name: name_filter in name.split()))
    if conditions:
        combined_condition = functools.reduce(lambda x, y: x & y, conditions)
        df_query = df[combined_condition]
    else:
        df_query = df

    m_index = dAny(dice_range_end=(len(df_query.name)))
    random_result = df_query.iloc[int(m_index) -1]
     
    return random_result    # Monster name located at [1] since is a Series

def calculate_alignment(karma_multiplier):   # Calculate Karma based on decisions made
    base_value = 10
    adjusted_value = base_value * karma_multiplier
    moral_values = player.moral_values
    
    if moral_values != -1000 and moral_values != 1000:
        moral_values += adjusted_value
    
    if moral_values >= 500:
        new_moral = "Lawful Good"
    elif 150 <= moral_values <= 499:
        new_moral = "Lawful Neutral"
    elif -149 <= moral_values <= 149:
        new_moral = "Neutral"
    elif -499 <= moral_values <= -150:
        new_moral = "Chaotic Neutral"
    else:
        new_moral = "Chaotic Evil"

    player.alignment = new_moral
    
    # Use this display alignment change to user

    # if new_moral != player_alignment:
    #     blink(f"Your alignment is now: {new_moral}")
    #     clear(2)
    
    return new_moral, moral_values

def multiple_choice(choice_list, question_prompt="What do you do?: ", karma=None):
    print()
    num_of_choices = len(choice_list)
    for index, option in enumerate(choice_list):
        print(str(index + 1) + ") " + option)

    print()
    response = fun.num_response(num_of_choices, question_prompt)
    response = int(response) - 1
    fun.clear()

    if karma:
        multiplier = karma[response]
        new_moral, moral_values = calculate_alignment(multiplier)
        player.alignment = new_moral
        player.moral_values = moral_values

    return response

def xp_calc(multiplier=1): # Depending on d20 rolls, story choices, and successful encounters, player will be rewarded xp until xp bar reaches threshold, at which point player will have 2 skill point to spend on their player.
    xp = player.xp
    level = player.level
    xp += 10 * multiplier
    xp_threshold = 1000

    def leveling():
        skills = player.skills
        skill_keys = list(skills.keys())
        skill_values = list(skills.values())
        points_remaining = 2
        zip_list = [f"{item[0]} {item[1]}" for item in list(zip(skill_keys, skill_values))]
        print("* 2 Skills Points ")
        skill_index = multiple_choice(zip_list, question_prompt="Which skill to upgrade?: ")
        skill_choice = skill_keys[skill_index]
        points_remaining += -1
        skills[skill_choice] += points_remaining
        if fun.yes_or_no("Use both points for this skill?: "):
            skills[skill_choice] += points_remaining
        else:
            skills = player.skills
            skill_keys = list(skills.keys())
            skill_values = list(skills.values())
            zip_list_adj = [f"{item[0]} {item[1]}" for item in list(zip(skill_keys, skill_values))]
            skill_index = skill_index = multiple_choice(zip_list_adj, question_prompt="Which skill to upgrade?: ")
            skill_choice = skill_keys[skill_index]
            skills[skill_choice] += points_remaining

    if xp > xp_threshold:
        fun.clear()
        level += 1
        print(f_replace("Level  Up!", font=1))
        leveling()


def inventory(added_item=None): # When items are picked up or used, item should be printed as removed or added, then adjust players inventory dictionary accordingly
    item_choice = None
    inv = player.inventory["inventory_list"]
    
    if added_item is not None:
        
        inv.remove("None")
        inv.append(added_item)
        inv.append("None")
        fun.plural_check(added_item, "added.")
        fun.wait(3)
        fun.clear()

    else:
        
        item_index = multiple_choice(inv, question_prompt="Which item would you like to use?: ")
        item_choice = inv[item_index]

        if item_choice == "None":

            print("No items have been selected.")
            item_choice = None
            fun.wait(1.5)

        else:

            fun.plural_check(item_choice, "removed.")
            inv.remove(item_choice)
            fun.wait(3)
            fun.clear()
        return item_choice
    # Allow player to interact with items in their inventory and change the story based on items used.