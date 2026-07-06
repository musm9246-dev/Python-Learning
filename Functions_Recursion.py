# ===================================================
# Functions in Python
# ===================================================

# Without a function, we'd have to repeat this logic every time:
a = 6
b = 8
result = a + b          # renamed from "sum" -> sum() is a Python built-in
print(result)
# If our code gets too complex and we need to do this again and again,
# repeating it like this becomes messy.

a = 9
b = 4
result = a + b
print(result)

# So instead, we wrap the repeated logic into a function:
def cal_sum(a, b):
    result = a + b
    print(result)
    return result

cal_sum(5, 9)             # calling the function gives us the result directly
cal_sum(9008, 87456)
cal_sum(12, 45)

# ---------------------------------------------------
# Now the simpler version
# ---------------------------------------------------
def calculate_sum(a, b):   # this whole block is called "defining" a function
    return a + b            # a, b here are called "parameters"

result = calculate_sum(23, 23)   # 23, 23 here are called "arguments"
print(result)

# ---------------------------------------------------
# Even simpler — a function with no parameters
# ---------------------------------------------------
def print_hello():
    print("hello")

print_hello()          # we can call this as many times as we want
print_hello()
print_hello()

# ---------------------------------------------------
# Calculating the average of 3 numbers
# ---------------------------------------------------
def average(a, b, c):
    total = a + b + c
    avg = total / 3
    print(avg)
    return avg

average(1, 2, 3)

# ---------------------------------------------------
# Built-in functions
# ---------------------------------------------------
print("usman")     # this itself is a built-in function, same as len(), type(), input(), etc.

# ---------------------------------------------------
# User-defined functions with default parameters
# ---------------------------------------------------
def calc_product(a=1, b=1):     # a=1, b=1 are DEFAULT values, used when no argument is passed
    print(a * b)
    return a * b

calc_product()          # uses the defaults (1, 1)

# ===================================================
# Practice Programs (functions)
# ===================================================

# 1. Print the length of a list (list passed in as a parameter)
goats = ["Cristiano", "Ronaldo", "BabarAzam", "ViratKohli", "WasimAkram", "LionelMessi"]
legends = ["NeymarJunior", "SergioRamos", "Pepe", "Afridi", "Sharma", "Sachin"]

def print_len(items):        # renamed param from "list" -> list is a Python built-in type
    print(len(items))
    return len(items)

print_len(goats)
print_len(legends)

# 2. Print all elements of a list in a single line
nums = [9, 8, 3, 7, 5, 6, 2, 4, 1]

def print_list(items):
    for item in items:
        print(item, end=" ")
    print()   # move to a new line after the loop finishes

print_list(nums)

# 3. Find the factorial of n
# First, with a plain loop:
n = int(input("Enter the number: "))
fact = 1
for i in range(1, n + 1):
    fact *= i
print(fact)

# Now, wrapped in a function:
def fact_n(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    print(fact)

fact_n(5)

# 4. Convert USD to Rs
def converter(usd_val):
    rs_val = usd_val * 288
    print(usd_val, "USD =", rs_val, "Rs")

converter(100)

# ===================================================
# Recursion in Python
# ===================================================
# A recursive function is a function that calls itself.

def show(n):
    print(n)

show("5")     # this only prints once — what if we need to print 5,4,3,2,1 in ONE call?

# Recursive version:
def show(n):
    if n == 0:          # base case -> stops the recursion
        return
    print(n)
    show(n - 1)          # the function calling itself, with a smaller value each time

show(5)

# Factorial of number n, using recursion
def fact(n):
    if n == 0 or n == 1:   # base case
        return 1
    return fact(n - 1) * n

print(fact(7))

# ===================================================
# Practice Programs (recursion)
# ===================================================

# 1. Sum of first n natural numbers, using recursion
def cal_sum(n):
    if n == 0:            # base case
        return 0
    return cal_sum(n - 1) + n

print(cal_sum(5))

# 2. Print all elements in a list, using recursion
def print_list(items, idx=0):
    if idx == len(items):     # base case -> stop once we've reached the end
        return
    print(items[idx])
    print_list(items, idx + 1)   # recursive call, moving to the next index

goats_list = ["CR7", "Cristiano", "Ronaldo", "Babar Azam", "Bobzy", "King Babar"]
print_list(goats_list)
