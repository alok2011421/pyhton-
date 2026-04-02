import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
password=[]
print("You will get a password of 16 letters")
for i in range(0,nr_letters):
    a=random.randint(0,25)
    password.append(letters[a])
for i in range(0,nr_numbers):
    b=random.randint(0,9)
    password.append(numbers[b])
for i in range(0,nr_symbols):
    c=random.randint(0,8)
    password.append(symbols[c])
password_string= ''.join(password)
print(password_string)
random.shuffle(password)  # This shuffles password in place
password_string = ''.join(password)  # Join the already-shuffled password list
print(password_string)