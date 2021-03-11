import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
img = cv2.imread('Lorem_Ipsum_rot.png')
text = pytesseract.image_to_string(img)
text = text[:-2].splitlines()
broj = 0
for i in range(len(text)):
    if text[i]!='':
        broj+=1
print(text)
print(broj)
