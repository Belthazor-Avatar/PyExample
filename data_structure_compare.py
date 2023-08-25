import sys
import timeit

list_eg = [1, 2, 3, "a", "b", "c", True, 3.14159]
tuple_eg = (1, 2, 3, "a", "b", "c", True, 3.14159)
set_eg = {1, 2, 3, "a", "b", "c", True, 3.14159}
dict_eg = {"a": 1, "b": 2, "c": 3, "d": "a", "e": "b", "f": "c", "g": True, "h": 3.14159}

print("Tuple size =", sys.getsizeof(tuple_eg), "bytes")
print("List size =", sys.getsizeof(list_eg), "bytes")
print("Dict size =", sys.getsizeof(dict_eg), "bytes")
print("Set size =", sys.getsizeof(set_eg), "bytes")

list_test = timeit.timeit()