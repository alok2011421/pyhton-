import random
print("Welcome to the Guess the Number")
num = random.randint(1,100)
def easy():
    no=0
    count =0
    while(count<11 and no!=num):
        no=int(input("Enter the number"))
        if no>num:
            print("Too High")
        elif no==num:
            print("You Guessed it correct")
        else:
            print("Too Low")
        count+=1
    if no==num:
        print("Hurray! You won the game")
    else:
        print("Sorry! You lose the game!")
        
def hard():
    no=0
    count =0
    while(count<6 and no!=num):
        if no>num:
            print("Too High")
        elif no==num:
            print("You Guessed it correct")
        else:
            print("Too Low")
        count+=1
    if no==num:
        print("Hurray! You won the game")
    else:
        print("Sorry! You lose the game!")
a=input("Which level you want to play 'Easy' or 'Hard'?").lower()
if a=="easy":
    easy()
elif a=="hard":
    hard()
else:
    print("Wrong choice")