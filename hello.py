import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
img = Image.open('1-1-4.jpg')


text = pytesseract.image_to_string(img)
print(text)