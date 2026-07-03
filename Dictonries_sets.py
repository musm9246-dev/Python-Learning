# ===================================================
# Dictionaries in Python
# ===================================================
# We can store any type of data in a dictionary (key : value pairs)

info = {
    "name": "Usman",
    "age": "21",
    "CGPA": "3.21"
}
print(info)
print(type(info))
print(info["name"])
info["CGPA"] = "3.36"
print(info["CGPA"])
info["Section"] = "6B"     # we can also add a new key-value pair like this
print(info)

# We can also create an empty dictionary and add data to it later
# NOTE: avoid naming it "dict" since that shadows Python's built-in dict type
my_dict = {}
print(my_dict)
my_dict["name"] = "Ali"
print(my_dict)

# ===================================================
# Nested Dictionaries (a dictionary inside another dictionary)
# ===================================================
student = {
    "name": "Ali",
    "age": "23",
    "subjects": {
        "phy": "3.04",
        "chem": "3.75",
        "Bio": "3.98"
    },
    "Section": "6B"
}
print(student)
print(student["subjects"])
print(student["subjects"]["phy"])   # if we need only one specific subject

# ===================================================
# Dictionary Methods
# ===================================================

# 1. keys() -> returns only the keys
info = {
    "name": "Usman",
    "age": "21",
    "CGPA": "3.21"
}
print(info.keys())
print(list(info.keys()))       # if we want keys as a list, type-cast like this
print(len(info))                # count of keys (works directly on the dict)
print(len(list(info.keys())))   # count of keys (via the list)

# 2. values() -> returns only the values
print(info.values())
print(list(info.values()))      # if we want values as a list, type-cast like this
print(len(info))                 # count of values
print(len(list(info.values())))  # count of values

# 3. items() -> returns both keys and values (as key-value pairs)
print(info.items())
print(list(info.items()))        # if we want items as a list, type-cast like this
print(len(info))                  # count of items
print(len(list(info.items())))    # count of items
pairs = list(info.items())
print(pairs[2])                    # access a specific (key, value) pair by index

# 4. get() -> returns the value for a given key
print(info["name"])
print(info.get("name"))

# 5. update() -> insert/merge specific items into the dictionary
info.update({"city": "Lahore"})
print(info)

# ===================================================
# Sets in Python
# ===================================================
# The elements inside a set must be immutable, but the set itself is mutable.
# A set automatically ignores duplicate values.

collection = {1, 4, 2, 7, 5}
print(collection)
print(len(collection))
print(type(collection))

# Empty set
# collection = {}   -> This is actually the syntax for an EMPTY DICTIONARY, not a set!
collection = set()   # This is the correct syntax for an empty set
print(type(collection))

# ===================================================
# Set Methods
# ===================================================

# 1. add() -> add an element (anything except a list, since lists aren't hashable)
collection = set()
collection.add(1)
collection.add("Hello world")
collection.add(9)
print(collection)

# 2. remove() -> remove a specific element
collection = {5, 6, "hello", 9, 2}
collection.remove("hello")
collection.remove(5)
print(collection)

# 3. clear() -> clears/empties the whole set
collection = {5, 6, "hello", 9, 2}
print(len(collection))
collection.clear()
print(collection)

# 4. pop() -> removes and returns a RANDOM value (sets are unordered)
collection = {"Hello", "kim so hyun", "ko munsuk", 1, 5}
print(collection.pop())
print(collection.pop())
print(collection.pop())

# 5. union() -> combines elements from both sets (no duplicates)
set_1 = {1, 2, 3, 4}
set_2 = {5, 6, 7, 8}
print(set_1.union(set_2))

# 6. intersection() -> only the elements common to both sets
set_1 = {1, 2, 3, 4, 6}
set_2 = {5, 6, 7, 8, 4, 2, 3}
print(set_1.intersection(set_2))

# ===================================================
# Practice Programs
# ===================================================

# 1. Add words and their meanings to a dictionary
dictionary = {
    "cat": "a small animal",
    "table": ["a piece of furniture", "list of facts and figures"]
}
print(dictionary)

# 2. A list of subjects for students is given.
# Assume one classroom is required per unique subject.
# python, c++, java, python, javascript, java, python, java, c++, c
students = {"python", "C++", "java", "python", "javascript", "java", "python", "java", "C++", "C"}
print(len(students))    # a set automatically removes duplicates, so this gives
                         # the number of UNIQUE subjects -> number of classrooms needed
