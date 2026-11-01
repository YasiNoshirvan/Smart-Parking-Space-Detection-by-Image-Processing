import cv2
import numpy as np
import pickle


cap = cv2.VideoCapture('D:/Training Image Processing/Parking Project/parking5.mp4')

with open('CarParkPos', 'rb') as f:
    posList = pickle.load(f)

width, height = 57, 18


def putTextRect(img, text, pos, scale=3, thickness=3, colorT=(255, 255, 255),
                colorR=(255, 0, 255), font=cv2.FONT_HERSHEY_PLAIN,
                offset=10, border=None, colorB=(0, 255, 0)):

    ox, oy = pos
    (w, h), _ = cv2.getTextSize(text, font, scale, thickness)

    x1, y1, x2, y2 = ox - offset, oy + offset, ox + w + offset, oy - h - offset

    cv2.rectangle(img, (x1, y1), (x2, y2), colorR, cv2.FILLED)

    if border is not None:
        cv2.rectangle(img, (x1, y1), (x2, y2), colorB, border)

    cv2.putText(img, text, (ox, oy), font, scale, colorT, thickness)

    return img, [x1, y2, x2, y1]


def carparkcheck(img):
    carparkcount = 0

    for pos in posList:
        x, y = pos
        print(pos)

        carpark_img = img[y:y+height, x:x+width]
        countwhite = cv2.countNonZero(carpark_img)

        if countwhite < 100:
            carparkcount += 1
            color = (0, 255, 0)
        else:
            color = (0, 0, 255)

        # cv2.imshow("car" , carpark_img)
        # if cv2.waitKey(25) & 0xFF == ord ('q'):
        #    break

        cv2.rectangle(frame, pos, (pos[0] + width, pos[1] + height), color, 4)

        putTextRect(frame, str(countwhite), (x, y + height - 3), scale=1,
                    thickness=2, offset=0, colorR=color)

    putTextRect(frame, f'Free: {carparkcount}/{len(posList)}', (100, 50), scale=3,
                thickness=5, offset=20, colorR=(0, 200, 0))



while True:
    ret, frame = cap.read()

    if not ret:
        break

    imgGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (3, 3), 1)

    imgThreshold = cv2.adaptiveThreshold(imgBlur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV, 25, 16)

    imgMedian = cv2.medianBlur(imgThreshold, 5)

    carparkcheck(imgMedian)

    cv2.imshow("Image", frame)
    # cv2.imshow("imgThreshold", imgThreshold)
    # cv2.imshow("imgMedian", imgMedian)

    if cv2.waitKey(25) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()