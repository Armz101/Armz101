height = int(input("How tall would you like the trangle to be? "))

for rows in range(1, height+1):
    # display spaces
    for spaces in range(1,(height-rows)+1):
        print("",end="")
    # try to display *
    for stars in range(1,rows+1):
        print("*", end="")
    print(rows)

