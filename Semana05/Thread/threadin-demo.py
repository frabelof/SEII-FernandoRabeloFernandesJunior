# Guilherme Gonzaga Silva 
# 11621EMT021 

import time
# import threading #
import concurrent.futures

start = time.perf_counter() #estarta um contador 

def do_something(seconds): #define a founção do_something() recebendo como argumento os segundos que irá dormir
    print(f'SLeeping {seconds} second(s)...') #nos fala a quantos segundos dormirá, usamos f string para passar a variavel seconds
    time.sleep(seconds) #coloca pra dormir seconds segundos
    # print('Done Sleeping...') # termina de dormir
#    return 'Done Sleeping...'
    return f'Done Sleeping...{seconds}' #retorna que acabou de dormir e os segundos 

#fazendo a mesma coisa com o módulo future da biblioteca concurrent.futures. O método future, e
with concurrent.futures.ThreadPoolExecutor() as executor: 
#     f1 = executor.submit(do_something, 1) #criamos os executors passando o argumento 1, para 1 segundo
#     f2 = executor.submit(do_something, 1)
#     print(f1.result()) #rodando o método result, nos esperamos até a função se completar 
#     print(f2.result())
#     results = [executor.submit(do_something, 1) for _ in range(10)]
    secs = [5, 4, 3, 2, 1] #testa para outros segundos 
    results = executor.map(do_something, secs)  #com map, em vez de retorna os resultados, agora vai ainda rodar as threads concorrentemente, porém retorará os resultados na ordem que foram startados

#     for result in results:
#         print(result)
    
#     results = [executor.submit(do_something, sec) for sec in secs] #para rodar o méotodo future secs vezes.

#     for f in concurrent.futures.as_completed(results): #para cosneguir os resultados, nos podemos usar essa função as_completed que nos da um iterator e, fazendo um loop sobre e produzirá os resultados.
#         print(f.result())

# utilizando o método das threads, o código roda mais rápido, pois starta as duas threads e enquanto uma esta dormindo o código roda concoretemente e continuou com o resto do código
# do_something() #chama a função
# t1 = threading.Thread(target=do_something) #cria a primeira thread, como não queremos executar a função, fica sem o ()
# t2 = threading.Thread(target=do_something) #cria a segunda thread

# t1.start() #starta a thread 1
# t2.start() #starta a thread 2

#o método join garante que os dois completem antes de ir para calculo do final
# t1.join() 
# t2.join()

# threads = [] #lista de threads vazio

#vamos agora fazer o código rodar 10x mais rapido
# for _ in range(10): #iremos dormir 10 vezes, para isso startamo no loop, logo colocamos todos os itens anteriores dentro do loop
#     t = threading.Thread(target=do_something, args=[1.5]) #passamos os argumentos a função com uma lista de um valor e garante que irá dormir por 1.5 segundos
#     t.start()
#     threads.append(t) #não podemos fazer o join dentro do loop, acrescentando a cada thread que starta 

# for thread in threads: #precisamos de uma lista de todas essas threads que startamos, para isso criamos um loop
#     thread.join() #agora realmente estamos rodando a musica 10 vezes e dorme 1 segundo toda vez. 

finish = time.perf_counter() #termina de dormir 

print(f'Finished in {round(finish-start, 2)} second(s)') #pr8intamos que o código acabou e o total numero de segundos