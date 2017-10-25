import random

from lib.GenerativeFormatter import GenerativeFormatter
from lib.Vocab import merge_vocab
from lib.Vocab import Vocab

import words.Fantasy
import words.General

d = Vocab()
d = merge_vocab(d, words.Fantasy.get_all())
d = merge_vocab(d, words.General.get_all())
d["ranged_weapon"] 		= ["bow", "crossbow", "javeline"]
d["thrusting_weapon"] 	= ["dagger", "sword", "rapier", "spear", "halberd", "claws"]
d["cutting_weapon"] 	= ["sword", "axe", "halberd", "poleaxe", "claws"]
d["crushing_weapon"] 	= ["axe", "mace", "warhammer", "warclub", "poleaxe", "flail", "quarterstaff"]
d["blade_weapon"]			= ["sword", "dagger", "rapier"]
d["weapon"] 			= d.merge_sets("ranged_weapon", "thrusting_weapon", "cutting_weapon", "crushing_weapon")
d["shield"]				= ["shield", "tower shield", "buckler"]
d["armor"]				= ["boots", "gauntlets", "bracers", "chest armor", "greaves", "helmet"]
d["clothes"]			= ["robes", "gloves", "shoes", "cloak"]
d["jewelry"]			= ["ring", "jewel", "amulet", "bracelet", "necklace"]
d["misc_magic"] 	= ["book", "scroll", "wand", "staff", "potion", "orb"]
d["curio"]				= ["eye", "bone", "jaw", "hammer", "anvil", "chains"]
d["enchantable"] 	= d.merge_sets("jewelry", "weapon", "armor", "misc_magic", "curio", "clothes")

d["species"] = ["demon", "orc", "divine", "undead", "life", "magic"]
d["enchanted_weapon"] = [	"Penetrating {thrusting_weapon}", "Flaming {cutting_weapon}", "Electocuting {cutting_weapon}",
													"Molten {crushing_weapon}", "Thunderous {crushing_weapon}", "{species.capitalize()} seeker {ranged_weapon}",
													"Vampiric {blade_weapon}", "Venomous {blade_weapon}", "Poison-tipped {ranged_weapon}", "{crushing_weapon.capitalize()} of slaughter"]

d["social_item"]			= d.merge_sets("clothes", "armor", "jewelry")
d["enchanted_social"] = ["Charming {social_item}", "{social_item.capitalize()} of desire", "{social_item.capitalize()} of wealth", "{social_item.capitalize()} of negotiation", "{social_item.capitalize()} of precision", "{social_item.capitalize()} of mastery"]

d["enchanted_armor"] = ["Warding {armor}", "Negating {armor}", "Divine {armor}", "Demonic {armor}", "Chaos {armor}", "Living {armor}", "Obsidian {armor}", "Steadfast {armor}"]
d["legendary_items"] = ["{misc_magic|curio|jewelry.capitalize()} of power", "{mystic_god.capitalize()} {misc_magic|curio}", "Holy {misc_magic|curio} of the {good_god}", "Unholy {misc_magic|curio} of the {evil_god}"]

d["curse"]				= ["weakness", "dread", "hunger", "pain", "sin", "blindness", "greed"]
d["cursed_item"] 	= ["{weapon.capitalize()} of imprecision", "Corrupting {enchantable}", "{enchantable.capitalize()} of {curse}"]

patterns = ["{enchantable.capitalize()} of {symbolism_of}", "{cursed_item}", "{enchanted_social}", "{legendary_items}", "{enchanted_weapon}", "{enchanted_armor}"]



def generate():
	formatter = GenerativeFormatter(d)
	pattern = random.choice(patterns)
	result = formatter.format(pattern)
	return result

def get_context():
	return "#Item"

if __name__ == "__main__":
	for i in range(0, 20):
		print(generate())