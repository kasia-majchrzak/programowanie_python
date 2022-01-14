from person_detector_service import detect
import images_service as imgService


images = imgService.getImagesInDir("images")
for img in images:
    img = detect(img)
