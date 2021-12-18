try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import cv2
from os.path import exists

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'


def read_text_from_file(file_path: str):
    if exists(file_path):
        img = cv2.imread(file_path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        print(f'Extracted text from file {file_path}: \n {pytesseract.image_to_string(img)}\n')
    else:
        print(f'File {file_path} not found')


read_text_from_file("photos/example1.jpg")
read_text_from_file("photos/example2.jpg")
read_text_from_file("photos/example3.png")
read_text_from_file("photos/example4.jpg")
read_text_from_file("photos/example5.jpg")
