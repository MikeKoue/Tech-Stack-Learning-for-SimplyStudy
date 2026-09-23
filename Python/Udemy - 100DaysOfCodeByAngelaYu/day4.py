import random
# random


random_integer = random.randint(1,10)
print(random_integer)


random_number = random.random() 


random_float = random.uniform(1,10)
print(random_float)

random_heads_or_tails = random.randint(0,1)
if random_heads_or_tails == 0:
    print("'Heads")
else:
    print("Tails")

#lists are data scructures 

states_of_america = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut"]
print(states_of_america[0])
print(states_of_america[-4])
print(states_of_america)
states_of_america.append("Delaware")
states_of_america.extend("Florida")

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
random_name = random.randint(0,4)
print(random_name)
# option 1
who_pays = friends[random_name]
print(who_pays)
# option 2
print(random.choice(friends))

# dirty_dozen = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
dirty_dozen = fruits, vegetables

paper = """



            d88b               __     __
           /78889            d7 7b  d7 7b
          d88889           d8`8b  d8`-8b _
         d888889         d8888b d8888b d7 7b
        d888888        d88888b d8888b d888b
       d8888884_____d888888b d888b  d888b
      d88888888888888888888,d888b  d888b _
     d888888888888888888888888b  d888b d7_b
   d8 88888888888888888888888,d8888b d888b
 d888 888888888888888888888888888b d8888b
   888 8888888888888888888888888b d888b
  88888888888888888888888888888,8888b
  8888888888 8888888888888888888888b
 888888888888 88888888888888888p8"
88888888888888`pj998ppppp88888"
8888888hjw888b
 88888888888b




"""

rock = """



                        _    ,-,    _
                 ,--, /: :\/': :`\/: :\
                |`;  ' `,'   `.;    `: |
                |    |     |  '  |     |.
                | :  |     | pb  |     ||
                | :. |  :  |  :  |  :  | \
                 \__/: :.. : :.. | :.. |  )
                      `---',\___/,\___/ /'
                           `==._ .. . /'
                                `-::-'


"""

scissors = """



     ."".    ."",
     |  |   /  /
     |  |  /  /
     |  | /  /
     |  |/  ;-._
     }  ` _/  / ;
     |  /` ) /  /
     | /  /_/\_/\
     |/  /      |
     (  ' \ '-  |
      \    `.  /
       |      |



"""

print(rock)
print(paper)
print(scissors)

choice = ["rock", "paper", "scissors"]


human = input("Welcome to my rock, paper, scissors game! Type rock, paper, or scissors to play! ")
human = human.lower()
ai = random.choice(choice)
if human == "rock" and ai == "scissors":
    print("You chose rock")
    print(rock)
    print("Ai chose scissors")
    print(scissors)
    print("You won the game")
elif human == "scissors" and ai == "paper":
    print("You chose scissors")
    print(scissors)
    print("Ai chose paper")
    print(paper)
    print("You won the game")
elif human == "paper" and ai == "rock":
    print("You chose paper")
    print(paper)
    print("Ai chose rock")
    print(rock)
    print("You won the game")
elif human == ai:
    print("you guys tied")
else:
    print("You lost!")

