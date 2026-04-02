import random
from game_data import data
from art import logo, vs
while True:
    print(logo)
    c=len(data)
    a=random.randint(0,c)
    print(data[a])
    print(vs)
    b=random.randint(0,c)
    print(data[b])
    c=int(input("Enter the choice"))
    count=0
    if a>b or c==a:
        print("Right choice")
        count=count+1
    elif b>a or c==b:
        print("Right Choice")
    else:
        print("You Lose")
        print("count")
        break
    

