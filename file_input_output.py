# ===================================================
# File Input / Output in Python
# ===================================================
# NOTE: I reordered "writing" before "reading" below (compared to how you
# originally wrote it) so this script can run top-to-bottom without errors.
# Originally "reading" came first, but that only works if practice.py
# already exists beforehand — writing it first guarantees it does.

# ---------------------------------------------------
# Writing to a file
# ---------------------------------------------------
f = open("practice.py", "w")     # "w" REPLACES the whole content of the file
f.write("My name is M usman. \nI am a Software engineer")
f.close()

f = open("practice.py", "a")     # "a" APPENDS to the existing content instead
f.write("\nCurrently I am in 7th semester of SE")
f.close()

# ---------------------------------------------------
# Reading a file
# ---------------------------------------------------
f = open("practice.py", "r")
data = f.read()
print(data)
print(type(data))
f.close()

# We can also read line by line
f = open("practice.py", "r")
line1 = f.readline()
line2 = f.readline()
print(line1)
print(line2)
f.close()

# ===================================================
# Practice Programs
# ===================================================

# 1. Create a file and add lines to it
# Using "with" automatically closes the file for us, so we don't need f.close()
with open("practice.txt", "w") as f:
    f.write("Hi everyone \nWe are learning File I/O\n")
    f.write("using Java.\nI like programming in Java.")

# 2. Replace the word "Java" with "Python"
with open("practice.txt", "r") as f:
    data = f.read()

new_data = data.replace("Java", "Python")
print(new_data)

with open("practice.txt", "w") as f:
    f.write(new_data)

# 3. Search whether a word exists in the file
def check_for_word():
    word = "learning"
    with open("practice.txt", "r") as f:
        data = f.read()
        if word in data:
            print("Found")
        else:
            print("Not Found")

check_for_word()

# 4. Find the FIRST line number where a word exists
def check_for_line():
    word = "learning"
    line = True
    line_no = 1
    with open("practice.txt", "r") as f:
        while line:
            line = f.readline()
            if word in line:
                print(line_no)
                return line_no
            line_no += 1
    return -1

check_for_line()

# 5. From a file of numbers separated by commas, count how many are even
# (Added this small setup step just so the file has comma-separated numbers
# in it for this demo — otherwise it would still contain the sentence
# from the practice programs above, which can't be split into numbers.)
with open("practice.txt", "w") as f:
    f.write("4,7,10,3,8,15,22,9,6")

count = 0
with open("practice.txt", "r") as f:
    data = f.read()

nums = data.split(",")
for val in nums:
    if int(val) % 2 == 0:
        count += 1
print(count)
