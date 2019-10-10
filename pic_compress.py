from PIL import Image
import os

folder="photo/"
photos=[]

compress = 20
index=1

for photo in os.listdir(folder):
    photos.append(photo)

for photo in photos:
    Ifile = Image.open(folder+photo)
    print(str(index)+" : "+photo)
    index += 1
    h = int(Ifile.size[0]*compress/100)
    w = int(Ifile.size[1]*compress/100)

    Ifile=Ifile.resize((h,w))

    Ifile.save("photo_th/"+photo.lower())
