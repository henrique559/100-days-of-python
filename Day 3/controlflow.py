# if condition:
# do this
# else:
# do this

print("[Rollercoaster]\n")
height = float(input("What's your height?\nR:"))
if height >= 1.20 and height <= 2.00:
    print("Welcome to the rollercoaster")
elif height > 2.00:
    print("Are you a human?")
else:
    print("You can't ride the rollercoaster")