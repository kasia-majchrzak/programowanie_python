try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import cv2
from os.path import exists

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'


def read_text_from_file_with_gaussian_blur(file_path: str):
    if exists(file_path):
        img = cv2.imread(file_path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = cv2.threshold(cv2.GaussianBlur(img, (5, 5), 0), 0, 255,
                            cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
        cv2.imshow('image', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        print(f'Extracted text from file {file_path}: \n {pytesseract.image_to_string(img)}\n')
    else:
        print(f'File {file_path} not found')


def read_text_from_file_with_bilateral_filter(file_path: str):
    if exists(file_path):
        img = cv2.imread(file_path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = cv2.threshold(cv2.bilateralFilter(img, 5, 75, 75), 0, 255,
                            cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

        print(f'Extracted text from file {file_path}: \n {pytesseract.image_to_string(img)}\n')
    else:
        print(f'File {file_path} not found')


def read_text_from_file_with_median_blur(file_path: str):
    if exists(file_path):
        img = cv2.imread(file_path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = cv2.threshold(cv2.medianBlur(img, 3), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

        print(f'Extracted text from file {file_path}: \n {pytesseract.image_to_string(img)}\n')
    else:
        print(f'File {file_path} not found')


read_text_from_file_with_median_blur("photos/captcha1.png")
read_text_from_file_with_bilateral_filter("photos/captcha2.jpg")
read_text_from_file_with_gaussian_blur("photos/captcha3.jpg")