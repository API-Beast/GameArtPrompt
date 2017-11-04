import random

from lib.Vocab import Vocab
from lib.Vocab import merge_vocab
from lib.GenerativeFormatter import GenerativeFormatter
import random

d = Vocab()

d["religious_order"] = ["the Purifying Sun", "the Iron Legion", "the Draconic Order", "the Weeping Mistress", "the Eternal Light", "the Crusaders"]
d["religious"] = ["cleric", "paladin", "monk"]
d["historic_inspiration"] = ["East-Asian", "Central-Asian", "Middle-Eastern", "Egyptian", "Germanic", "Nomadic", "Nordic", "Greek", "Roman", "Sumerian", "Tribal", "Mesoamerican"]
d["arctype"] = ["Warrior", "Diplomat", "Soldier", "General", "Merchant"]

d["level"] = [["Elite", "Armored"], "[none]"]

d["mount"] = ["Horse", "Lizard", "Raptor", "Griphon", "Dragon"]

d["horde_tribe"] = ["Iceblood", "Infernal", "Firebringer", "Steelclad", "Deathraiser", "Warborn", "Shadowstalker"]
d["demonic_assoc"] = ["Sin", "Greed", "Lust", "Horror", "Hysteria", "the Blasphemous", "Discord", "Mischief", "Sloth", "Envy", "Pride", "Gluttony", "Domination", "War", "Treason", "Terror", "Wrath", "Temptation", "Nightmare"]

d["profession"] = {}
d["profession"]["civilian"]  = ["Lumberjack", "Farmer", "Alchemist", "Smith", "Engineer"]
d["profession"]["ranged"]    = ["Ranger", "Marksman", "Bowman", "Javelin Thrower"]
d["profession"]["melee"]     = ["Berserker", "Militia", "City Guard", "Hoplite", "Spearman", "Paladin", "Swordsman", "Pikeman", "Knight", "Juggernaut"]
d["profession"]["sneaky"]    = ["Rogue", "Assassin", "Ranger", "Scout", "Hunter"]
d["profession"]["noble"]     = [["King", "Queen"], ["Prince", "Princess"], "Noble"]
d["profession"]["command"]   = ["Commander", "General"]
d["profession"]["twisted"]   = ["Warlord", "Infiltrator", "Assassin", "Torturer", "Executioner", "Mistress", "Raider", "Slaver", "Warlock", "Necromancer", "Cultist"]
d["profession"]["primitive"] = ["Berserker", "Shaman", "Druid", "Beastmaster", "Chieftain", "Summoner"]
d["profession"]["arcane"]    = ["Arcanist", "Enchanter", "Illusionist", "Elementalist", "Runesmith", "Summoner", "Conjurer"]
d["profession"]["rightous"]  = ["Cleric", "Priest", "Paladin", "Knight", "Preacher"]

d["species"] = {}
d["species"]["special"] 	= ["Avian", "Celestial", "Sylvan", "Lizard", "Merman", "Demonic", "Demon", "Succubus", "Naga"]
d["species"]["twisted"]		= ["Demonic", "Demon", "Lizard", "Demonic", "Succubus", "Orc", "Beastman", "Dark Elf", "Human"]
d["species"]["muscular"] 	= ["Orc", "Beastman", "Half-Orc", "Human", "Dwarf", "Demon", "Demonic", "Lizard", "Naga"]
d["species"]["dextrous"]  = ["Elf", "Human", "Dark Elf", "Wood Elf", "Lizard", "Halfling", "Demonic", "Succubus"]
d["species"]["noble"]     = ["Avian", "Celestial", "Lizard", "Naga", "Elf", "Dark Elf", "Human", "Dwarf"]
d["species"]["smart"]     = ["Dwarf", "Human", "Celestial", "Lizard", "Demon", "Succubus", "Elf", "Dark Elf", "Gnome", "Halfling"]
#d["species"]["big"]				= ["Giant", "Ogre", "Troll"]
d["species"]["small"] 		= ["Goblin", "Gnome", "Dwarf", "Kobold", "Halfling"]
d["species"]["sneaky"]    = ["Goblin", "Halfling","Half-Elf", "Elf", "Dark Elf"]
d["species"]["primitive"] = ["Goblin", "Ogre", "Troll", "Orc", "Beastman", "Wood Elf", "Sylvan", "Lizard"]
d["species"]["rightous"]  = ["Human", "Celestial", "Beastman", "Dwarf", "Halfling", "Elf"]

d["pattern"] = ["{species[rightous]} {profession[rightous]}", "{species[primitive]} {profession[primitive]}", "{species[smart]} {profession[civilian]}",
								"{species[twisted]} {profession[twisted]}", "{species[dextrous]} {profession[ranged]}", "{species[sneaky]} {profession[sneaky]}",
								"{species[muscular]} {profession[melee]}", "{species[noble]} {profession[noble]}", "{species[smart]} {profession[arcane]}"]

# -----------------------------------------

formatter = GenerativeFormatter(d)

def generate():
	result = formatter.format("{pattern}")
	return result

def get_context(): 
	return "#Character"

def count_permutations(*args):
	return formatter.count_permutations("{pattern}", *args)

if __name__ == "__main__":
	for i in range(0, 20):
		print(generate())