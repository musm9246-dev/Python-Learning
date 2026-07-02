# ===================================================
# Lists in Python
# ===================================================
# We can store multiple types of data in a single list.

marks = [93.5, 78, 65, 59, 86.5]
print(marks)
print(len(marks))

# Accessing marks at specific indexes
print(type(marks))
print(marks[0])
print(marks[3])

# ===================================================
# Lists are mutable, while strings are immutable
# ===================================================
# text = "hello world"
# print(text[0])
# text[0] = "y"   -> This gives an error, we cannot change characters in a string

student = ["usman", 99.0, 21, "lahore"]
print(type(student))
print(student)
print(student[0])
student[0] = "Ali"     # Lists allow changing values (mutable)
print(student)

# ===================================================
# Slicing in lists (same rules as string slicing)
# ===================================================
marks = [93.5, 78, 65, 59, 86.5]
print(marks[0:4])

# ===================================================
# List Methods
# ===================================================

# 1. list.append() -> adds an element at the end of the list
a = [1, 2, 7, 8]
a.append(5)          # append() modifies the list in place and returns None
print(a)

# 2. list.sort() -> sorts the list

# Ascending order
a = [3, 2, 9, 7, 5]
a.sort()
print(a)

# Descending order
a = [3, 2, 9, 7, 5]
a.sort(reverse=True)
print(a)

# 3. list.reverse() -> completely reverses the order of elements
a = [3, 2, 9, 7, 5]
a.reverse()
print(a)

# 4. list.insert(index, value) -> adds a value at a specific index
a = [3, 2, 9, 7, 5]
a.insert(3, 6)
print(a)

# 5. list.remove(value) -> removes the FIRST occurrence of the given value
a = [3, 2, 9, 7, 5, 2]
a.remove(2)
print(a)

# 6. list.pop(index) -> removes and returns the element at the given index
a = [3, 2, 9, 7, 5, 2]
print(a.pop(3))
print(a)

# NOTE: append(), sort(), reverse(), and insert() all modify the list
# IN PLACE and return None. That's why printing their return value
# directly (e.g. print(a.append(5))) shows "None" instead of the list.
# remove() and pop() also modify in place, but pop() additionally
# RETURNS the removed value, which is why print(a.pop(3)) shows a number.
