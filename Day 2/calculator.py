print("\t[Welcome to the tip calculator]")
total = input("\nWhat was the total bill? \n$")
percentage = input("\nWhat percentage tip would you like to give? 10, 12, or 15? \n")
people = input("\nHow many people to split the bill? \n")

result = ((int(percentage) / 100 * float(total)) + float(total)) / int(people)

print(f"\nEach person should pay ${format(result, '.2f')}")