from glob import glob
import random
import importlib.util as impu
from sys import argv

themes = glob("Gen*.py")

#from argparse import ArgumentParser
#parser = ArgumentParser("Generate a game art prompt.")
#parser.add_argument("")

iterations = 10
if len(argv) > 1:
	iterations = int(argv[1])

for i in range(0, iterations):
	theme = random.choice(themes)

	spec = impu.spec_from_file_location(theme[:3], theme)
	generator = impu.module_from_spec(spec)
	spec.loader.exec_module(generator)

	print(generator.generate())


print("      ")
import words.Fantasy
import words.General
from lib.Helpers import merge_words
from lib.Helpers import count_words

d = {}
d = merge_words(d, words.Fantasy.get_all())
d = merge_words(d, words.General.get_all())

print("Dictionairy consists of ", count_words(d), " words and sub-phrases.")