# ===================================================
# Nesting in Python (writing an if statement inside another if statement)
# ===================================================
age = 88
if age >= 18:
    if age >= 80:
        print("You cannot drive")
    else:
        print("You can drive")
else:
    print("You are not eligible for vote")

# ===================================================
# if / elif / else chain
# ===================================================
Light = "Blue"
if Light == "red":
    print("stop")
elif Light == "green":
    print("go")
elif Light == "yellow":
    print("wait")
else:
    print("Light is broken")
print("end of code")

# ===================================================
# Multiple separate if statements
# (NOTE: these are independent checks, not elif —
#  both conditions are checked even if the first is True)
# ===================================================
num = 5
if num > 3:
    print("number is greater than 3")
if num > 5:
    print("number is greater than 5")

# ===================================================
# Grading system using elif chain
# ===================================================
marks = int(input("Enter your marks: "))
if marks >= 90:
    grade = "A"
elif marks >= 80:              # marks < 90 already guaranteed by elif order
    grade = "B"
elif marks >= 70:
    grade = "C"
elif marks >= 60:
    grade = "D"
else:
    grade = "F"
print("Your grade is ->", grade)

# ===================================================
# Practice Programs
# ===================================================

# 1. Check if a number is even or odd
num = int(input("Enter the number please: "))
if num % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")

# 2. Find the greatest of three numbers
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))
if a > b and a > c:
    print("First number is greatest ->", a)
elif b > a and b > c:
    print("Second number is greatest ->", b)
elif c > a and c > b:
    print("Third number is greatest ->", c)
else:
    print("All three numbers you entered are the same")

# 3. Check if a number is a multiple of 7
num = int(input("Enter number: "))
if num % 7 == 0:
    print("Number is a multiple of 7")
else:
    print("Number you entered is not a multiple of 7")

# 4. Simple calculator (+, -, *, /)
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter the operator (+, -, *, /): ")
if operator == "+":
    print("Result =", num1 + num2)
elif operator == "-":
    print("Result =", num1 - num2)
elif operator == "*":
    print("Result =", num1 * num2)
elif operator == "/":
    if num2 != 0:
        print("Result =", num1 / num2)
    else:
        print("Cannot divide by zero.")
