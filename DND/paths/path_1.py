from background.DND_global import df_dict, monster, log, player, fun, dm, f_replace

def main():
    story()

def story():

    # Scene

    fun.display_and_type(f"Having outlived several massacres before you, the gaze of bloodlust is no stranger to the {monster.type}.", log.scene)

    # # Monster

    fun.display_and_type("A creature of habit it appears.", monster.speak)
    fun.display_and_type(f"Pure arrogance, driven by the intent to leave only ruins in your wake.", monster.speak, nextline=False) # Add race stat["race"]
    fun.display_and_type("Very well then...", monster.speak, nextline=False, pause=False)
    fun.wait(0.5)
    fun.typewriter(" Marauder,", delay=0.1, nextline=False)
    fun.wait(1)
    fun.typewriter(" go on.", pause=True)

    # # Scene

    fun.display_and_type(f"The beast plants its feet in preperation to hold its ground or to leap into action.", log.scene)

    if "Success" in dm.difficulty_check("medium", stat="strength"):

        # Scene

        fun.display_and_type(f"You grip your {log.weapon_name}, whitening the knuckles as you hastefully aproach the {monster.type}.", log.scene)
        fun.display_and_type("The beast sweeps its limb in your direction, attempting to diplace your poise.", log.scene)


        if "Success" in dm.difficulty_check("hard", stat="dexterity"):

            fun.display_and_type("With a quick maneuver, you dodge out of the way.", log.scene)
            dm.xp_calc(multiplier=2)
            fun.display_and_type(f"Carrying over your momentum into a purposeful thrust, your {log.weapon_name} penetrates the thick skin of the {monster.type}.", log.scene)
            monster.hp += dm.dmg_dealt( player.weapon)

            # Scene

            fun.display_and_type(f"As blood pours from the wound, the {monster.type} lets out a deafing screech.", log.scene, nextline=True)

        else: 

            player.condition.append("Prone")
            player.hp += dm.dmg_dealt(set_range=4)

            # Scene 

            fun.display_and_type(f"Abruptly you're thrown to the ground, your {log.weapon_name} veers out of reach.", log.scene)
            dm.xp_calc(multiplier=2)
            
            # Monster

            fun.display_and_type("I assumed better of you Marauder. Shouldn't keep your ancestors fun.waiting.", monster.speak)

            # Scene

            fun.display_and_type("The beast's figure perks up, preping for an attack.", log.scene) 

            monster_attack()

    else: 

        monster_attack()


def monster_attack():
        
        fun.clear()

        # Scene

        fun.display_and_type(f"Flaring its nostrils and glaring its razer like teeth, the {monster.type}'s muscles tense.", log.scene)
        fun.display_and_type("Abruptly, the beast hurles itself in your direction", log.scene)

        choices_2 = ["Dodge out of the way", "Stand fast", "Charge the beast", "Defend with an item"]

        response_2 = dm.multiple_choice(choices_2)

if __name__ == "__main__":
    main()