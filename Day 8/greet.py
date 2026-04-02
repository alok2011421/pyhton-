import random
def greet(a):
    if a==1:
        print("Good Morning")
    elif a==2:
        print("Good Evening")
    else:
        print("Good Night")
a=random.randint(0,2)
greet(a)