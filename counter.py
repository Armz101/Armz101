# COUNTER
import re
import time

#counter Function
def count():
    for i in range(counter):
        time.sleep(x)
        print(i+1)


# While loop To make another counter without closing the program
while True:
    #Takes user inputs
    counter = int(input("How many numbers would you like to count? "))
    x = int(input("How much seconds would you like between each number? "))

    if counter and x >= 1:
        # Checks if both inputs are greater than 0
        count()
        print("Finished")
        # Asks the User if they want another counter after the other is done
        again = str(input("Would you like to do another count? Y/N "))
        if again.upper() != "Y":
            break
    else:
        # Tells the user they must have a higher number than one for their input
        print("Both numbers must be higher than 1!")
        # Asks the user if they want another counter
        again = str(input("Would you like to do another count? Y/N "))
        if again.upper() != "Y":
            break