from glob import glob
import random
import importlib.util as impu
from sys import argv
import math

themes = glob("Gen*.py")

def load_generator(theme):
	spec = impu.spec_from_file_location(theme[:3], theme)
	generator = impu.module_from_spec(spec)
	spec.loader.exec_module(generator)
	return generator

generators = [load_generator(theme) for theme in themes]

#from argparse import ArgumentParser
#parser = ArgumentParser("Generate a game art prompt.")
#parser.add_argument("")

iterations = 25
prompts = []
if len(argv) > 1:
	iterations = int(argv[1])

for i in range(0, iterations):
	generator = random.choice(generators)
	prompt = generator.get_context().rjust(12)+": "+generator.generate()
	print(prompt)
	prompts.append(prompt)
	if i > 100000 and i%100000 == 0:
		print(str(round(i/iterations*100, 3))+"%")


print("      ")
count = 0
for gen in generators:
	i = gen.count_permutations()
	print("{} has {} permutations".format(gen.get_context().rjust(12), i)) 
	count += i
print()
print("Total of {} possible permutations".format(count))
print()
print("Generated {} unique prompts".format(len(list(set(prompts)))))