"""
An advanced string formatter for inserting random words into the placeholders.
"""

from string import Formatter
from .Vocab import combine
import random

class GenerativeFormatter(Formatter):
	def __init__(self, db, num_iterations = 10):
		Formatter.__init__(self)
		self.vocab = db
		self.iterations = num_iterations

	def format(self, format_string, *args, **kwargs):
		result = format_string
		for i in range(1, self.iterations):
			result = self.vformat(result, args, kwargs)
		result = self.replace_placeholders(result)
		return result

	def replace_placeholders(self, string):
		# replace [a/an] with the indefinite article
		tmp = string
		while "[a/an]" in tmp:
			parts = tmp.split("[a/an]", 1)
			letters = [parts[1][1], parts[1][2]]

			if letters[0] in ['a', 'e', 'i', 'o']:
				tmp = parts[0] + "an" + parts[1]
				continue

			if letters[0] == 'u':
				if letters[1] in ['n', 'l']:
					tmp = parts[0] + "an" + parts[1]
					continue

			if letters[0] == 'h':
				if letters[1] == 'i':
					tmp = parts[0] + "an" + parts[1]
					continue

			tmp = parts[0] + "a" + parts[1]
		# Remove [empty] along with any superfluous whitespace
		while "[empty]" in tmp:
			parts = tmp.split("[empty]", 1)
			tmp = parts[0].rstrip()+" "+parts[1].lstrip()

		return tmp

	def expand(self, items, *args, **kwargs):
		result = []
		for item in items:
			result.append(self.get_field(item, args, kwargs))
		return result

	def get_field(self, field_name, args, kwargs):
		if field_name.endswith("()"):
			parts = field_name.rsplit(".", 1)
			obj = self.get_field(parts[0], args, kwargs)[0]
			funcName = parts[1][:-2]
			func = getattr(self, "func_"+funcName, None)

			if isinstance(obj, (list, tuple)):
				return ([func(x) for x in obj], 0)
			if isinstance(obj, dict):
				return ([func(x) for x in list(obj.values())], 0)
		else:
			return Formatter.get_field(self, field_name, args, kwargs)

	def get_value(self, key, args, kwargs):
		if key in kwargs:
			return kwargs[key]

		if isinstance(key, int):
			return args[key]

		# {a-b}: set of things only in a
		if '-' in key:
			firstKey, secondKey = key.split('-', 1)
			a = set(self.get_value(firstKey, args, kwargs))
			b = set(self.get_value(secondKey, args, kwargs))
			return list(a-b) 

		# {a&b}: set of things that are in both a and b
		if '&' in key:
			firstKey, secondKey = key.split('&', 1)
			a = set(self.get_value(firstKey, args, kwargs))
			b = set(self.get_value(secondKey, args, kwargs))
			return list(a&b) 

		# {a|b}: set of things that are in either a  or b
		if '|' in key:
			firstKey, secondKey = key.split('|', 1)
			a = self.get_value(firstKey, args, kwargs)
			b = self.get_value(secondKey, args, kwargs)
			return combine(a, b) 

		val = self.vocab[key]
		return val

	def format_field(self, value, format_spec):
		val = value
		if isinstance(val, (list, tuple)):
			val = self.format_field(random.choice(val), format_spec)
		if isinstance(val, dict):
			val = self.format_field(list(val.values()), format_spec)

		return Formatter.format_field(self, val, format_spec)

	# The builtin string manipulation methods
	def func_plural(self, string):
		return string + "s"

	def func_capitalize(self, string):
		return string.capitalize()

	def func_title(self, string):
		return string.title()