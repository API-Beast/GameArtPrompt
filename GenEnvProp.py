import random

from lib.Vocab import merge_vocab
from lib.GenerativeFormatter import GenerativeFormatter

import words.Fantasy
import words.General

d = {}
d = merge_vocab(d, words.Fantasy.get_all())
d = merge_vocab(d, words.General.get_all())
d["manmade_style"] 	= ["Futuristic", "Fantasy", "Military", "Cyberpunk", "Steampunk", "Historic", "Macabre", "Modern", "Primitive", "Ancient", "Mystic"]
d["manmade_prop"] = ["Crates", "Pottery", "Barrels", "Bucket", "Machinery", "Chair", "Bench", "Sign", "Chest", "Light Source", "Fence"]
d["flora_style"] 	= ["Alien", "Dark", "Glowing", "Arid", "Dense", "Bright", "Neat", "Frozen", "Voluminous"]
d["flora_prop"] 	= ["Tuft of Grass", "Mushrooms", "Flowers", "Plants", "Trees", "Bushes", "Tree Stump"]
d["rock_style"] 	= ["Solid", "Broken", "Smooth", "Overgrown", "Magic-imbued"]
d["rock_prop"] 		= ["Rock", "Crystal"]

patterns = []
patterns.append("{manmade_style} {manmade_prop}")
patterns.append("{flora_style} {flora_prop}")
patterns.append("{rock_style} {rock_prop}")

def generate():
	formatter = GenerativeFormatter(d)
	pattern = random.choice(patterns)
	result = formatter.format(pattern)
	return result

def get_context():
	return "#EnvProps"

if __name__ == "__main__":
	for i in range(0, 10):
		print(generate())