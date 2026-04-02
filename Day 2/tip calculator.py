print("Welcome to the tip calculator!")
b=int(input("What was the total bill?"))
t=int(input("How much tip would you like to give?"))
s=int(input("How many people to split the bill?"))
c=(b+t)/s
print("Each person should pay:",c)