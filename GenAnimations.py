import random

from lib.Vocab import Vocab
from lib.Vocab import merge_vocab
from lib.GenerativeFormatter import GenerativeFormatter

d = Vocab()

d["characteristic"] = ["heavy-weight", "short", "quick", "very muscular", "very scrawny", "shy", "very aggressive", "hunched", "[empty]"] 
d["generic_action"] = ["idle", "walking", "running", "fleeing", "jumping", "falling", "dying"]
d["weight"] = ["very heavy", "very light", "[empty]"]
d["length"] = ["very long", "short", "[empty]"]
d["size"]		= ["enormous", "large", "small", "[empty]"]
d["weapon"] = ["a {weight} sword", "a war hammer", "a {weight|length} polearm", "a {weight|length} staff", "a {length} bow", "a {size} gun", "fists", "claws"]
d["character"] = ["{characteristic} character", "{characteristic} scholar", "{characteristic} mage", "{characteristic} warrior", "{characteristic} berserker"]
d["creature"] = ["{characteristic} animal"]
d["specific_animation"] = ["charging bull", "fire-breathing dragon"]

patterns = []
patterns.append("{generic_action.capitalize()} animaton of a {character}.")
patterns.append("{generic_action.capitalize()} animaton of a {character} wielding {weapon}.")
patterns.append("{generic_action.capitalize()} animaton of a {creature}.")
patterns.append("Animation of a {character} attacking with {weapon}.")
patterns.append("Animation of a {specific_animation}.")

def generate():
	formatter = GenerativeFormatter(d)
	pattern = random.choice(patterns)
	result = formatter.format(pattern)
	return result

def get_context():
	return "#Animation"

if __name__ == "__main__":
	for i in range(0, 10):
		print(generate())