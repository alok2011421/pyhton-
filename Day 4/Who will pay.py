import random
friends=["Alok","Ankit","Abhijeet","Abhishek","Uplakshya","Anurag"]

# option 1
a=random.randint(0,5)
print(f"{friends[a]} will pay the bill")

#option 2
print(random.choice(friends))