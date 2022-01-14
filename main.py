from services.person_detector_service import detect
from services.images_service import getImagesInDir

images = getImagesInDir("images")
for img in images:
    img = detect(img)
