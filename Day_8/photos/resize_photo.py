import os
from PIL import Image

def resize(name_root, new_width):
    folder = os.getcwd()
    print(folder)
    for nr, foto in enumerate(os.listdir(folder)):

        ext = os.path.splitext(foto)[1]

        if ext.lower() not in ['.png', '.jpg', '.jpeg', '.bmp']:
            continue

        zdjecie = Image.open(os.path.join(folder, foto))

        ratio = zdjecie.width / zdjecie.height
        new_height = round(new_width / ratio)

        male_foto = zdjecie.resize((new_width, new_height))
        nowa_nazwa = f"{name_root}{nr + 1}{ext}"

        male_foto.save(os.path.join(folder, nowa_nazwa))

        zdjecie.close()


resize("foto_", 800)
