import cv2
import imutils
import time

hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())


def detect(image: any):
    start = time.time()
    image = imutils.resize(image, width=min(800, image.shape[1]))
    image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    (regions, _) = hog.detectMultiScale(image,
                                        winStride=(4, 4),
                                        padding=(4, 4),
                                        scale=1.05)

    human_counter = 0
    image = cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)
    for (x, y, w, h) in regions:
        cv2.rectangle(image, (x, y),
                      (x + w, y + h),
                      (0, 255, 0), 2)
        human_counter += 1

    end = time.time()
    cv2.putText(image, f'Total : {human_counter}',
                (20, 40),
                cv2.FONT_HERSHEY_DUPLEX,
                0.8, (0, 0, 255), 2)
    cv2.putText(image, f'Time : {end - start}',
                (20, 60),
                cv2.FONT_HERSHEY_DUPLEX,
                0.8, (0, 0, 255), 2)

    cv2.imshow('output', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
