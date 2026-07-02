# ===================================================
# Tuples in Python
# ===================================================
# Tuples are immutable, just like strings
# (we cannot add, remove, or change elements once created)

Tup = (2, 4, 6, 8, 1)
print(type(Tup))
print(Tup[0])
print(Tup[3])
# Tup[0] = "5"   -> Not allowed here, this only works on lists

# ===================================================
# Empty tuple
# ===================================================
tup = ()
print(tup)
print(type(tup))

# ===================================================
# Single value tuple
# ===================================================
# A comma at the end is REQUIRED to make Python treat it as a tuple.
# Without the comma, Python just treats it as a regular value in brackets.

tup = (1,)              # This IS a tuple, because of the trailing comma
print(tup)
print(type(tup))

tup = (1)                # This is just an int, NOT a tuple (no comma)
print(tup)
print(type(tup))

tup = ("Hello")           # This is just a string, NOT a tuple (no comma)
print(tup)
print(type(tup))

# ===================================================
# Slicing in tuples (same rules as lists/strings)
# ===================================================
tup = (4, 5, 1, 3, 8)
print(tup[1:3])
print(tup[0:])

# ===================================================
# Tuple Methods
# ===================================================

# 1. index() -> returns the index of the FIRST occurrence of a value
tup = (4, 5, 1, 3, 8)
print(tup.index(3))
print(tup.index(5))

# 2. count() -> returns how many times a value appears in the tuple
tup = (4, 5, 1, 3, 4, 8, 7, 4, 9, 8)
print(tup.count(4))
print(tup.count(8))

# ===================================================
# Practice Programs for Lists and Tuples
# ===================================================

# 1. Take 3 movie names from the user and store them in a list
mov1 = input("Enter the first movie: ")
mov2 = input("Enter the second movie: ")
mov3 = input("Enter the third movie: ")
movies = []
movies.append(mov1)
movies.append(mov2)
movies.append(mov3)
print(movies)

# 2. Check whether a list is a palindrome
# Palindrome = reads the same forward and backward
# e.g. "ma'am", "racecar", [1, 2, 3, 2, 1]

list_1 = [1, 2, 3, 2, 1]
list_2 = [1, 2, 3]

copy_list_1 = list_1.copy()
copy_list_1.reverse()
if copy_list_1 == list_1:
    print("Palindrome")
else:
    print("Not a Palindrome")

copy_list_2 = list_2.copy()
copy_list_2.reverse()
if copy_list_2 == list_2:
    print("Palindrome")
else:
    print("Not a Palindrome")
