import cv2
import time
from imageai.Detection import ObjectDetection
import os

detector = ObjectDetection()
detector.setModelTypeAsRetinaNet()
detector.setModelPath(os.path.join("services", "resnet50_coco_best_v2.1.0.h5"))
detector.loadModel()
person_model = detector.CustomObjects(person=True)


def detect(imagePath: str, outputPath: str):
    start = time.time()

    detector.detectObjectsFromImage(input_image=imagePath,
                                    output_image_path=outputPath,
                                    custom_objects=person_model)
    end = time.time()

    image = cv2.imread(outputPath)
    cv2.putText(image, f'Time : {end - start}',
                (20, 60),
                cv2.FONT_HERSHEY_DUPLEX,
                0.8, (0, 0, 255), 2)

    cv2.imwrite(outputPath, image)


def detectPersonInImages(images):
    for idx, img in enumerate(images):
        detect(img, os.path.join("images/output", f"outputImg{idx}.jpg"))
