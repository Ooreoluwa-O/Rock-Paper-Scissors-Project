import random
end_game = False

while not end_game:
 player = input("R, P, or S,?:").lower()

 possible_options = ["R", "P", "S"]
 cpu = random.choice(possible_options)

 print("player:", player)
 print("cpu:", cpu)  

 if player == cpu:
   print("tie!")      
 elif player == "R" and cpu == "S":
   print("you won! cpu lost") 
 else:
    print("you lost! cpu won")

 if player == "P" and cpu == "R": 
    print("you won! cpu lost")
 elif player == "S" and cpu == "P":
    print("you won! cpu lost")
 else:
    print("you lost! cpu won")
 if player not in possible_options and cpu == "R":
    print("error")
 elif player not in possible_options and cpu == "S":
    print("error")
 elif player not in possible_options and cpu == "P":
    print("error")
 else: 
    print("continue this game") 