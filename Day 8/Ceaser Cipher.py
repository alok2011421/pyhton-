alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print("""           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88           
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
""")
while True:
 def encrypt(text,shift):
    new=[]
    for letter in text:
         if letter in alphabet: 
          c=alphabet.index(letter)+shift
          new.append(alphabet[c])
         else:
            new.append(letter)
        
    print(''.join(new))
    
 def decrypt(text,shift):
    new=[]
    for letter in text:
        if letter in alphabet: 
          c=alphabet.index(letter)-shift
          new.append(alphabet[c])
        else:
            new.append(letter)
    print(''.join(new))


 direction=input("Type 'encode' to encrypt,type 'decode' to decrypt \n").lower()
 if direction=="encode":
    text=input("Enter the message\n").lower()
    shift=int(input("How many letters do you want to shift"))
    encrypt(text,shift)
 elif direction=="decode":
    text=input("Enter the message\n").lower()
    shift=int(input("How many letters do you want to shift"))
    decrypt(text,shift)
 else:
    print("Invalid text")
 a=input("Do you want repeat if yes type 'yes' in no type'No'?").lower()
 if a=="no":
    break

