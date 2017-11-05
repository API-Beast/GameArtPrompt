import random

from lib.Vocab import Vocab
from lib.GenerativeFormatter import GenerativeFormatter

d = Vocab()

d["climate"] 				 = ["Grassy", "Desert", "Snowy", "Tropical", "Swamp"]
d["style"]	 				 = ["Mystic", "Primitive", "Stone", "Wooden", "Ornamental"]
d["forest_type"] 		 = ["Alien", "Dark", "Pine", "Lush", "Bamboo"]
d["settlement_type"] = ["Forest", "Mountain", "Harbour", "Primitive", "Destroyed"]
d["raw_metal"]			 = ["Iron", "Copper", "Gold", "Silver", "Mythril"]
d["mined_materials"] = d.merge_sets("raw_metal", ["Coal", "Crystal"])

d["pattern"] = 	["{climate} Mountain", "{climate} Hill", "{climate} Stone Formation", "{forest_type} Forest", "{climate} Riverbed", "Oasis", "{climate} Lake"]
d["pattern"] += ["{climate|style} Fortress", "{climate|style} Encampment", "{climate|settlement_type} Village"]
d["pattern"] += ["{climate|settlement_type} House", "{climate|settlement_type} Town", "{climate} Dungeon Entrance"]
d["pattern"] += [["Storehouse", "Barracks", "Training Ground", "Lumberers Camp", "{mined_materials} Mine"]]
d["pattern"] += [["Church", "Cathedral", "{style} Gatehouse", "{style} Wall", "Workshop"]]
d["pattern"] += [["Farm", "Stables", "{style|Corrupted*} Shrine", "Colossal Statue", "Colossal Dragon Skeleton"]]
d["pattern"] += [["Alchemists Lab", "Blacksmith", "Bowmakers Shop", "Enchanters Atelier"]]

formatter = GenerativeFormatter(d)

def generate():
	result = formatter.format("{pattern}")
	return result.title()

def get_context():
	return "#WorldMap"

def count_permutations(*args):
	return formatter.count_permutations("{pattern}", *args)

if __name__ == "__main__":
	for i in range(0, 20):
		print(generate())