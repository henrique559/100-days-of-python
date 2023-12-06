print("\t[Rollercoaster]\t")
price = 0
height = int(input("What is your height in cm?\n> "))
#
if height >= 120 and height <= 200:
    print("\nYou can ride the rollercoaster!")
    age = int(input("How years old are you?\n> "))
    if age <= 12:
        price = 5.00
        print(f"\nWelcome to the Rollercoaster\nPrice: ${format(price, '.2f')}\n")
    elif age >= 12 and age <= 18:
        price = 7.00
        print(f"\nWelcome to the Rollercoaster\nPrice: ${format(price, '.2f')}\n")
    elif age >= 45 and age <= 55:
        print("Everything is going to be ok. Have a free ride on us!")
    
    else:
        price = 12.00
        print(f"\nWelcome to the Rollercoaster\nPrice: ${format(price, '.2f')}\n")
        
    wants_photo = input("Do you want a photo taken? (Y or N)\nPrice: 3$\n> ")
    
    if wants_photo == "Y" or "y":
        price += 3.00
        
else:
    print("You can't enter the Rollercoaster")
    exit() 

print(f"\nTotal: ${format(price, '.2f')}")
    