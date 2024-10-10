import random

secret_number = random.randint(1, 10)
number = int(input("Guess the number between 1 and 10")) 
if number > secret_number:
    print("Too high")   
elif number < secret_number:
    print("Too low")        
else:
    print("Correct")                  
