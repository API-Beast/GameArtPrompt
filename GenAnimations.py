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
d["bolt_element"] = ["fiery", "ice", "lightning", "necrotic"]
d["attunment"] = ["holy", "elemental", ["unholy", "dark", "corrupted"]]
d["magic_spell"] = 	["a cleansing light spell", "a burning inferno", "opening a portal", "an teleportation spell",
										"the summoning of a demon", "a protective aura", "a petrifying gaze", "a dust storm",
										"[a/an] {bolt_element} bolt", "[a/an] {bolt_element} blast", "[a/an] barrage of {bolt_element}", "telekinesis",
										"a blast of wind", "a crushing tsunami", "a undead summoning spell", "[a/an] {attunment} healing spell"]
d["attack_desc"] = ["precise attack", "fast attack", "brutal attack", "barrage"]

d["character_detail"] = ["heavily armored {character}", "{character} armed with {weapon}", "{characteristic} {character}"]
d["creature"] = ["{size|weight|speed} animal", "{size} rabbit", ["alpha wolf", "wolf", "dog"], "cat", "bull"]

d["pattern"] = []
d["pattern"].append("{generic_action.capitalize()} animaton for [a/an] {character_detail}.")
d["pattern"].append("{generic_action.capitalize()} animaton for [a/an] {creature}.")
d["pattern"].append("Animation of [a/an] {character} launching [a/an] {attack_desc} with {weapon}.")
#d["pattern"].append("Animation of [a/an] {specific_animation}.")
d["pattern"].append("Special effects for {magic_spell}.")

def generate():
	formatter = GenerativeFormatter(d)
	result = formatter.format("{pattern}")
	return result

def get_context():
	return "#Animation"

if __name__ == "__main__":
	for i in range(0, 10):
		print(generate())