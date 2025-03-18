from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'
image_path= 'ibane1.jpg'
img=Image.open(image_path)
text = pytesseract.image_to_string(img,lang='fra')
print(text)