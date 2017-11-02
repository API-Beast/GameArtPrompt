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

s = Vocab()

# -------------------------------------
s["undead"] = Vocab()
s["undead"]["unit"] = ["Archer", "Rider", "Knight", "Assassin", "Soldier", "Thrall", "Ghoul", "Zombie", "Executioner", "Lieutenant"]
s["undead"]["essence"] = ["Soulstarved", "Embalmed", "Cursed", "Tormented", "Creeping Death", "Pestilence", "Spectral", "Shadowspectre", "Undying", "Fleshstitcher", "Bonecarver", "Soulswamp", "Iron Legion", "Corpserot"]
s["undead"]["special"] = ["Necromancer", "Lich", "Golem", "Revenant"]

s["undead"]["pattern"] = ["Undead {essence} {unit}", "{essence} {special}"]


# --------------------------------------
s["demonic"] = Vocab()
s["demonic"]["demon_unit"] = ["Warlord", "Infiltrator", "Assassin", "Commander", "Torturer", "Beastmaster", "Warrior", "Raider"]
s["demonic"]["demonic_unit"] = ["Swarmer", "Grunt", "Juggernaut", "Behemoth"]
s["demonic"]["worshipper"] = ["Summoner", "Warlock", "Cultist", "Conjurer", "High Priest"]
s["demonic"]["species"] = ["Succubus", "Imp"]
s["demonic"]["assoc"] = ["Sin", "Greed", "Lust", "Horror", "Hysteria", "the Blasphemous", "Discord", "Mischief", "Sloth", "Envy", "Pride", "Gluttony", "Domination", "War", "Treason", "Terror", "Wrath", "Temptation", "Nightmare"]

s["demonic"]["pattern"] = ["{level} Demon {demon_unit} of {assoc}", "{level} Demonic {demonic_unit}", "{worshipper} of {assoc}"]


# ---------------------------------------
s["orcish"] = Vocab()
s["orcish"]["unit"] = ["Warlord", "Grunt", "Archer", "Torturer", "Raider", "Assassin", "Shaman", "Warlock", "Warrior", "Slaver", "Javelin Thrower", "Berserker", "Juggernaut", "Shieldbearer", "Beastmaster"]
s["orcish"]["tribe"] = ["Iceblood", "Infernal", "Firebringer", "Steelclad", "Deathraiser", "Warborn", "Shadowstalker"]

s["orcish"]["pattern"] = ["{level|tribe} Orc {unit}", "{tribe} Orc {unit}"]


# ---------------------------------------
s["divine"] = Vocab()
s["divine"]["unit"] = ["Judge", "Executioner", "Commander", "Seraphim", "Fanatic", "Scribe", "Guardian", "Paladin"]
s["divine"]["assoc"] = ["Purifying Flame", "Last Stand", "Order"]

s["divine"]["pattern"] = ["Divine {unit} of The {assoc}", "Corrupted Divine {unit}"]


# ---------------------------------------
s["elven"] = Vocab()
s["elven"]["unit"] = ["Noble", "Lord", "Ranger", "Ascended", "High Priest", "Runesmith", "Shieldbearer", "Alchemist", "Arcanist", "Assassin"]

s["elven"]["dark_unit"] = s["elven"].merge_sets("unit", ["Torturer", "Slaver", "Infiltrator", "Mistress"])
s["elven"]["wood_unit"] = s["elven"].merge_sets("unit", ["Hunter", "Druid", "Beastmaster", "Shaman", "Warlock"])
s["elven"]["high_unit"] = s["elven"].merge_sets("unit", ["Paladin", "Chavalier"])

s["elven"]["pattern"] = ["Dark Elf {dark_unit}", "Wood Elf {wood_unit}", "High Elf {high_unit}"]


# -----------------------------------------
s["generic"] = Vocab()
s["generic"]["element"] = ["Holy", "Corrupted"]

d["mount"] = ["Horse", "Lizard", "Dinosaur", "Griphon", "Dragon"]

d["profession"] = {}
d["profession"]["ranged"]		= ["Ranger", "Marksman", "Bowman"]
d["profession"]["melee"] 		= ["Militia", "City Guard", "Hoplite", "Spearman", "Paladin", "Swordsman", "Pikeman", "Knight", "Juggernaut"]
d["profession"]["mounted"] 	= ["Chavalier", "Knight", "{mount}rider", "Cataphract"]
d["profession"]["civilian"] = ["Lumberjack", ["Huntsman", "Hunter"], "Farmer", "Alchemist", "Smith", "Noble"]
d["profession"]["noble"]		= ["Duke", "King", "Count", "Prince"]
d["profession"]["command"]	= ["Commander", "General"]
d["profession"]["magician"] = ["Enchanter", "Illusionist", "Elementalist", "Shaman", "Runesmith", "Cleric", "Priest", "Druid"]

d["species"] = {}
d["species"]["special"] 	= ["Avian", "Celestial", "Sylvan", "Lizard", "Merman", "Demonic", "Naga", "Cat"]
d["species"]["scrawny"] 	= ["Half-Elf", "Elf", "Dark Elf"]
d["species"]["muscular"] 	= ["Orc", "Beastman", "Half-Orc", "Human", "Dwarf"]
d["species"]["big"]				= ["Giant", "Ogre", "Troll"]
d["species"]["small"] 		= ["Goblin", "Gnome", "Dwarf", "Kobold", "Halfling"]

s["generic"]["pattern"] = ["{species} {profession}"]

formatter = GenerativeFormatter(d)

def generate():
	faction = random.choice(list(s.keys()))
	formatter.set_vocab(s[faction], d, s)
	result = formatter.format("{pattern}")
	return result

def get_context(): 
	return "#Character"

def count_permutations():
	i = 0
	for faction in list(s.keys()):
		formatter.set_vocab(s[faction], d, s)
		i += formatter.count_permutations("{pattern}")
	return i

if __name__ == "__main__":
	for i in range(0, 20):
		print(generate())