import sys
animals = {"cat", "dog", "tiger", "elephant"}
animals_list = ["cat", "dog", "tiger", "elephant"]
wild_animals = ["tiger", "leopard", "elephant", "ferret"]
domestic_animals = {"cat", "dog", "ferret"}
mad_animals = ["squirrel"]
print("List size =", sys.getsizeof(animals_list), "bytes")
print("Set size =", sys.getsizeof(animals), "bytes")

print("Check for monkey in animals")
print("monkey" in animals)
animals.add("monkey")
print("Check for monkey in animals after adding monkey")
print("monkey" in animals)

animals.update(wild_animals)
print("added wild animals:", animals)

animals.update(mad_animals, {"dolphins"})
print("added mad_animals:", animals)

animals.discard("elephant")
print("discard elephant:", animals)
animals.remove("dog")
print("removed dog:", animals)

# discard does not error on non existing item in set
animals.discard("ferret")
# Uncomment remove will show error no ferret found
#animals.remove("ferret")

animals.clear()
print("removed all items in set:", animals)

animals = set(wild_animals)
print("animals:", animals)

animals = domestic_animals.union(wild_animals)
print("union between domestic and wild animals:", animals)
animals = set(wild_animals) | domestic_animals
print("pipe between domestic | wild animals:", animals)
wild_animals_set = set(wild_animals)
animals = domestic_animals.intersection(wild_animals_set)
print("animal intersection:", animals)
animals = wild_animals_set & domestic_animals
print("animal intersection using & ampersand:", animals)

