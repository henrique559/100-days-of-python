# print(round(8/3)) - Arredonda o numero
# print(8/3) - Divisao normal
# print(int(8/3)) - Remove o ponto flutuante e não arredonda

# print(round(8/3, 2))
# O Segundo argumento serve para mostrar a quantidade de numeros após a virgula || Ex: %.2f 

# print(round(3.14159, 2))

# // = Realiza a divisão, porém remove todos os números decimais e transforma em INT 
# print(8 // 3) # == print(int(8/3))

# result = 4 / 2
# result /= 2 # Igual em C, result /= || result = result / 2
# print(int(result))

# score = 0 
# score += 1 # ou score = score + 1 || score -= 1 > score = score - 1
 
 # f-String
score = 0
height = 1.8
isWinning = True 

# Colocar f antes dos parenteses, agora o print pode colocar variaveis dentro da string, utilizando {}
print(f"Your score is {score}, your height is {height}, you are winning is {isWinning}")