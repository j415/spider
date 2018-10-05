# author:aspiring

from PIL import Image

import pytesseract

file_path = "image/tesseracttest.jpg"

img = Image.open(file_path)

print(pytesseract.image_to_string(img))
