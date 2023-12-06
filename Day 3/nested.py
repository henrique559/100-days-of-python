print("\t[Rollercoaster]\t")
height = int(input("What is your height in cm?\n> "))
#
if height > 120 or height < 200:
    print("\nYou can ride the rollercoaster!")
    age = int(input("How years old are you?\n> "))
    if age <= 12:
        price = 5.00
        print(f"\nWelcome to the Rollercoaster\nPrice: ${format(price, '.2f')}\n")
    elif age >= 12 and age <= 18:
        price = 7.00
        print(f"\nWelcome to the Rollercoaster\nPrice: ${format(price, '.2f')}\n")
    else:
        price = 12.00
        print(f"\nWelcome to the Rollercoaster\nPrice: ${format(price, '.2f')}\n")
else:
    print("You can't enter the Rollercoaster")