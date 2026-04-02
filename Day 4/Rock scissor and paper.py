import random

l=["""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
"""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""",
"""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""]
a=random.randint(0,2)
b=int(input("Enter your choice"))
print (a)
if a==0 and b==2:
    print("System wins")
    print("User lost")
if a==2 and b==1:
    print("System wins")
    print("User lost")
if a==1 and b==0:
    print("System wins")
    print("User lost")
if a==2 and b==0:
    print("User wins")
    print("System lost")
if a==1 and b==2:
    print("User wins")
    print("System lost")
if a==0 and b==1:
    print("User wins")
    print("System lost")
if a==b:
    print("Match draw")


#Option 2
''' import random

a = random.randint(0, 2)
b = int(input("Enter your choice (0=Rock, 1=Paper, 2=Scissors): "))

if a == b:
    print("Tie")
elif (a - b) % 3 == 1:
    print("System wins\nUser lost")
else:
    print("User wins\nSystem lost")
'''