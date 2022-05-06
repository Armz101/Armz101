# COUNTDOWN
import time

#Countdown function
def coundown():
    for seconds in range(countdown):
        time.sleep(x)
        print(countdown-seconds)

while True:
    while True:
        try:
            countdown = int(input("How many numbers would you like to countdown? "))
            x = int(input("How many seconds would you like between the numbers? "))
            break
        except ValueError:
            print("Numbers only")


    if countdown and x >= 1:
        #Checks that both the inputs are greater than 0
        coundown()
        print("Finished")
        # Asks the user if they want another countdown
        again = str(input("Would you like to do another countdown? Y/N "))        
    else:
        #Tells the user they have to put a input greater than 0
        print("Both numbers must be higher than one!")
        # Asks the user if they want to do another countdown
        again = str(input("Would you like to do another countdown? Y/N "))      

    if again.upper() != "Y":
        break   
            
