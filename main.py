import cv2 as cv
import numpy as np

img = cv.imread("./qq.jpg", cv.IMREAD_COLOR)
img = cv.resize(img, (img.shape[1] // 2, img.shape[0] // 2))
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
gray = cv.medianBlur(gray, 5)

circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1.2, 100,
                          param1=100, param2=30, minRadius=75, maxRadius=100)

if circles is not None:
    circles = np.uint16(np.around(circles)).astype("uint")
    for (x, y, r) in circles[0, :]:
        cv.circle(img, (x, y), r, (0, 255, 0), 2)

        cv.putText(img, f"({x}, {y})", (x - 50, y), cv.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)

cv.imshow("circles", img)

cv.waitKey(0)
