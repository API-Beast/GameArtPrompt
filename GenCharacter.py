import random

from lib.Vocab import Vocab
from lib.Vocab import merge_vocab
from lib.GenerativeFormatter import GenerativeFormatter
import random

d = Vocab()
d.include("words.Species")

d["religious_order"] = ["the Purifying Sun", "the Iron Legion", "the Draconic Order", "the Weeping Mistress", "the Eternal Light", "the Crusaders"]
d["religious"] = ["cleric", "paladin", "monk"]
d["historic_inspiration"] = ["East-Asian", "Central-Asian", "Middle-Eastern", "Egyptian", "Germanic", "Nomadic", "Nordic", "Greek", "Roman", "Sumerian", "Tribal", "Mesoamerican"]
d["arctype"] = ["Warrior", "Diplomat", "Soldier", "General", "Merchant"]

d["level"] = [["Elite", "Armored"], "[none]"]

d["mount"] = ["Horse", "Lizard", "Raptor", "Griphon", "Dragon"]

d["horde_tribe"] = ["Iceblood", "Infernal", "Firebringer", "Steelclad", "Deathraiser", "Warborn", "Shadowstalker"]
d["demonic_assoc"] = ["Sin", "Greed", "Lust", "Horror", "Hysteria", "the Blasphemous", "Discord", "Mischief", "Sloth", "Envy", "Pride", "Gluttony", "Domination", "War", "Treason", "Terror", "Wrath", "Temptation", "Nightmare"]

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