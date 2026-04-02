logo = '''
  _______ _             _____ _ _            _                        _   _             
 |__   __| |           / ____(_) |          | |       /\             | | (_)            
    | |  | |__   ___  | (___  _| | ___ _ __ | |_     /  \  _   _  ___| |_ _  ___  _ __  
    | |  | '_ \ / _ \  \___ \| | |/ _ \ '_ \| __|   / /\ \| | | |/ __| __| |/ _ \| '_ \ 
    | |  | | | |  __/  ____) | | |  __/ | | | |_   / ____ \ |_| | (__| |_| | (_) | | | |
    |_|  |_| |_|\___| |_____/|_|_|\___|_| |_|\__| /_/    \_\__,_|\___|\__|_|\___/|_| |_|                                                                                        
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\

'''
person={}
while True:
 name=input("Enter the name:\n")
 amt=int(input("Enter the bid amount\n"))
 person [name]= amt
 a=input("Enter 'Yes' if there in more person else write 'no'\n ").lower()
 if a=="no":
  break
 else:
  print("\n" * 100) 
highest_bid = 0
winner = ""

for name, bid in person.items():
    
    if bid > highest_bid:
        highest_bid = bid
        winner = name

print(f"The winner is {winner} with a bid of {highest_bid}")