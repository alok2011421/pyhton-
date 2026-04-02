import random
logo={
    '''
    .------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _' |/ __| |/ / |/ _' |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
'-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_/
      |  \/ K|                            _/ |                
      '------'                           |__/      
'''
}
print(logo)
consent=input("Do you want to play Blackjack21? type 'Y' for yes or 'N' for no?").lower
cards=[11,1,2,3,4,5,6,7,8,9,10,10,10]
p1=0
p2=0
while consent:
    a=random.randint(0,11)
    print(f"Your card is {cards[a]}")
    p1+=cards[a]
    print(f"Your current score is {p1}")
    b=random.randint(0,11)
    print(f"Computer card is {cards[b]}")
    p2+=cards[b]
    print(f"Computer current score is {p2}")
    if p1>=21 and p2>=21:
        break 
    c=input("If you want to continue type 'y' or to pass type'n'?").lower()
    if c=="n":
        continue
    else:
        break
if p1>=21:
    print("You lose")
else:
    print("Computer lose")