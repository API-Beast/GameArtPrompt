
from importlib import import_module

class Vocab(dict):
	def lookup(self, key):
		keys = key.split(".")
		val = self
		for k in keys:
			val = val[k]
		if isinstance(val, dict):
			val = list(val.values())
		return val

	def merge_sets(self, *args):
		retVal = list()
		for arg in args:
			if isinstance(arg, (list, tuple)):
				retVal += arg
			else:
				retVal += self.lookup(arg)

		# Remove duplicates
		unique_list = []
		[unique_list.append(obj) for obj in retVal if obj not in unique_list]
		return unique_list

	def include(self, path):
		module = import_module(path)
		module.write_to(self)


	def copy(self):
		return Vocab(dict.copy(self))
		

def combine(a, b):
	retVal = a + b
	unique_list = []
	[unique_list.append(obj) for obj in retVal if obj not in unique_list]
	return unique_list

def count_vocab(words):
	if isinstance(words, (list, tuple, set)):
		count = 0
		for val in words:
			count += count_vocab(val)
		return count
	elif isinstance(words, dict):
		count = 0
		for key, val in words.items():
			count += count_vocab(val)
		return count
	else:
		return 1

def merge_vocab(first, second):

	if isinstance(first, (list, tuple, set)):
		return list(set(first) | set(second))

	if isinstance(first, dict):
		result = first.copy()
		for key, val in second.items():
			if key in result:
				result[key] = merge_vocab(result[key], second[key])
			else:
				result[key] = second[key]
		return Vocab(result)

	return first