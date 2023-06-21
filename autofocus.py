from PIL import Image
import os
import sys

def metric(img):
    value=0.5
    return value

input = sys.argv[2]
images=[]
entries = os.listdir(input)
for entry in entries:
    images.append(Image.open(input+entry))

print("la imagen resultante es {} y su metrica fue {}".format(entries[0],metric(images[0])))
