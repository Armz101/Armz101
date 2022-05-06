#Make program readable and optimized as much as possible
#Because python programs have a specific structure 


#Scopes 1.1

# x = 10
# def func():
#     global x
#     x += 2
#     return x

# print(func())


# people = [
#     ("Alice", 30),  # Tuple
#     ("Carol", 15),
#     ("Dylan", 5)
# ]

# youngest = people[0]
# for elm in people:
#     if elm[1] < youngest[1]:
#         youngest = elm

#  print(f"Youngest: {youngest[0]} at {youngest[1]} years old. ")


import sys

loser = []
i = 0
sum = int(sys.argv[1])
num = sum
while i in range(5):
    i += 1
    loser.append(num)
    num += 1

adam = loser.copy()
for num in range(len(adam)):
    if adam[num] %2 == 0:
        adam[num] = int(adam[num]/2)
    

    

print(loser)
print(adam)

# import sys
# bruh = sys.argv
# del bruh[0]
# for bruh2 in sys.argv:
#     print(bruh2[0], end= "")
    



