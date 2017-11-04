import random

from lib.Vocab import merge_vocab
from lib.GenerativeFormatter import GenerativeFormatter

d = {}

d["flora_style"] 			= ["Alien", "Dark", "Glowing", "Rotting", "Dense", "Frozen", "Voluminous", "Oozing"]
d["flora_prop"] 			= ["Tuft of Grass", "Mushrooms", "Flowers", "Plants", "Tree", "Bush", "Tree Stump", "Vines"]
d["rock_style"] 			= ["Solid", "Collapsing", "Cracked", "Overgrown", "Crystaline", "Mossy", "Limestone", "Sandstone", "Ice", "Oozing"]
d["rock_prop"] 				= ["Rock", "Boulder", "Spire", "Cliff", "Peak", "Crag", "Arch", "Cave Entrance"]
d["structure_style"]	= ["Collapsing", "Crystaline", "Brick", "Macabre", "Rune Etched", "Stone set", "Limestone", "Obsidian", "Sandstone", "Wooden", "Orderly", "Steel", "Magi-Tech", "Primitive", "Ancient", "Mystic", "Ornamental", "Overgrown"]
d["structure"]   			= [["Column", "Pillar"], "Wall", "Floor", "Window", "Door", "Roof", "Gate", "Staircase", "Wall", "Balcony", "Bridge", "Railing"]
d["style"]						= ["Ornamental", "Rotting", "[none]"]
d["container"]				=	["Crate", "Pottery", "Barrels", "Chest", "Bag"]
d["special"]					= ["Stalactite", "Rubble", "Riverside", "Wine Barrel", "Fruit Tree", "Berry Bush", "{style} Tombstone"]
d["patches"]					= ["Patch of Grass", "Patch of Leaves", "Patch of Undergrowth", "Patch of Grain", "{Cracked?} Patch of Stone", "{Cracked?} Sandstone Patch"]
d["profession"]				= ["Alchemists", "Artists", "Sculptors", "Researchers", "Writers", "Engineers", "Tailors", "Woodworkers", "Architects"]
d["merchant"]					= ["Alchemist", "Blacksmith", "Goldsmith", "Runesmith", "Artificer", "Grocer", "Tailor", "Potter"]
d["furniture"]				= ["{merchant}s Display", "{style} bookshelf", "{style} table", "{profession} {style} desk", "{style} cupboard", "{style} bed", "{style} bed"]
# TODO: Floor types
# TODO: Scatter
# TODO: Water
# TODO: Transition

d["pattern"] = ["{patches}", "{furniture}", "{style} {container}", "{flora_style} {flora_prop}", "{rock_style} {rock_prop}", "{structure_style} {structure}"]

formatter = GenerativeFormatter(d)

def generate():
	result = formatter.format("{pattern}")
	return result.title()

def get_context():
	return "#Environment"

def count_permutations(*args):
	return formatter.count_permutations("{pattern}", *args)

if __name__ == "__main__":
	for i in range(0, 20):
		print(generate())