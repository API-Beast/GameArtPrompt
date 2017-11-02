from glob import glob
import random
import importlib.util as impu
from sys import argv

themes = glob("Gen*.py")

#from argparse import ArgumentParser
#parser = ArgumentParser("Generate a game art prompt.")
#parser.add_argument("")

iterations = 50
if len(argv) > 1:
	iterations = int(argv[1])

for i in range(0, iterations):
	theme = random.choice(themes)

	spec = impu.spec_from_file_location(theme[:3], theme)
	generator = impu.module_from_spec(spec)
	spec.loader.exec_module(generator)

	print(generator.get_context().rjust(12)+":", generator.generate())


print("      ")
import words.Fantasy
import words.General
from lib.Vocab import merge_vocab
from lib.Vocab import count_vocab

d = {}
d = merge_vocab(d, words.Fantasy.get_all())
d = merge_vocab(d, words.General.get_all())

print("Dictionairy consists of", count_vocab(d), "words and sub-phrases.")