# ===================================================
# Loops in Python
# ===================================================

# ---------------------------------------------------
# While Loop
# ---------------------------------------------------
# Variables set up BEFORE the loop are called "iterators"
# The repeated process inside the loop is called "iteration"

count = 1
while count <= 5:
    print("usman baloch")
    count += 1
print(count)

i = 1
while i <= 10:
    print("usman baloch", i)
    i += 1

i = 10
while i >= 1:
    print(i)
    i -= 1
print("loop ended")

# ---------------------------------------------------
# Practice Programs (while loop)
# ---------------------------------------------------

# 1. Print 1 to 100
i = 1
while i <= 100:
    print(i)
    i += 1
print("loop ended")

# 2. Print 100 to 1
i = 100
while i >= 1:
    print(i)
    i -= 1
print("loop ended")

# 3. Print multiplication table of n
n = int(input("Enter the number: "))
i = 1
while i <= 10:
    print(n * i)
    i += 1
print("loop ended")

# 4. Print the elements of a list using a loop
num = [1, 4, 6, 16, 20, 35, 87, 29, 85, 100]
idx = 0
while idx <= len(num) - 1:
    print(num[idx])
    idx += 1
print("loop ended")

# 5. Print the names of heroes from a list
heroes = ["Captain", "ironman", "spiderman", "thor", "superman", "usman"]
i = 0
while i < len(heroes):
    print(heroes[i])          # traversing the list using an index
    i += 1
print("loop ended")

# 6. Search for a number x inside a tuple
num = (1, 4, 6, 16, 20, 35, 87, 29, 85, 100)
x = 85
i = 0
while i < len(num):
    if num[i] == x:
        print("found at idx", i)
    else:
        print("finding.....")
    i += 1
print("loop ended")

# ---------------------------------------------------
# break and continue in loops
# ---------------------------------------------------

# break -> stops the loop completely
i = 0
while i < 10:
    print(i)
    if i == 5:
        break
    i += 1
print("loop ended")

# continue -> skips the rest of the CURRENT iteration only
i = 0
while i <= 10:
    if i == 7:
        i += 1
        continue
    print(i)
    i += 1
print("loop ended")

# Print odd numbers from 1 to 30 using continue
i = 1
while i <= 30:
    if i % 2 == 0:
        i += 1
        continue
    print(i)
    i += 1
print("loop ended")

# ===================================================
# For Loop
# ===================================================

nums = [2, 3, 1, 6, 4, 3, 8]
for val in nums:
    print(val)

fruits = ["Apple", "Mango", "Orange", "Watermelon", "Banana", "Grapes", "Apricot"]
for val in fruits:
    print(val)

tup = (9, 7, 1, 6, 3, 5, 8)
for num in tup:
    print(num)

# for-else: the "else" runs once the loop finishes normally (no break)
str_1 = "Usman"
for ch in str_1:
    print(ch)
else:
    print("end")

# Searching for a specific character in a string
str_1 = "Usman"
for ch in str_1:
    if ch == "a":
        print("a found")
        break
    print(ch)
print("end")

# ---------------------------------------------------
# Practice Programs (for loop)
# ---------------------------------------------------

# 1. Print the elements of a list
list_1 = [7, 5, 1, 8, 6, 9, 3, 0, 4]
for nums in list_1:
    print(nums)

# 2. Search for a number in a tuple (method 1: using break)
tup_1 = (7, 5, 1, 8, 6, 9, 3, 0, 4)
for num in tup_1:
    if num == 8:
        break
print(num)     # NOTE: this only shows the value where the loop stopped
               # (or the last value checked, if it was never found)

# 3. Search for a number in a tuple (method 2: reporting the index)
tup_1 = (7, 5, 1, 8, 6, 9, 3, 0, 4)
x = 0
idx = 0
for num in tup_1:
    if num == x:
        print("num found at idx", idx)
    idx += 1

# ===================================================
# range() function
# ===================================================

seq = range(10)
for i in seq:
    print(i)

# or, more commonly written directly inside the for loop:
for i in range(10):        # only a stop value given
    print(i)

# range can take start (optional), stop (required), and step (optional)
for i in range(3, 10):          # start and stop given
    print(i)

for i in range(2, 12, 2):        # start, stop, and step all given
    print(i)

# Print even numbers from 1 to 20 using range
for i in range(2, 21, 2):
    print(i)

# Print odd numbers from 1 to 20 using range
for i in range(1, 21, 2):
    print(i)

# ---------------------------------------------------
# Practice Programs (for loop + range)
# ---------------------------------------------------

# 1. Print 1 to 100
for i in range(1, 101):
    print(i)

# 2. Print 100 to 1
for i in range(100, 0, -1):
    print(i)

# 3. Print the multiplication table of n
n = int(input("Enter the number: "))
for i in range(1, 11):
    print(i * n)

# ===================================================
# pass statement
# ===================================================
# "pass" is a null statement — it does nothing, just a placeholder
# so the code doesn't error out on an empty block.

for i in range(5):
    pass

if i > 5:
    pass

print("some useful work")

# ===================================================
# More Practice Programs
# ===================================================

# 1. Sum of first n natural numbers (using for loop)
n = 5
total_sum = 0             # renamed from "sum" since sum() is a Python built-in
for i in range(1, n + 1):
    total_sum += i         # NOTE: original had "total_sum += 1" which is a bug,
                           # it should add "i" on each step, not a fixed 1
print("total sum =", total_sum)

# Sum of first n natural numbers (using while loop)
n = 5
total_sum = 0
i = 1
while i <= n:
    total_sum += i
    i += 1
print("total sum =", total_sum)

# 2. Factorial of first n natural numbers (using while loop)
n = 5
fact = 1
i = 1
while i <= n:
    fact *= i
    i += 1
print("the fact =", fact)

# Factorial of first n natural numbers (using for loop)
n = 5
fact = 1
for i in range(1, n + 1):
    fact *= i
print("the factorial =", fact)
