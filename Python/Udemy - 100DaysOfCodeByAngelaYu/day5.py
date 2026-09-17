import random

fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + " Pie")
print(fruits)
# indentation is important

student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89]

total_exam_score = sum(student_scores)
print(total_exam_score)

sum = 0
for score in student_scores:
    sum += score

print(sum )
max = 0
for score in student_scores:
    if score > max:
        max = score

print(max)
  
for number in range(1, 11, 3):  
    print(number)
sum = 0

for number in range(1, 101):
    sum += number
print(sum)

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', "5", '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
HalfPassword = []
Password = []



print("welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

for num in range(1, nr_letters + 1):
    HalfPassword.append(random.choice(letters))

for num in range(1, nr_symbols + 1):
    HalfPassword.append(random.choice(symbols))

for num in range(1, nr_numbers + 1):
    HalfPassword.append(random.choice(numbers))

random.shuffle(HalfPassword)
for i in HalfPassword:
    Password.append(i)

Truth = ""

for i in Password:
    Truth += i

print(f"Your new password is {Truth}!")

