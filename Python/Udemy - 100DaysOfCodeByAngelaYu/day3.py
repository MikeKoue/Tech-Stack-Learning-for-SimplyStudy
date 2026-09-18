print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age >= 18:
        bill = 12
        print("Price is $12.")
    elif age < 12:
        bill = 5
        print("Price is $5.")
    elif 45 <= age <= 55:
        bill = 0
        print("Everything is going to be ok. Have a free ride on us!")
    else:
        bill = 7
        print("Price is $7")

    wants_photo = input("Do you want to have a photo take? Type y for Yes and n for No.")
    if wants_photo == "y":
        bill += 3
    else:
        bill += 0
    print(f"Your final bill is ${bill}.")
else:
    print("sorry you have to grow taller before you can ride.")

# Modulo Operator 
Number = int(input("Enter a number to know if it is even or odd. "))
if Number % 2 != 0:
    print("Your number is odd")
else:
    print("Your number is even")

# pizz order practice
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("You typed the wrong input.")
if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}.")

# logical operators 

# day 3 project: Choose your own adventure




print("Welcome to Treasure Island. Your mission is to find the treasure")
answer = (input("You come across to paths. One is on the left and the other on the right. Type left or right to choose where to go. "))
answer.lower()
if answer == "left":
    answer = input("You continue on the path through a an abondoned castle and come across a lake on the other side. You have the choice to either wait or continue. Type wait or continue to proceed.  ") 
    answer.lower()
    if answer == "wait":
        answer = input("You answered a riddle to a magical fairy and a bridge appeared for you to cross the lake. You come across a set of three portals with the colors red, yellow, and blue. Type one of the colors to choose which portal to enter. ")
        answer.lower()
        if answer == "yellow":
           print("Yeah you found the treasure of an old wise king. Congrats!")
        else:
            print("You came into an empty dimension filled with darkness. You forever rot in body and minde. How unfortunate.")
    else:
        print("The lake had a vicious undercurrent that dragged you into the mouth of a gigantic clam. How unfortunate.")
    

else:
  print("You stumbled across a dragon and became barbecue. How unfortunate.")
