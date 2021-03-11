import cv2

#img = cv2.imread('messi5.jpg')



in_file = input()
img = cv2.imread(in_file)
print(img)
pixel = img[0, 0]
print("Red: {0}".format(pixel[2]))
print("Green: {0}".format(pixel[1]))
print("Blue: {0}".format(pixel[0]))

