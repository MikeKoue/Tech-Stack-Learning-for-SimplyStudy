# Conditional/ if-else statements
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
else:
    print("Sorry you have to grow taller before you can ride")

# Comparision operators include >, <, >=, <=, ==, !=

# modulo takes the remainder of a division problem
print(10 % 3)

Answer = int(input("Enter an Integer! "))
if Answer % 2 == 0:
    print("The number you inputed is even!")
else:
    print("The number you inputed is odd!")


# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))

# if height >= 120:
#     age = int(input("How old are you? "))
#     if age >= 18:
#         print("You have to pay $12.")
#     elif age < 18 and age >= 12:
#         print("You have to pay $7.")
#     else:
#         print("You have to pay $5.")
# else:
#     print("Sorry you have to grow taller before you can ride")


print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    age = int(input("How old are you? "))
    if age >= 18:
        bill = 12
    elif 45 >= age <= 55:
        print("Everything ok? Have a free ride on us!")
    elif age < 18 and age >= 12:
        bill = 7
    else:
        bill = 5
    
    wants_photo = input("Do you want to have a photo taken? type y for Yes and n for No. ")
    if wants_photo == "y":
        bill += 3

    print(f"You final bill is ${bill}.")
else:
    print("Sorry you have to grow taller before you can ride")


print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you wnat? S ($15), M ($20) or L ($25): ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

if size == "S":
    bill = 15
elif size == "M":
    bill = 20
elif size == "L":
    bill = 25
if pepperoni == "Y":
    if size == "S":
        bill += 1
    else:
        bill += 3
if extra_cheese == "Y":
    bill += 1
print(f"Your final bill is ${bill}. Thank you and have a wonderful day\n")

print('''
                      __
                 / _,\
                 \_\
      ,,,,    _,_)  #      /)
     (= =)D__/    __/     //
    C/^__)/     _(    ___//
      \_,/  -.   '-._/,--'
_\\_,  /           -//.
 \_ \_/  -,._ _     ) )
   \/    /    )    / /
   \-__,/    (    ( (
              \.__,-)\_
               )\_ / -(
              / -(////
             ////  
      
      
      
      
      
      
      
      ''')

print("Welcome to treasure island!")

choice = input(print("You're at a cross road. Where do you want to go? R or L")).lower()
if choice == "r":
    print("Game over. You go hit by Truck-kun and isekaid")
else:
    print("You've come across a lake. There is an island in the middle of the lake.")

choice = input(print("Type wait to wait for a boat. Type swim to swim to swim across."))
if choice == "swim":
    print("Game over. You got swallowed by the Kraken")
else:
    print("You wait for the boat and get accross to the castle.")
choice = input(print("There are three doors, blue, yellow, and red. pick one"))
if choice != "yellow":
    print(" Game over. You opened the door and there was a green light that turned you into stone. Gotta wait for a Doctor named Senku")
else:
    print("You get the treasure")