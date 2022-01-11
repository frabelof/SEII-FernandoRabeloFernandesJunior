
cursos = ['Historia', 'Matematica', 'Fisica', 'Computacao']
print(cursos)
print(len(cursos))
print(cursos[0])
print(cursos[-1])
print(cursos[:2])
print(cursos[2:])

cursos.append('Arte') #adiciona um elemento ao final da lista
cursos.insert(0, 'Geography') #adiciona um elemento na posição da lista que foi especificada
print(cursos)

cursos2 = ['Chemistry', 'Educatiom']
#cursos.insert(0, cursos2) #também é possível adicionar uma lista à outra lista
cursos.extend(cursos2) #faz a fusão de duas listas
print(cursos)

cursos = ['Historia', 'Matematica', 'Fisica', 'Computacao']
cursos.remove('Matematica') #retira da lista o termo especificado
popped = cursos.pop() #retira da lista o último termo
print(popped)
print(cursos)

cursos = ['Historia', 'Matematica', 'Fisica', 'Computacao']
cursos.reverse() #invrete a ordem dos elementos da lista
print(cursos)

cursos.sort() #ordena os elementos da lista em ordem alfabética (ou em ordem crescente, se os elementos foram números)
print(cursos)

cursos = ['Historia', 'Matematica', 'Fisica', 'Computacao']
sorted_cursos = sorted(cursos) #cria uma nova lista com os elementos da lista anterior ordenados
print(cursos)
print(sorted_cursos)

num = [1, 2, 3, 4, 5]
print(min(num)) #mostra o menor número da lista
print(max(num)) #mostra o maior número da lista
print(sum(num)) #mostra a soma dos números da lista

cursos = ['Historia', 'Matematica', 'Fisica', 'Computacao']
print(cursos.index('Computacao')) #mostra quaç é o índice do elemento especificado
print('Matematica' in cursos) #diz se o elemento está ou não na lista

for curso in enumerate(cursos, start=1): #mostras os ítens da lista e seus respectivos índices começando com o número 1
    print(curso)

cursos_str = ', '.join(cursos) #une os ítens da lista em uma única string
print(cursos_str)
nova_lista = cursos_str.split(', ') #separa os elementos de uma string e os coloca em uma lista
print(nova_lista)

# Mutável
lista_1 = ['Historia', 'Matematica', 'Fisica', 'Computacao']
lista_2 = lista_1

print(lista_1)
print(lista_2)

lista_1[0] = 'Arte'

print(lista_1)
print(lista_2)


# Imutavel
tupla_1 = ('Historia', 'Matematica', 'Fisica', 'Computacao')
tupla_2 = tupla_1

print(tupla_1)
print(tupla_2)

# tupla_1[0] = 'Art' #tuplas não podem ser alteradas

# print(tupla_1)
# print(tupla_2)

# Sets
#sets não têm ordens e nem elementos repetidos
cs_cursos = {'Historia', 'Matematica', 'Fisica', 'Computacao'}
print(cs_cursos)
arte_cursos = {'Historia', 'Matematica', 'Arte', 'Design'}
print(cs_cursos.intersection(arte_cursos)) #mostra os elementos comuns nos dois sets
print(cs_cursos.difference(arte_cursos)) #mostra os elementos diferentes nos dois sets
print(cs_cursos.union(arte_cursos)) #unifica os elementos dos dois sets

# Lista Vazia
lista_vazia = []
lista_vazia = list()

# Tupla Vazia
tupla_vazia = ()
tupla_vazia = tuple()

# Set Vazio
#set_vazio = {} # isso não é m set, set um dicionário
set_vazio = set()
