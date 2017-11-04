import random

from lib.Vocab import Vocab
from lib.Vocab import merge_vocab
from lib.GenerativeFormatter import GenerativeFormatter

d = Vocab()

d["characteristic"] = ["heavy-weight", "short", "quick", "very muscular", "very scrawny", "shy", "very aggressive", "hunched", "[none]"] 
d["generic_action"] = ["idle", "walking", "running", "fleeing", "jumping", "falling", "death"]
d["subject_action"]	= ["charging at", "executing", "evading", "running away from"]
d["weight"] = ["very heavy", "very light", "[none]"]
d["length"] = ["very long", "short", "[none]"]
d["size"]		= [["over-sized", "enormous"], "large", "small", "[none]"]
d["speed"]	= ["slow", "fast", "[none]"]
d["weapon"] = ["[a/an] {weight} sword", "[a/an] {size} war hammer", "a ball and chain", "[a/an] {weight|length} polearm", "[a/an] {weight|length} staff", "[a/an] {length} bow", "[a/an] {size} gun", "fists", "claws"]
d["character"] = {}
d["character"]["general"] = ["character", "scroundel", "ranger"]
d["character"]["magic"]		= ["cleric", "mage", "scholar"]
d["character"]["melee"]		= ["warrior", "berserker", "knight"]
d["undead"] = ["zombie", "skeleton", "mummy", "lich", "ghost"]
d["breath_weapon"] = ["fire-breathing", "ice-breathing", "acid-spewing"]
d["specific_animation"] = ["{breath_weapon} creature", "{undead} rising out of it's grave"]
d["bolt_element"] = ["Fiery", "Ice", "Lightning", "Necrotic"]
d["attunment"] = ["Holy", "Elemental", ["Unholy", "Dark", "Corrupted"]]
d["magic_spell"] = 	["Cleansing Light", "Burning Inferno", "Portal", "Teleportation",
										"Summon Demon", "Protective Aura", "Petrifying Gaze", "Dust Devil",
										"{bolt_element} Bolt", "{bolt_element} Blast", "{bolt_element} Barrage", "Telekinesis",
										"Tsunami", "Summon Undead", "{attunment} Healing"]
d["attack_desc"] = ["precise attack", "fast attack", "brutal attack", "barrage"]

d["character_detail"] = ["heavily armored {character}", "{character} armed with {weapon}", "{characteristic} {character}"]
d["creature"] = ["{size|weight|speed} animal", "{size} rabbit", ["alpha wolf", "wolf", "dog"], "cat", "bull"]

d["pattern"] = []
d["pattern"].append("{generic_action.capitalize()} animaton for [a/an] {character_detail}.")
d["pattern"].append("{generic_action.capitalize()} animaton for [a/an] {creature}.")
d["pattern"].append("Animation of [a/an] {character} launching [a/an] {attack_desc} with {weapon}.")
#d["pattern"].append("Animation of [a/an] {specific_animation}.")
d["pattern"].append("\"{magic_spell}\" Spell")

formatter = GenerativeFormatter(d)

def generate():
	result = formatter.format("{pattern}")
	return result

def count_permutations(*args):
	return formatter.count_permutations("{pattern}", *args)

def get_context():
	return "#Animation"

if __name__ == "__main__":
	for i in range(0, 20):
		print(generate())