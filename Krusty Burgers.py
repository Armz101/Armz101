while True:
    def menu():
        print("Welcome to Krusty Burgers!")
        print("1.Krusty Burger","                                  ","$5.10")
        print("2.Milkshake","                                      ","$3.50")
        print("3.Krusty Meal set[Burger + Drink + Krusty Laugh","  ","10.50")

    menu()

    x = int(input("Enter order amount for number 1: "))
    y = int(input("Enter order amount for number 2: "))
    z = int(input("Enter order amount for number 3: "))

    def order(num1,num2,num3):
        total = num1*5.1 + num2*3.5 + num3*10.5
        return total

    print("Order Summary")
    print("1.Krusty Burger","                                  ","$","5.10 x", x )
    print("2.Milkshake","                                      ","$","$3.50 x", y)
    print("3.Krusty Meal set[Burger + Drink + Krusty Laugh]","  ","$","10.50 x",z)
    print("Total","                                            ","$",order(x,y,z))

    reorder = input("Would you like to order again? (Yes/No):  ")
    if reorder.lower() != "yes":
       break

    #Test

print("Have a Great Krusty Day!")



