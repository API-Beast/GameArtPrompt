import random

from lib.GenerativeFormatter import GenerativeFormatter
from lib.Vocab import merge_vocab
from lib.Vocab import Vocab

d = Vocab()

d["ranged_weapon"] 		= ["bow", "crossbow", "javeline"]
d["thrusting_weapon"] = ["dagger", "sword", "rapier", "spear", "halberd", "claws"]
d["cutting_weapon"] 	= ["sword", "axe", "halberd", "poleaxe", "claws"]
d["crushing_weapon"] 	= ["axe", "mace", "warhammer", "warclub", "poleaxe", "flail", "quarterstaff"]
d["blade_weapon"]			= ["sword", "dagger", "rapier"]
d["weapon"] 			= d.merge_sets("ranged_weapon", "thrusting_weapon", "cutting_weapon", "crushing_weapon")
d["shield"]				= ["shield", "tower shield", "buckler"]

d["armor_type"]		= ["chainmail", "plated mail", "plate", "plated cloth", "lamellar", "laminar", "scale", "brigandine", "leather"]
d["armor_material"] = [	"chainmail", "padded cloth", "steel", "bronze", "plate", "plated", "scale", "leather", "unobtainium", "hide",
												"crystaline", "obsidian", "overgrown", "earthen", ["majestic", "ornamental"], "primitve"]
d["armor_metal"]  = ["[none]", "crystaline", "obsidian", "overgrown", "earthen", "majestic", "steel", "bronze"]
d["chest_piece"]  = ["hauberk", "cuirass", "{armor_metal} plate armor", "brigandine", "{armor_metal} plated mail", "gambeson", "leather jacket", "{armor_metal} laminar chest"]
d["armor"]				= ["{armor_material} boots", "{armor_material} gauntlets", "{armor_material} bracers", "{chest_piece}", "{armor_material} greaves", "{armor_material} helmet"]
d["unspec_armor"] = ["boots", "gauntlets", "bracers", "brigandine", "cuirass", "plate armor", "helmet", "greaves"]
d["clothes"]			= ["pants", "robes", "dress", "jacket", "head-dress", "gloves", ["shoes", "boots"], "cloak"]
d["jewelry"]			= ["ring", "jewel", "amulet", "bracelet", "necklace"]
d["magic_tool"] 	= [["book", "grimoire"], "wand", "staff", ["orb", "gemstone"]]
d["curio"]				= ["eye", "bone", "jaw", "hammer", "anvil", "chains"]
d["elemental"]		= ["fire", "physical", "cold", "poison", "lightning", "elemental", "unholy", "holy"]
d["enchantable"] 	= d.merge_sets("jewelry", "weapon", "armor", "magic_tool", "curio", "clothes")

d["species"] = ["demon", "orc", "god", "undead", "life", "magic"]
d["enchanted_weapon"] = [	"{cutting_weapon} of bursting flames", "Electocuting {cutting_weapon}", "{crushing_weapon} of slaughter",
													"Molten {crushing_weapon}", "Thunderous {crushing_weapon}", "{species}seeker {ranged_weapon}",
													"Vampiric {blade_weapon}", "Venomous {blade_weapon}", "Poison-tipped {ranged_weapon}", "Demonic {weapon}",
													"Cursed {weapon}", "Blessed {weapon}", "Anti-magic {weapon}"]
													
d["enchanted_armor"] 	= [	"{clothes|unspec_armor} of the Bull", "Nightmare {unspec_armor}",
													"Divine {unspec_armor}", "Cursed {unspec_armor}",
													"Magic circuit {unspec_armor}", "Molten core {unspec_armor}",
													"Reflective {shield}", "Spiked {shield}", "Ornamental {shield}"]


d["social_item"]			= d.merge_sets("clothes", "jewelry")
d["enchanted_social"] = ["Alluring {social_item}", "{social_item} of the Scholar", "{social_item} of the Scroundel", "{social_item} of the Beggar", "Noble {social_item}", "Master-craft {social_item}"]

d["enchanted_magic_tool"] = [	"{magic_tool} of the Scorching Flame", "{magic_tool} of Creeping Poison", "{magic_tool} of Chilling Frost",
															"{magic_tool} of Demon Summoning", "{magic_tool} of Eternal Servitude", "{magic_tool} of Divine Light",
															"{magic_tool} of Eternal Life", "{magic_tool} of Undeath", "{magic_tool} of Corrupting Blight",
															"{magic_tool} of the Protective Arts", "{magic_tool} of Thunderous Lightning", "{magic_tool} of Raging Storms",
															"{magic_tool} of Soul Harvest", "{magic_tool} of Cleansing Waters", "Reinforcing {magic_tool}"]

d["substance"] = ["potion", "tinkture", "vial", "powder", "mushroom", "root"]
d["scroll"] = ["scroll"]
d["alchemy_consumable"]  = ["Healing {substance}", "Revitalizing {substance}", "Mana {substance}", "{substance} of Bulls Strength"]
d["alchemy_consumable"] += ["Creeping poison vial", "Lethal poison vial", "Immobilizing poison vial", "Weakening poison vial", "Vial of acid"]

d["utility_item"] 	= ["{jewelry} of Teleportation", "{jewelry|unspec_armor|shield} of {elemental} Resistance"]
d["food"]						= ["Sausage", "Chicken Wing", "Bread", "Milk", "Cheese", "Eggs", "Apricot", "Apple", "Orange", "Chocolate", "Ice Cream", "Pie", "Citrus", "Onion", "Garlic", "Pumpkin", "Tomato", "Lobster", "Cucumber", "Steak", "Kebab", "Potato", "Cake", "Celery"]
d["metal"]					= ["Steel", "Iron", "Copper", "Gold", "Silver", "Bronze", "Mythril"]
d["raw_metal"]			= ["Iron", "Copper", "Gold", "Silver", "Mythril"]
d["stone"]					= ["Sandstone", "Marble", "Limestone", "Granite", "Pbsidian"]
d["crafting_item"] 	= ["{metal} Ingot", "{raw_metal} Ore", "Wooden Log", "Wooden Stick", "Wood Plank", "Slab of {stone}"]

patterns 	= ["{armor}", "{enchanted_armor}", "{enchanted_magic_tool}", "{enchanted_social}", "{enchanted_weapon}"]
patterns += ["{alchemy_consumable}", "{utility_item}", "{food}", "{crafting_item}"]
formatter = GenerativeFormatter(d)

def generate():
	pattern = random.choice(patterns)
	result = formatter.format(pattern)
	return result.title()

def get_context():
	return "#Item"

def count_permutations(*args):
	return formatter.count_permutations(patterns, *args)

if __name__ == "__main__":
	for i in range(0, 20):
		print(generate())