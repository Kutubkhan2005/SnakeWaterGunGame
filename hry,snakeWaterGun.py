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
    print("It is a tie")
    no_chance=no_chance+1
    co_point=co_point+1
    your_point=your_point+1

   #if human enters "s"
   elif human=="s" and computer=="w":
     print("Congratulations, you won")
     print("com chose water")
     your_point=your_point+1
     no_chance=no_chance+1
   elif human=="s" and computer=="g":
     print("Ohh!! You lose, better luck next time")
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
     print("Ohh!! You lose, better luck next time")
     print("com chose snake")
     co_point=co_point+1
     no_chance=no_chance+1

     #if humanenters "g"
   elif human=="g" and computer=="s":
     print("Congratulations, you won")
     print("com chose snake")
     your_point=your_point+1
     no_chance=no_chance+1
   elif human=="g" and computer=="w":
     print("Ohh!! You lose, better luck next time")
     print("com chose water")
     co_point=co_point+1
     no_chance=no_chance+1

   #if user inputs invalid input he losed
   else:
       print("You entered the wrong letter, thus breaking the discipline of the game so you lose")
       your_point=your_point*0
       break
    

print("\n \n")

if your_point==0:
    print("you are undisciplined,but you lost the game")

if your_point>co_point:
 print("you won the match")
 
elif your_point<co_point:
 print("you lose the match")
    
elif your_point==co_point:
 print("match tied")

   

