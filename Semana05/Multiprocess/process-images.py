#Guilherme Gonzaga Silva 
# 11621EMT021

import time
import concurrent.futures
from PIL import Image, ImageFilter #biblioteca precisa ser instalada, serve para trabalhar com imagens 
#ja baixamos as imagens e agora queremos redimensionar a imagem para 1200x1200

img_names = [ #nome das imagens que foram ja baixadas
    'photo-1516117172878-fd2c41f4a759.jpg',
    'photo-1532009324734-20a7a5813719.jpg',
    'photo-1524429656589-6633a470097c.jpg',
    'photo-1530224264768-7ff8c1789d79.jpg',
    'photo-1564135624576-c5c88640f235.jpg',
    'photo-1541698444083-023c97d3f4b6.jpg',
    'photo-1522364723953-452d3431c267.jpg',
    'photo-1513938709626-033611b8cc03.jpg',
    'photo-1507143550189-fed454f93097.jpg',
    'photo-1493976040374-85c8e12f0c0e.jpg',
    'photo-1504198453319-5ce911bafcde.jpg',
    'photo-1530122037265-a5f1f91d3b99.jpg',
    'photo-1516972810927-80185027ca84.jpg',
    'photo-1550439062-609e1531270e.jpg',
    'photo-1549692520-acc6669e2f0c.jpg'
]

t1 = time.perf_counter()

size = (1200, 1200) #nova resolução das fotos

for img_name in img_names:
   img = Image.open(img_name) #para cada imagem, iremos abir a imagem e então 

   img = img_filter(ImageFilter.GaussianBlur(15)) #roda esse filtro de imagem que deixa um blur na foto

   img.thumbnail(size) #nova resolução
   img.save(f'processed/{img_name}') #salvmos essa nova imagem, lembrando que essa pasta deve ter sido criada previamente para salvar os arquivos
   print(f'{img_name} was processed...') #fala que o processo foi concluido

#def process_image(img_name): 
#    img = Image.open(img_name)

#    img = img.filter(ImageFilter.GaussianBlur(15))

#    img.thumbnail(size)
#    img.save(f'processed/{img_name}')
#    print(f'{img_name} was processed...')


#with concurrent.futures.ProcessPoolExecutor() as executor: #utilizando o processpoolexecutor
#    executor.map(process_image, img_names) #rodar a função process para cada valor de url rodando paralelamente


t2 = time.perf_counter()

print(f'Finished in {t2-t1} seconds')