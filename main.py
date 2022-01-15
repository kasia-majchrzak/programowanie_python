from services.images_service import getImagesInDir
import os

from services.person_detector_service import detectPersonInImages

images = getImagesInDir("images")
detectPersonInImages(images)

