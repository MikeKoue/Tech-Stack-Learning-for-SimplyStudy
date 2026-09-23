import random
# for loops 
fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + "Pie")

print(fruits)

student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
total_exam_score = sum(student_scores)
print(total_exam_score)

sum = 0
for score in student_scores:
    sum += score

print(sum)

max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score
      
print(max_score)

#Range function wiht For loop

for number in range(1, 11):
    print(number)

total = 0
for number in range(1, 101):
    total += number
print(total)

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbos would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

choice_list = []
randlen_Letters = nr_letters
randlen_Symbols = nr_symbols
randlen_Numbers = nr_numbers

for i in range(randlen_Letters):
    choice_list.append(random.choice(letters))
for i in range(randlen_Symbols):
    choice_list.append(random.choice(symbols))
for i in range(randlen_Numbers):
    choice_list.append(random.choice(numbers))


random.shuffle(choice_list)
output = ""

for code in choice_list:
    output += code

print(output)
   