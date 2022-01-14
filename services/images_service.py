import cv2
import os


def getImagesInDir(dir_path: str) -> list:
    images = []
    for filename in os.listdir(dir_path):
        ext = os.path.splitext(filename)[1]
        if ext.lower() not in [".jpg", ".png"]:
            continue
        else:
            img = cv2.imread(os.path.join("../images", filename))
            images.append(img)

    return images
