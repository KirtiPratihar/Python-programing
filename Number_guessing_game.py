#random Number Generator
import random
print("WELCOME TO THE NUMBER GUESSING GAME")
n =random.randrange(1,100)
attempts=0

while True:
    try:
        k=int(input("YOU HAVE TO CHOOSE A NUMBER BETWEEN 1 TO 100-"))
        attempts=attempts+1
        if (k>100 or k<0):
            print("NOT VALID")
        elif k<n:
            print("YOU CHOOSED A SMALLER NUMBER")
        elif k>n:
            print("YOU HAVE CHOOSE A LARGER NUMBER")
        else:
            print(f"YOU HAVE SUCESSFULLY GUESSED THE CORRECT NUMBER WITH {attempts} ATTEMPTS".format(attempts))
            break
    except ValueError:
        print("Please enter a valid Number")
