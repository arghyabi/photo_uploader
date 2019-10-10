import requests
import os

url = 'http://www.photo.arghyabiswas.com/upload.php'
folder="photo_th/"
photos=[]
index=1

for photo in os.listdir(folder):
    photos.append(photo)

for photo in photos:
    print(str(index)+": "+str(photo))
    index += 1
    files = {'fileToUpload': open(folder+photo, 'rb')}
    r = requests.post(url, files=files)
