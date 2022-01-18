#GUilherme Gonzaga SIlva
#11621EMT021

#multiprocessing serve para aumentar a velocidade do nosso programa, vindo de tarefas rodando em paralelo

import time
# import multiprocessing
import concurrent.futures

start = time.perf_counter() #starta um contador

# def do_something(): #define a founção do_something() 
#     print('Sleeping 1 second...') #printa que vamos dormir 1 segundo
#     time.sleep(1) #dorme por um segundo
#     print('Done SLeeping...') #terminamos de dormir 

def do_something(seconds): #define a founção do_something() recebendo como argumento os segundos que irá dormir
    print(f'Sleeping {seconds} second(s)...') #nos fala a quantos segundos dormirá, usamos f string para passar a variavel seconds
    time.sleep(seconds) #coloca pra dormir seconds segundos
    return f'Done Sleeping...{seconds}' #retorna que acabou de dormir e os segundos 


with concurrent.futures.ProcessPoolExecutor() as executor:
    # f1 = executor.submit(do_something, 1)
    # f2 = executor.submit(do_something, 1)
    # print(f1.result())
    # print(f2.result())
    secs = [5, 4, 3, 2, 1] #testa para outros segundos
    #results = [executor.submit(do_something, sec) for sec in secs]
    results = executor.map(do_something, secs) #com map, em vez de retorna os resultados, agora vai ainda rodar as threads concorrentemente, porém retorará os resultados na ordem que foram startados

    # for f in concurrent.futures.as_completed(results):
    #     print(f.result())
           
#vamos rodar sincronizadamente o código
# processes = [] lista de processos vazia
# for _ in range(10): #iremos dormir 10 vezes, para isso startamo no loop, logo colocamos todos os itens anteriores dentro do loop
#     p = multiprocessing.Process(target=do_something, args=[1.5]) #passamos os argumentos a função com uma lista de um valor e garante que irá dormir por 1.5 segundos
#     p.start()
#     processes.append(p) #não podemos fazer o join dentro do loop, acrescemos a cada thread que starta 

# for process in processes: #precisamos de uma lista de todas os processos que startamos, para isso criamos um loop
#     process.join() #agora realmente estamos rodando a musica 10 vezes e dorme 1 segundo toda vez. 

# for result in results:
#     print(result)

# p1 = multiprocessing.Process(target=do_something) #cria o processo do_something ao invez de chamar a fubnção
# p2 = multiprocessing.Process(target=do_something) #cria o processo novamente 

# p1.start() #starta o processo
# p2.start() #starta o processo 

#o método join garante que os dois completem antes de ir para calculo do final
# p1.join()
# p2.join()

# do_something() #chama a função do_something para domir 
# do_something() #dorme de novo, porém roda uma de cada vez

finish = time.perf_counter() #calcula o tempo final

print(f'Finished in {round(finish-start, 2)} second(s)') #printa quanto tempo gastamos para dormir