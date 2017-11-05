import random

from lib.Vocab import Vocab
from lib.Vocab import merge_vocab
from lib.GenerativeFormatter import GenerativeFormatter

# TODO: More focus on animations with context
# A wolf jumping over a small obstacle
# A wolf calling for reinforcements
# A rogue sliding below a edge/behind cover
# A commander giving his subordinate a command
# A character being impaled on a spike
# A character falling down a ledge
# A character jumping down a ledge
# A moving character being hit by an arrow
# A character being kicked back by his opponent
# A character evading a attack with the sword
# A knight bracing himself against an incoming arrow
# An snake snapping after it's unsuspecting prey
# An scroundel lying in wait
# A wolf jumping at it's prone target
# A boar charging at the fearless warrior
# A massive warrior disposing multiple men with a single blow
# A muscular warrior grabbing his enemy and pushing him away
# A berserker falling into a frenzied rage
# A character slowly moving forward in a snow storm
# A character ascending the stairs
# A powerful blow sending the opponent flying
# A rogue delivering a quick stab
# A smith lost in his work
# An serf delivering material to a local craftsman
# A coiling snake
# A burning campfire
# A lion roaring intimidating his opponent

d = Vocab()
d.include("words.Spells")

d["pattern"] = []
d["pattern"] += ["\"{magic_spell}\" Spell"]

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