"""
    import random
    lst = ['s','w','g']

    chance = 10
    no_of_chance = 0
    computer_point = 0
    human_point = 0

    print(" \t \t \t \t Snake,Water,Gun Game\n \n")
    print("s for snake \nw for water \ng for gun \n")

    # making the game in while
    while no_of_chance < chance:
        _input = input('Snake,Water,Gun:')
        _random = random.choice(lst)

        if _input == _random:
            print("Tie Both 0 point to each \n ")

        # if user enter s
        if _input == "s" and _random == "g":
            computer_point = computer_point + 1
            print(f"your guess {_input} and computer guess is {_random} \n")
            print("computer wins 1 point \n")
            print(f"computer_point is {computer_point} and your point is {human_point} \n ")

        elif _input == "s" and _random == "w":
            human_point = human_point + 1
            print(f"your guess {_input} and computer guess is {_random} \n")
            print("Human wins 1 point \n")
            print(f"computer_point is {computer_point} and your point is {human_point} \n")

        # if user enter w
        elif _input == "w" and _random == "s":
            computer_point = computer_point + 1
            print(f"your guess {_input} and computer guess is {_random} \n")
            print("computer wins 1 point \n")
            print(f"computer_point is {computer_point} and your point is {human_point} \n ")

        elif _input == "w" and _random == "g":
            human_point = human_point + 1
            print(f"your guess {_input} and computer guess is {_random} \n")
            print("Human wins 1 point \n")
            print(f"computer_point is {computer_point} and your point is {human_point} \n")

        # if user enter g

        elif _input == "g" and _random == "s":
            human_point = human_point + 1
            print(f"your guess {_input} and computer guess is {_random} \n")
            print("Human wins 1 point \n")
            print(f"computer_point is {computer_point} and your point is {human_point} \n")


        elif _input == "g" and _random == "w":
            computer_point = computer_point + 1
            print(f"your guess {_input} and computer guess is {_random} \n")
            print("computer wins 1 point \n")
            print(f"computer_point is {computer_point} and your point is {human_point} \n ")

        else:
            print("you have input wrong \n")

        no_of_chance = no_of_chance + 1
        print(f"{chance - no_of_chance} is left out of {chance} \n")

    print("Game over")

    if computer_point > human_point:
        print("Computer wins and you loose")

    if computer_point < human_point:
        print("you win and computer loose")

    print(f"your point is {human_point} and computer point is {computer_point}")
"""
import random
ref=['s','w','g']

chance=7
no_chance=0
co_point=1
your_point=1

print("snake water gun game \n s for snake \n w for water \n g for gun \n if you enter different choice you loss")

while no_chance<chance:
   human=input("\n")
   computer=random.choice(ref)

   if human==computer:
    print("tie")
    no_chance=no_chance+1
    co_point=co_point+1
    your_point=your_point+1

   #if human enters "s"
   elif human=="s" and computer=="w":
     print("won, keep it up")
     print("com chose water")
     your_point=your_point+1
     no_chance=no_chance+1
   elif human=="s" and computer=="g":
     print("lose, better luck next time")
     print("com chose gun")
     co_point=co_point+1
     no_chance=no_chance+1
     
   #if humanenters "w"
   elif human=="w" and computer=="g":
     print("won, keep it up")
     print("com chose gun")
     your_point=your_point+1
     no_chance=no_chance+1
   elif human=="w" and computer=="s":
     print("lose, better luck next time")
     print("com chose snake")
     co_point=co_point+1
     no_chance=no_chance+1

     #if humanenters "g"
   elif human=="g" and computer=="s":
     print("won, keep it up")
     print("com chose snake")
     your_point=your_point+1
     no_chance=no_chance+1
   elif human=="g" and computer=="w":
     print("lose, better luck next time")
     print("com chose water")
     co_point=co_point+1
     no_chance=no_chance+1

   #if user inputs invalid input he losed
   else:
       print("you entered wrong, and broke the disipline so you losed")
       your_point=your_point*0
       break
    

print("\n \n")

if your_point==0:
    print("you are undisiplined and loser")

if your_point>co_point:
 print("you won the match")
 
elif your_point<co_point:
 print("you lose the match")
    
elif your_point==co_point:
 print("match tied")

"""
     
   
   

