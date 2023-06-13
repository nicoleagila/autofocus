import cv2
import sys


def metric(img):
    value=0.5
    return value

input = sys.argv[1]
images=[]
entries = os.listdir(input)
for entry in entries:
    images.append(cv2.imread(entry, 0))

print("la imagen resultante es {} y su metrica fue {}".format(entries[0],metric(images[0])))