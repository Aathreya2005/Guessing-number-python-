from importlib.util import module_for_loader
from random import *
num = (int)(random()*8+1)
i = 0
guess = int(input("Enter your guess "))

while i<2:

    if(guess == num):
        print("Congrats! You won")
        break
    else:
        guess = int(input("Wrong! Re-enter your guess "))
        if(guess == num):
            print("Congrats! You won")
            break
        else:
            i+=1
        
if(i==2):
    print("You lose!Number is",num)
    