import random

from lib.Vocab import merge_vocab
from lib.GenerativeFormatter import GenerativeFormatter

import words.Fantasy
import words.General

d = {}
d = merge_vocab(d, words.Fantasy.get_all())
d = merge_vocab(d, words.General.get_all())

patterns = []
patterns.append("The {attribute} {player} talks to [a/an] {emotion} {civilian}.")
patterns.append("Old temple dedicated to the {specific_god}.")
patterns.append("{faction.capitalize()} {unit}.")
patterns.append("{faction.capitalize()} {building} made of {material} and {material}.")
patterns.append("{faction.capitalize()} {building} infested by {creature.plural()}.")

def generate():
	formatter = GenerativeFormatter(d)
	pattern = random.choice(patterns)
	result = formatter.format(pattern)
	return result

def get_context():
	return "Fantasy"

if __name__ == "__main__":
	for i in range(0, 10):
		print(generate())