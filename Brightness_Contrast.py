import cv2
import os


arrp=[]
i=-1
# Set the directory path
directory = 'D:\PHOTOS\Scanner'

# Extract all files in the directory
for filename in os.listdir(directory):
    if filename.endswith('.jpg'):
       s=os.path.join(directory, filename)
       arrp.append(s)
       i=i+1


def get_brightness_contrast(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    brightness = cv2.mean(gray)[0]
    std = cv2.meanStdDev(gray)[1]
    contrast = std[0][0] / brightness

    return brightness, contrast

j=0
k=0
arrb=[]
arrc=[]
while (i!=0):
    print("image "+ arrp[i] + ":")
    print(" ")
    image = cv2.imread(arrp[i])
    brightness, contrast = get_brightness_contrast(image)
    b= brightness
    arrb.append(b)
    j=j+1
    print(arrb[j-1])
    c= contrast
    arrc.append(c)
    k=k+1
    print(arrc[k-1])
    print(" ")
    i=i-1
    
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

j=j-1

while (j!=0):

    print(quicksort(arrb[j]))
    j=j-1
