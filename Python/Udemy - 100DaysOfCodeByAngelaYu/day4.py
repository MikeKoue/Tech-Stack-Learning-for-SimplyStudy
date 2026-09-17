import random 

# random_integer = random.randint(1, 10)
# print(random_integer)

# random_number_0_to_1 = random.random() * 10
# print(random_number_0_to_1)

# random_float = random.uniform(1, 10)
# print(random_float)

# HorT = random.randint(1,2)
# if HorT == 1:
#     print("heads")
# else:
#     print("tails")

# states_of_america = ["Texas", "Florida", "Virginia", "North Carolina", "Nevada"] 
# print(states_of_america[0])
# states_of_america[3] = "South Carolina"
# print(states_of_america)
# states_of_america.append("North Carolina")
# print(states_of_america)
# states_of_america.extend(["Delaware", "Illinois"])
# print(states_of_america)

# friends = ["Michael", "Julio", "Lucas", "Tetegan", "Malik", "Francis", "Leo"]
# pick = random.randint(0,len(friends) - 1)

# print(friends[pick])

# print(random.choice(friends))



# Rock
rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

# Paper
paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

# Scissors
scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

choice  = int(input("Welcome to my rock, papaer, scissors game. Pick 0 for rock, 1 for paper, and 2 for scissors! "))

computer = random.randint(0,2)

if choice == 0:
    print(rock)
elif choice == 1:
    print(paper)
elif choice == 2:
    print(scissors)

compChoice = [rock, paper, scissors]

print(f"""
      Computer chose:

    {compChoice[computer]}
      """)

if computer == choice:
    print("You tied")
elif computer == 0 and choice == 2:
    print("You lose")
elif computer == 1 and choice == 0:
    print("You lose")
elif computer == 2 and choice == 1:
    print("You lose")
else:
    print("You win")