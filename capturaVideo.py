import cv2
import numpy as np
import pywhatkit as rep


#captura = cv2.VideoCapture('VideoUPIIZ.mp4')
captura = cv2.VideoCapture(0)

while True:
    ret, frame = captura.read()
    cv2.imshow('Salida', frame)
    k=cv2.waitKey(10)&0xFF
    if k == 27:
        break
captura.release()
cv2.destroyAllWindows()