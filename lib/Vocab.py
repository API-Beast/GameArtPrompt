
class Vocab(dict):
	def merge_sets(self, *args):
		retVal = set()
		for arg in args:
			retVal |= set(self[arg])
		return list(retVal)

	def copy(self):
		return Vocab(dict.copy(self))
		

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
				result[key] = merge_words(result[key], second[key])
			else:
				result[key] = second[key]
		return Vocab(result)

	return first