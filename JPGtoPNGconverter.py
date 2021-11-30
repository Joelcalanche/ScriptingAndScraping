import sys
import os
from PIL import Image

# grab first and second argument
# el argumento 0 es el nombre del script
image_folder = sys.argv[1]
output_folder = sys.argv[2]


# check is new/ exists, if not create it
if not os.path.exists(output_folder):
    os.makedirs(output_folder)





# loop through Pokedex
# listdir retorna una lista con los elementos (files)dentro de un folder
for filename in os.listdir(image_folder):
    # Se asume que la el folder tiene '/' al final
    img = Image.open(f'{image_folder}{filename}')
    # removemos la extension .jpg  el metodo splitex retorna una tupla(name, extension)
    clean_name = os.path.splitext(filename)[0]
    # print(clean_name)
    img.save(f'{output_folder}{clean_name}.png', 'png')
    print('all done!')

# Convert images to png

# Save to the new folder.