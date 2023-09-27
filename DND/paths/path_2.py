from background.DND_global import df_dict, monster, log, player, fun, dm, f_replace
from paths.path_1 import monster_attack
import paths.path_2_ext

def main():
    story()

def story():
    log.town_merchant = dm.rand_query("races")
    town_merchant = log.town_merchant
    
    # Scene

    fun.display_and_type(f"Paying no mind to the {monster.type}, you dismissively redirect your attention to the shimmering coin all around you.", log.scene)
    fun.display_and_type(f"This will spend mighty well with the local {town_merchant[0]} shopkeep, you think to yourself.", log.scene)
    fun.display_and_type(f"Stuffing the first handful of gold into your knapsack, a total of {dm.gp(10, min_gp=3)} GP accrued.", log.scene)
    
    if "Success" in dm.difficulty_check("hard", "dexterity"):

        fun.display_and_type(f"The {monster.type}, none the wiser, overlooks your stealthy advance.", log.scene)
        fun.display_and_type("To what do I owe the pleasure, Marauder?", monster.speak, comma_wait=0.7)

        choice_2()
    
    else:

        stealth_fail()


def stealth_fail():
    # Monster

    fun.display_and_type("Befoul MY FORTUNE with your begrimed hands!?", monster.speak)

    # Scene

    fun.display_and_type(f"The {monster.type}, in a state of disbelief, vigorously slams its tail against the cavern walls.", log.scene, nextline=True, pause=False)
    fun.wait(1.5)
    fun.typewriter("Debris crumbles from the subterranean celling, littering large stones amoungst the many treasures.", scene=True, pause=True)

    # Monster

    fun.display_and_type("Gluttony will be your FINAL mistake, Marauder!", monster.speak, comma_wait=0.1)

    monster_attack()

def choice_2(path_3=None):
    choice_2 = ["Riches", "Companionship", "Guidance", f"* Draw your {log.weapon_name.capitalize()} *"]
    karma_2 = [-2, 2, 3, -5]

    response_2 = dm.multiple_choice(choice_2, karma=karma_2, question_prompt="What do you desire?: ")

    paths.path_2_ext.story(response_2, path_3=path_3)

if __name__ == "__main__":
    main()
