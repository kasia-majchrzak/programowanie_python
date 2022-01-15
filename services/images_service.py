import os


def getImagesInDir(dir_path: str) -> list:
    images = []
    for filename in os.listdir(dir_path):
        ext = os.path.splitext(filename)[1]
        if ext.lower() not in [".jpg", ".png"]:
            continue
        else:
            images.append(os.path.join("images", filename))

    return images
