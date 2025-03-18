from PIL import Image
import re
import pytesseract

pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'
image_tel= '/home/kl003468/PycharmProjects/PythonProject/demo/tel2.png'
img=Image.open(image_tel)
textp = pytesseract.image_to_string(img,lang='fra')
print(textp)
partternp= r'[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}'
textp=textp.replace(" ","")
resultatp = re.findall(partternp,textp)

if len(resultatp)==0:
    print("il n'y a pas de numéro de tel")
else:
    print('il y a des numéro de tel ', resultatp)
    for iban in resultatp:
        print(iban)