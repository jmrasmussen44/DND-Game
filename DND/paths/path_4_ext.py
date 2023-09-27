# Helping dragon path
from background.DND_global import df_dict, monster, log, player, fun, dm, f_replace
import paths.path_1

def main():
    story()

def story(item, no_repeat=None):
    player.name = "beans"

    if item == None:

        friendly_fail()

    elif item == "food ration" or item == "canteen":
        dm.xp_calc()

        if no_repeat:

            fun.display_and_type(f"A measly {item} would offer very little to the dying {monster.type}", log.scene)

        else:
    
        # Scene
        
            term = "quenched" if item == "canteen" else "fed"

            fun.display_and_type("The manageled beast expells a weak snort, as to mock your offering.", log.scene)

            # Monster

            fun.display_and_type(f"The mouths of the living are much better off staying {term} than the latter.", monster.speak)

        dm.inventory(added_item=item)

        log.na_items.append(item)

        item_retry(no_repeat=True)

        # fun.display_and_type("")

    elif item == "tinder box":
            
        # Scene

        fun.display_and_type("Perhaps you could manipulate the fire to seal the wound.", log.scene)

        if "Success" in dm.difficulty_check("very hard", stat="intelligence"):

            ...

        else:
            
            fun.display_and_type("While trying to conjure a Cauterization spell, the tinderbox disintegrates into ashes.", log.scene, pause=False, nextline=True)
            fun.wait(0.7)
            fun.typewriter("The spell has failed", scene=True)

            item_retry()

    else:
        # Scene
        
        fun.display_and_type("Ripping up the dressing into multiple strands, you begin applying them along the length of the laceration", log.scene, nextline=True, pause=False)
        fun.wait(0.7)
        fun.typewriter("This should allow you to temporary mend the wound.", scene=True)

        if "Success" in dm.difficulty_check("medium", stat="wisdom"):
            ...

    # Monster

        fun.display_and_type(f"My time is quickly passing, {player.name[0]}...{player.name}", monster.speak, nextline=True, pause=False)
        fun.wait(0.5)
        fun.typewriter("Will you help me, friend?", pause=False)
        fun.yes_or_no("")

def item_retry(no_repeat=None):

    if fun.yes_or_no("Would you like to use another item?"):
        while True:

            item_choice = dm.inventory()

            if item_choice in log.na_items:

                fun.display_and_type("I can't use that here.", log.scene)
                dm.inventory(added_item=item_choice)
                fun.wait(0.5)
                fun.clear()

            else:

                story(item_choice, no_repeat=no_repeat)
                fun.wait(0.5)
                fun.clear()


def friendly_fail():
        dm.xp_calc()
        fun.clear()
        fun.display_and_type("Insincerity shows through your opaque faith.", monster.speak, nextline=True, pause=False)
        fun.wait(1)
        fun.typewriter("Do you believe you have me fooled, Marauder?")
        paths.path_1.monster_attack()
    

if __name__ == "__main__":
    main()


