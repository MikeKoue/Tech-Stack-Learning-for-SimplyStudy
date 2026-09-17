# Subscripting
print("Hello"[4])

print("Hello"[-1])

# String

print("123" + "345") # concantanation 

# Integer = whole number

print(123 + 345)

# Large Integers

print(123_456_789)

print(123456789)

# Float = floating point number

print(3.14159)

# Boolean
print(True)
print(False) 

# Len() only works with things that are sized such as Lists and strings

# Type() 
print(type("Hello"))
print(type(123))
print(type(3.14))
print(type(True))

# Type casting/ Type conversion 

print(int("123") + int("456"))

# Value errors occur from trying to convert type of something not logical. Example: cant convert abc into an integer

int()
float()
str()
bool()

print("Number of letters in your name: " + str(len(input("What is your name? "))))

name_of_the_user = input("Enter your name ")
length_of_name = len(name_of_the_user)

print(type("Number of letters in your name: ")) # str
print(type(length_of_name)) # int

# Mathematical Operations

print("My age: " + str(12))
print(123 + 456)
print(7 - 3) 
print(3 * 2)
print(6 / 3)
# for division to result in an integer instead of float, use //
# be careful because the double slash does not round, it just removes anything after the decimal point
print(6//3)
print(2**2) # exponental, so this is equivalent to 2^2 = 4

# Python uses PEMDAS method too

bmi = 84 / 1.65 ** 2

print(bmi)

print(int(bmi))

print(round(bmi))

print(round(bmi, 3))

score = 0 

# User scores a point

score += 1
print(score)

# f-strings

score = 0
height = 1.8
is_winning = True

print(f"Your score is = {score}, your height is {height}, and you are winning is {is_winning}")


# Day 2 project
print("Welcome to tip calculator!")
bill = float(input("What is the total bill? $")) 
tip = 1 + round((float(input("How much tip would you like? ")) / 100), 2)
split = int(input("How many people are splitting the bill? "))
# Calculated final bill for everyone
Total = round(((bill * tip)/ split), 2)
print(f"Each person should pay: ${Total}" )