from background.DND_global import df_dict, monster, log, player, fun, dm, f_replace
import paths.path_2, paths.path_4

def main():
    story()

def story(no_repeat=None):

    prompt2_3 = "you wish to do me no harm?"

    # Scene

    fun.display_and_type(f"A look of confusion dances across the {monster.type}'s face.", log.scene)
    fun.display_and_type(f"Your clemency appears rather peculiar to the {monster.type}, as if mercy were scarcer than bloodshed.", log.scene, comma_wait=0.3)

    # Monster

    fun.display_and_type(f" You...", monster.speak, pause=False)
    fun.wait(0.5)
    fun.typewriter(prompt2_3, pause=True)

    if no_repeat: 

        paths.path_4.story(prompt=False)

    else:

        fun.display_and_type("If that's so, what is it that you seek,", monster.speak, pause=False)
        fun.typewriter(" Marauder?", delay=0.1, pause=True)

        paths.path_2.choice_2(path_3=True)

    # response_2 = dm.multiple_choice()

if __name__ == "__main__":
    main()