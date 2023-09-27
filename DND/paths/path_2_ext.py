import paths.path_1
import paths.path_2
import paths.path_3
import paths.path_4

from background.DND_global import df_dict, monster, log, player, fun, dm, f_replace

def main():
    story()
#["Riches", "Companionship", "Guidance", f"Draw your {log.weapon_name}"]
def story(player_response, path_3=None):
    if player_response == 0:

        paths.path_2.stealth_fail()

    if player_response == 1:

        if path_3:
            
            paths.path_4.story(prompt=False) 

        else:

            paths.path_3.story(no_repeat=True)

    if player_response == 2:

        # Add dialouge later
        paths.path_5.story()

    if player_response == 3:
        paths.path_1.story()

if __name__ == "__main__":
    main()