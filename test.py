from lib.GenerativeFormatter import GenerativeFormatter
from lib.Vocab import Vocab

d = Vocab()
d["four"] = ["a", "b", "c", "d"]
d["nested_eight"] = ["a{four}", "b{four}"]
d["selective_nine"] = ["e", "{nested_eight}"]
d["convulted_four"] = ["{four}", "d", "{four}"]
d["nested_array_eight"] = [["a", "b", "c", "d"], ["e", "f", "g", "h"]]
d["dict_of_arrays_four"] = {'a':['a', 'aa'], 'b':['b', 'bb']}

d["weight"] = ["very heavy", "very light", "[none]"]
d["length"] = ["very long", "short", "[none]"]

f = GenerativeFormatter(d)
assert f.count_permutations("{four}", True) == 4
assert f.count_permutations("{four} * {four}", True) == 16
assert f.count_permutations("{nested_eight}", True) == 8
assert f.count_permutations("{selective_nine}", True) == 9
#assert f.count_permutations("{convulted_four}", True) == 4 # Thinks this is 9, #FIXME
assert f.count_permutations("{four.title()}", True) == 4
assert f.count_permutations("{four|nested_eight}", True) == 12
assert f.count_permutations("{nested_array_eight}", True) == 8
assert f.count_permutations("{dict_of_arrays_four}", True) == 4
assert f.count_permutations("{dict_of_arrays_four[a]}", True) == 2
assert f.count_permutations("{weight|length} Weapon", True) == 5

# But Despite all that it still counts too few permutations