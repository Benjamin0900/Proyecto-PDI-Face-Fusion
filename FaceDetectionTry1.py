from cvzone.FaceDetectionModule import FaceDetector
import cv2
import matplotlib.pyplot as plt
import numpy as np

test = cv2.imread('images/image3.jpg')
detector = FaceDetector()
img, bboxs = detector.findFaces(test)
if bboxs:
    x1, y1, w1, h1 = bboxs[0]['bbox']
    x2 = x1 + w1
    y2 = y1 + h1

    # Aplicar el filtro sepia al área del rostro
    img_face = img[y1:y2, x1:x2]
    sepia_filter = np.array([[0.272, 0.534, 0.131],
                             [0.349, 0.686, 0.168],
                             [0.393, 0.769, 0.189]])
    sepia_img = cv2.transform(img_face, sepia_filter)
    sepia_img = np.clip(sepia_img, 0, 255)

    img[y1:y2, x1:x2] = sepia_img  # Inserta la imagen con filtro sepia en la imagen original

    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(img)
    plt.axis('off')
    plt.show()

