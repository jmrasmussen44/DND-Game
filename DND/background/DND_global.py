import background.DND_database
import background.DND_mechanics
from background.journal import monster_class, journal
from background.character_class import character
from background.font_func import font_replacer

df_dict = background.DND_database.df_dict
log = journal()
monster = monster_class()
player = character()
fun = background.functions_i_like
dm = background.DND_mechanics
f_replace = font_replacer
log.scene = f_replace("scene", font=2)
monster.starter_dragon = dm.rand_query("monsters", type="dragon", name_filter='ancient', location='mountains')
monster.type = monster.starter_dragon[3].lower()
monster.speak = f_replace(monster.type)
monster.hp = monster.starter_dragon[9]
log.na_items = []

