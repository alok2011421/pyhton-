print("Here is your pizza bill")
s=input("Enter the size of your pizza S,M and L?")
p=input("Do you want papperoni?")
c=input("Do you want extra Chesse?")
bill=0
if s== "S":
    bill = 15
elif s=="M":
    bill = 20
else:
    bill = 25
if p=="Y":
    bill+=3
if c=="Y":
    bill+=5

print(f"Your bill is{bill}")