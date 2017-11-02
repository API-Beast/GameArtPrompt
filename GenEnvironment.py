import random

from lib.Vocab import merge_vocab
from lib.GenerativeFormatter import GenerativeFormatter

d = {}

d["flora_style"] 			= ["Alien", "Dark", "Glowing", "Rotting", "Dense", "Frozen", "Voluminous", "Oozing"]
d["flora_prop"] 			= ["Tuft of Grass", "Mushrooms", "Flowers", "Plants", "Trees", "Bushes", "Tree Stump"]
d["rock_style"] 			= ["Solid", "Collapsing", "Overgrown", "Crystaline", "Mossy", "Limestone", "Sandstone", "Oozing"]
d["rock_prop"] 				= ["Rock", "Cliff", "Cave Entrance"]
d["structure_style"]	= ["Collapsing", "Macabre", "Rune Etched", "Stone set", "Limestone", "Sandstone", "Wooden", "Orderly", "Steelclad", "Primitive", "Ancient", "Mystic", "Ornamental", "Overgrown"]
d["structure"]   			= ["Collumn", "Wall", "Floor", "Window", "Door", "Roof", "Gate", "Staircase", "Wall", "Balcony", "Bridge", "Railing"]
d["container_style"]	= ["Ornamental", "Steelclad", "Simple", "Fantasy", "Steampunk"]
d["container"]				=	["Crate", "Pottery", "Barrels", "Chest"]

patterns = []
patterns.append("{container_style} {container}")
patterns.append("{flora_style} {flora_prop}")
patterns.append("{rock_style} {rock_prop}")
patterns.append("{structure_style} {structure}")


formatter = GenerativeFormatter(d)

def generate():
	pattern = random.choice(patterns)
	result = formatter.format(pattern)
	return result

def get_context():
	return "#Environment"

def count_permutations():
	return formatter.count_permutations(patterns)

if __name__ == "__main__":
	for i in range(0, 10):
		print(generate())