import cv2
import pytesseract
import os
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
t = input("Drag and drop image here: ")
t = str(t).replace('"','')
img = cv2.imread(t)
text = pytesseract.image_to_string(img)
os.system("cls")
print(text)
os.system("pause")