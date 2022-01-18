#GUilherme Gonzaga Silva
#11621EMT021

import requests
import time
import concurrent.futures
# baixará fotos do servidor unsplash de alta resolução
#Demorou bastante mesmo com a implementação, porém acredito que seja pq o servidor das fotos eh muito longe

img_urls = [ #urls das imagens
    'https://images.unsplash.com/photo-1516117172878-fd2c41f4a759',
    'https://images.unsplash.com/photo-1532009324734-20a7a5813719',
    'https://images.unsplash.com/photo-1524429656589-6633a470097c',
    'https://images.unsplash.com/photo-1530224264768-7ff8c1789d79',
    'https://images.unsplash.com/photo-1564135624576-c5c88640f235',
    'https://images.unsplash.com/photo-1541698444083-023c97d3f4b6',
    'https://images.unsplash.com/photo-1522364723953-452d3431c267',
    'https://images.unsplash.com/photo-1513938709626-033611b8cc03',
    'https://images.unsplash.com/photo-1507143550189-fed454f93097',
    'https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e',
    'https://images.unsplash.com/photo-1504198453319-5ce911bafcde',
    'https://images.unsplash.com/photo-1530122037265-a5f1f91d3b99',
    'https://images.unsplash.com/photo-1516972810927-80185027ca84',
    'https://images.unsplash.com/photo-1550439062-609e1531270e',
    'https://images.unsplash.com/photo-1549692520-acc6669e2f0c'
]

t1 = time.perf_counter()

#  for img_url in img_urls:
#     img_bytes = requests.get(img_url).content #usamos a biblioteca request para acessar o conteudo do url
#     img_name = img_url.split('/')[3] #string para analisar o nome da photo
#     img_name = f'{img_name}.jpg'  #pegando o nome da imagem e colando o .jpg
#     with open(img_name, 'wb') as img_file: #abre o arquivo no modo wb
#         img_file.write(img_bytes) #escreve os bytes da imagem que baixou da internet para o file 
#         print(f'{img_name} was downloaded...') # printa que o download foi concluido

#otimizando, movendo para o proximo url sem esperar a resposta do site
def download_image(img_url): #define uma função passando o argumento do url da imagem
    img_bytes = requests.get(img_url).content
    img_name = img_url.split('/')[3]
    img_name = f'{img_name}.jpg'
    with open(img_name, 'wb') as img_file:
        img_file.write(img_bytes)
        print(f'{img_name} was downloaded...')


with concurrent.futures.ThreadPoolExecutor() as executor: #utilizando o threadpoolexecutor
    executor.map(download_image, img_urls) #rodar a função dowdnload para cada valor de url, baixando com um thread diferente para cada um


t2 = time.perf_counter()

print(f'Finished in {t2-t1} seconds')