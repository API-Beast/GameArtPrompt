import random

from lib.Vocab import Vocab
from lib.Vocab import merge_vocab
from lib.GenerativeFormatter import GenerativeFormatter
import random

d = Vocab()

d["pattern"] = []

d["humanoid"] = {}
d["humanoid"]["special"]  = ["Avian", "Celestial", "Sylvan", "Lizard", "Merman", "Demonic", "Naga", "Cat"]
d["humanoid"]["scrawny"]  = ["Half-Elf", "Elf", "Dark Elf"]
d["humanoid"]["muscular"]	= ["Orc", "Beastman", "Half-Orc", "Human", "Dwarf"]
d["humanoid"]["big"]      = ["Giant", "Ogre", "Troll"]
d["humanoid"]["small"] 		= ["Goblin", "Gnome", "Dwarf", "Kobold", "Halfling"]
d["living_creature"]      = d.merge_sets("humanoid")

# -------------------------------------
d["undead_unit"] = ["Archer", "Soldier", "Magician", "Executioner", "Lieutenant"]
d["undead_essence"] = ["Souldrained", "Embalmed", "Tormented", "Pestilence", "Fleshstitcher", "Bonecarver", "Soulswamp", "Iron Legion", "Corpserot"]
d["undead_special"] = ["Lich", "Golem", "Revenant", "Thrall", "Ghoul", "Zombie"]

d["undead_pattern"] = ["Undead {living_creature}", ["Undead {undead_essence} {undead_unit}", "Spectral {undead_unit}"], "{undead_essence} {undead_special}"]

d["pattern"] += d["undead_pattern"]

# -----------------------------------------

formatter = GenerativeFormatter(d)

def generate():
	result = formatter.format("{pattern}")
	return result

def get_context(): 
	return "#Creature"

def count_permutations(*args):
	return formatter.count_permutations("{pattern}", *args)

if __name__ == "__main__":
	for i in range(0, 20):
		print(generate())