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
s["undead"]["essence"] = ["Soulstarved", "Cursed", "Tormented", "Creeping Death", "Pestilence", "Spectral", "Shadowspectre", "Undying", "Fleshstitcher", "Bonecarver", "Soulswamp", "Iron Legion", "Corpserot"]
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
s["elven"]["subclass"] = ["Dark Elf", "Wood Elf", "High Elf"]

s["elven"]["Dark Elf"] = {}
s["elven"]["Dark Elf"]["unit"] = s["elven"].merge_sets("unit", ["Torturer", "Slaver", "Infiltrator", "Mistress"])

s["elven"]["Wood Elf"] = {}
s["elven"]["Wood Elf"]["unit"] = s["elven"].merge_sets("unit", ["Hunter", "Beastmaster", "Shaman", "Warlock"])

s["elven"]["High Elf"] = {}
s["elven"]["High Elf"]["unit"] = s["elven"].merge_sets("unit", ["Paladin", "Chavalier"])

s["elven"]["pattern"] = ["{~subclass} {#unit}"]


# -----------------------------------------
s["generic"] = Vocab()
s["generic"]["element"] = ["Holy", "Corrupted"]
s["generic"]["pattern"] = ["{element} Knight"]

def generate():
	formatter = GenerativeFormatter(d)
	faction = random.choice(list(s.keys()))
	formatter.set_vocab(s[faction], d, s)
	result = formatter.format("{pattern}")
	return result

def get_context(): 
	return "#Character"

if __name__ == "__main__":
	for i in range(0, 20):
		print(generate())