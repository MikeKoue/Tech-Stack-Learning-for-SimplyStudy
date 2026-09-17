# Subscripting
print("Hello"[0])
print("Hello"[-1])

# String
print("123" + "456") # concantination

#Integer = Whole numbers
print(123 + 456)
print(123_456_789)

# Float = Floating Point Number 
print(3.14159)

# Boolean
print(True)
print(False)

# Checking error & Type
len("Hello") # functions take a certain type of data

print(type(123))
print(type(3.14))
print(type(True))
print(type("Hello"))

# type casting/conversion
int("123")
print(int("123") + int("456"))

print("Number of letters in your name: " + str(len(input("Enter your name "))))

# Mathematical operators
print(123 + 456) # addition
print(7 - 3) # subtraction
print(3 * 2) # multiplication
print(6 / 3) # division (implicit type casting into float)
print(6 // 3) # removes numbers after decimal point
print ( 2 ** 2) # exponent

# PEMDAS (order of operations)

# Flooring, rounding, choosing digit place to cut off

bmi = 84 / 1.65 ** 2
print(bmi)

print(int(bmi))

print(round(bmi, 2))

#Number manipulation

score = 0
score += 1
print(score)

# f - strings
score = 0
height = 1.67
is_winning = True
print(f"Your score is {score}, your height is {height}. You are winning is {is_winning}" )

bill = float(input("Welcome to the tip calculator!\n What was the total bill? $"))
tip = float(input("How much tip would you like to give? 10, 12, or 15? "))
split = float(input("How many people to split the bill? "))
percentage = float(1 + (tip / 100))
final = round(((bill * percentage) / split), 2)
print(f"Each person should pay: ${final}")