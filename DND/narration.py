from background.DND_global import df_dict, monster, log, player, fun, dm, f_replace

def main():
    narration()


def narration():

    fun.display_and_type("A wave of relief envelops you as you reach the summit of the mountain.", log.scene)
    fun.display_and_type("As you wipe away the sweat accumulated from your laborious trek, your gaze locks onto the cave's entrance.", log.scene)
    fun.display_and_type("Cautiously, you peer in.", log.scene)
    fun.display_and_type("The cold rocky chamber is adorned with mounds of gold, armor, and weaponry that line both its floors and walls.", log.scene)
    fun.display_and_type("Your first step into the spacious cavern sends a barreling echo throughout the cave.", log.scene)
    fun.display_and_type(f"Before you lays an {monster.starter_dragon[1]}, only thousands of millennia could leave behind such an archaic creature.", log.scene)

if __name__ == "__main__":
    main()