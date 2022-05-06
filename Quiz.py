name = input("Hello, what is your name?: ")
print('Hello', name, 'welcome to the computer part test where you will be'+ \
'testing your knowledge about computers')


ready = input('Are you ready for the quiz?: ')
if ready.lower() != 'yes':
    print('See you next time!')
    quit()
else:
    print('You will be tested on three core components of the computer.')

while True:
    sum = 0

    awnser = input('1. What is the full long term for the word CPU called?: ')
    if awnser.lower() == 'central processing unit':
        sum += 1
        print("Correct!")

    else:
        print("Wrong!")

    print("Points =", sum)   

    awnser2 = input('2. What does the word GPU stand for?: ')
    if awnser2.lower() == 'graphics processing unit':
        print("Correct!")
        sum += 1
    else:
        print("Wrong!")

    print("Points =", sum)

    awnser3 = input('3. What does the word RAM stand for?: ')
    if awnser3.lower() == 'random access memory':
        print("Correct!")
        sum += 1
    else:
        print('Wrong!')

    print("Points =", sum)

    if sum <= 1:
        print('Unfortunatly', name, 'you have failed the quiz.')
        retest = input('Would you like to redo the test?: ')
        if retest.lower() != 'yes':
            break
    elif sum >= 2:
        print("Congratulation", name, "You have passed the test.")
        break
    else:
        continue

print("Goodbye")