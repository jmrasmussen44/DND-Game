from background.DND_global import df_dict, monster, log, player, fun, dm, f_replace
from narration import narration
import background.character_class as cc

log.scene = f_replace("scene", font=2)
           
def main():
    cc.main()
    narration()
    response_1 = storyline()
    response_2 = first_sequence(response_1)
    second_sequence(response_2)

def storyline():
    log.weapon_name =  player.weapon[0].lower()


    fun.display_and_type("Have you come for me, Marauder?", monster.speak, nextline=True, comma_wait=0.3, pause=False)
    fun.wait(0.7)
    fun.typewriter("Surely you'd grant me your name before taking my life.")
    player.name = fun.error_check("What is your name?: ")
    fun.clear()
    fun.display_and_type(f"Ah, {player.name}...", monster.speak, comma_wait=0.3, period_wait=0.06, nextline=False, pause=False)
    fun.wait(0.7)
    fun.typewriter(" the Forsaken.")
    fun.display_and_type("You'd best make it quick then.", monster.speak, nextline=False, period_wait=0.5, pause=False)
    fun.typewriter(" Plenty of bloodshed to be had for you,", nextline=False, pause=False)
    fun.typewriter(" Marauder.", delay=0.1)
 

    # First Sequence

    choices_1 = ["Attack the Beast", "Retreive its Belongings", "Spare its Life", "Befriend the Monstrosity"]
    karma_1 = [-5, -2, 1, 3]
    response_1 = dm.multiple_choice(choices_1, karma=karma_1)

    return response_1


def first_sequence(response_1):

    if response_1 == 0:
        import paths.path_1   
        response_2 = paths.path_1.story()

    elif response_1 == 1:
        import paths.path_2
        response_2 = paths.path_2.story()

    elif response_1 == 2:
        import paths.path_3
        response_2 = paths.path_3.story()
    
    else:
        import paths.path_4
        response_2 = paths.path_4.story()
        
    return response_2

def second_sequence(second_response):
    ...
    
if __name__ == "__main__":
    main()