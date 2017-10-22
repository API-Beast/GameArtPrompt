import random

from lib.Helpers import merge_words
from lib.GenerativeFormatter import GenerativeFormatter

import words.Fantasy
import words.General

d = {}
d = merge_words(d, words.Fantasy.get_all())
d = merge_words(d, words.General.get_all())

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