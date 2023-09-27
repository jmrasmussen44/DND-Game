from background.DND_global import df_dict, monster, log, player, fun, dm, f_replace
import paths.path_4_ext

def main():
    story()

def story(prompt=True):   
    prompt2_3 = "You wish to do me no harm?"
    
    # Scene

    fun.display_and_type(f"With a careful and purposeful motion, you disarm.", log.scene)
    fun.display_and_type(f"Laying down your {log.weapon_name.lower()} as an attempt to dispel doubt and foster faith.", log.scene)
    
    # Monster

    if prompt:
        fun.display_and_type(prompt2_3, monster.speak)
    stat_index = dm.dAny(dice_range_end=2)
    rand_stat_list = ["wisdom", "charisma"]
    
    if "Success" in dm.difficulty_check("easy", stat=rand_stat_list[stat_index -1]):

        # Scene

        fun.display_and_type(f"As you cautiously make your way over to the {monster.type}, a bloodied gash traveling across the beast's jugular comes into view.", log.scene)
        fun.display_and_type(f"The severity of the situation inspires a rush of heroism, perhaps you could spare an item with curative properties.", log.scene)
        
        if fun.yes_or_no("Open Inventory?"):
            fun.clear()
            fun.display_and_type(f"You hastefully rummage through your knapsack in search of anything to remedy the {monster.type}'s agony.", log.scene)

            item_choice = dm.inventory()

            if item_choice == None:
                paths.path_4_ext.friendly_fail()

            fun.display_and_type(f"You take out {fun.determine_article(item_choice).lower()} in hopes of aiding the {monster.type}.", log.scene)

            paths.path_4_ext.story(item_choice)

        else: 
    
             paths.path_4_ext.friendly_fail()

    else:

        paths.path_4_ext.friendly_fail()


            
if __name__ == "__main__":
    main()