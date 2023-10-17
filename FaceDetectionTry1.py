from cvzone.FaceDetectionModule import FaceDetector
import cv2
import matplotlib.pyplot as plt

test = cv2.imread('images/image3.jpg')
detector = FaceDetector()
img, bboxs = detector.findFaces(test)
if bboxs:
    x1, y1, w1, h1 = bboxs[0]['bbox']
    x2 = x1 + w1
    y2 = y1 + h1
    img2 = cv2.imread("images/image4.jpg")
    img2_resized = cv2.resize(img2, (w1, h1))
    img[y1:y2, x1:x2] = img2_resized  # Inserta la imagen 2 en la imagen 1
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(img)
    plt.axis('off')
    plt.show()
