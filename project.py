import time 
#This allows for pauses in between code execution
import random
#This allows for random number generation
name = input("Hello user, State your name ")
time.sleep(1.5)
print("Nice to meet you", name)
time.sleep(1.5)
number = random.randint(1,5)
print(" I have a number between 1 and 5, can you guess it? ")
guess = int(input("Enter your guess: "))
if guess == number:
    print("Congratulations! You guessed it right.")
else:
    print("Sorry, the correct number was", number)