import sys

# List example
prime_numbers = [2, 3, 5, 7, 11, 13, 17]
# Tuple example
perfect_squares = (1, 4, 9, 16, 25, 36)
print("List methods")
print(dir(prime_numbers))
print(80*"-")
print("Tuple methods:")
print(dir(perfect_squares))
print(dir(sys))
print(help(sys.getsizeof))

list_eg = [1, 2, 3, "a", "b", "c", True, 3.14159]
tuple_eg = (1, 2, 3, "a", "b", "c", True, 3.14159)
set_eg = {1, 2, 3, "a", "b", "c", True, 3.14159}
dict_eg = {1: None, 2: None, 3: None, "a": None, "b": None, "c": None, True: None, 3.14159: None}

print("Tuple size =", sys.getsizeof(tuple_eg), "bytes")
print("List size =", sys.getsizeof(list_eg), "bytes")
print("Dict size =", sys.getsizeof(dict_eg), "bytes")
print("Set size =", sys.getsizeof(set_eg), "bytes")
