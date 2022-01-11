
n = 3.14

print(type(n)) #mostra o tipo de classe da variável

# Arithmetic Operators:
# Addition:       3 + 2
# Subtraction:    3 - 2
# Multiplication: 3 * 2
# Division:       3 / 2
# Floor Division: 3 // 2 #ignora a parte decimal
# Exponent:       3 ** 2
# Modulus:        3 % 2 #mostra o resto de uma divisão

print(3 * 2 + 1)
print(3 * (2 + 1))

num = 1
num += 1 #soma ao valor atual
print(num)

print(abs(-3)) #mostra o valor absoluto do número
print(round(3.75)) #arredonda o valor para o valor inteiro mais próximo
print(round(3.75, 1)) #arredonda o valor para o valor com uma casa decimal

# Comparisons:
# Equal:            3 == 2
# Not Equal:        3 != 2
# Greater Than:     3 > 2
# Less Than:        3 < 2
# Greater or Equal: 3 >= 2
# Less or Equal:    3 <= 2

num_1 = 2
num_2 = 3

print(num_1 == num_2) #compara se o primeiro número é igual ao segundo

num_1 = '100'
num_2 = '200'

num_1 = int(num_1) #converte uma string em número inteiro
num_2 = int(num_2)

print(num_1 + num_2)