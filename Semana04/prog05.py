
estudante = {'nome':'Joao','idade':25,'cursos':['Matematica', 'computacao']}
print(estudante)
print(estudante['nome'])
print(estudante['cursos'])
estudante['telefone']='555-5555'
print(estudante)

estudante = {'nome':'Joao','idade':25,'cursos':['Matematica', 'computacao']}
estudante.update({'nome':'Jane','idade':26, 'telefone':'555-5555'})
print(estudante)
del estudante['idade']
print(estudante)

estudante = {'nome':'Joao','idade':25,'cursos':['Matematica', 'computacao']}
estudante.update({'nome':'Jane','idade':26, 'telefone':'555-5555'})
idade = estudante.pop('idade')
print(idade)


estudante = {'nome':'Joao','idade':25,'cursos':['Matematica', 'computacao']}

print(len(estudante))
print(estudante.keys)
print(estudante.values)
print(estudante.items)

print(estudante)
for x,valor in estudante.items():
    print(x,valor)
