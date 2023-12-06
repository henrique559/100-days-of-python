import os

os.system('clear')
print("\t[Calculadora do amor]\n")
name1 = input("Qual é o seu nome?\n") # What is your name?
name2 = input("\nQual é o nome dele/dela\n") # What is their name?

combinated_names = name1 + name2
lower_names = combinated_names.lower()

t = lower_names.count('t')
r = lower_names.count('r')
u = lower_names.count('u')
e = lower_names.count('e')

l = lower_names.count('l')
o = lower_names.count('o')
v = lower_names.count('v')
e = lower_names.count('e')

true_total = (t + r + u + e)
love_total = (l + o + v + e)

total = int(str(true_total) + str(love_total))

if total <= 10:
    print(f"\nSua pontuação total é {total}, vocês combinam igual coca cola e mentos.")

elif total >= 80:
    print(f"\nSua pontuação total é {total}, AMOR VERDADEIRO.")
    

elif total >= 40 and total <= 50:
    print(f"\nSua pontuação total é {total}, vocês estão bem juntos :3")

else:
    print(f"\nSua pontuação total é {total}.")
    
input()