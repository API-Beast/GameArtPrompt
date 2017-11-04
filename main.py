from glob import glob
import random
import importlib.util as impu
from sys import argv
import sys
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

iterations = 50
prompts = []
if len(argv) > 1:
	iterations = int(argv[1])

for i in range(0, iterations):
	generator = random.choice(generators)
	prompt = generator.get_context().rjust(12)+": "+generator.generate()
	if iterations < 1000:
		print(prompt)
	prompts.append(prompt)
	if i > 1 and i%1000 == 0:
		progress = int(i/iterations*100)
		sys.stdout.write("\r[{}] {}%".format('#'*int(progress/5) + ' '*(20-int(progress/5)), progress))
		sys.stdout.flush()


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