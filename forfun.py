# import random
# tries = 3
# age =  [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
# ahsan = random.choice(age)

# def game():
#     global tries
#     while True: 
#         Guesser = int(input("How old do you think ahsan is?"))
#         if Guesser == ahsan:
#             print("You guessed ahsan's age.")
#             break
#         elif tries == 1:
#             print("Game over, ahsan's age was", ahsan)
#             break
#         else:
#             tries -= 1
#             print(f"Wrong, you have {tries} more tries.")

# game()
     
while True:
    try:
        a = int(input("What is x?"))
        break
    except ValueError:
        print ("Enter a number")