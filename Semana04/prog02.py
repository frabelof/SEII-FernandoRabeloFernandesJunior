
menssagem = 'Ola Mundo'

print(menssagem) #mostra a string
print(len(menssagem)) #mostra no número de caracteres da string
print(menssagem[0]) #mostra o primeiro caractere da string
print(menssagem[:5]) #mostra os caracteres do primeiro ao índice 5 não incluindo o índice 5
print(menssagem[6:]) #mostra os caracteres a partir do índice 6
print(menssagem.lower()) #mostra a string com todas as letras minúsculas
print(menssagem.count('l')) #mostra quantos caracteres l estão na string
print(menssagem.find('l')) #mostra onde está o primeiro caractere l da string

nova_menssagem = menssagem.replace('Mundo', 'Universo') #substitui na menssagem o primeiro argumento da função pelo segundo
print(nova_menssagem)

cumprimento = 'Ola'
nome = 'Murilo'
segunda_menssagem = '{}, {}. Bemv-indo!'.format(cumprimento, nome) #cria uma nova string concatenando strings anteriores e formatando-as
#segunda_menssagem = f'{cumprimento}, {nome}. Welcome!' #faz o mesmo que a linha acima
print(segunda_menssagem)

print(dir(nome)) #mostra todas as funções que podem ser usadas com essa variável
print(help(str.lower))