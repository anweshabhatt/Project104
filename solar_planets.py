import cv2
img = cv2.imread("solar-system.jpg")

cv2.putText(img,
"sun",
(20,300),
cv2.FONT_HERSHEY_COMPLEX,
0.5,
(255,255,255,255)
)

cv2.putText(img,
"Mercury",
(20,400),
cv2.FONT_HERSHEY_COMPLEX,
0.3,
(255,255,255,255)
)

cv2.putText(img,
"Venus",
(20,450),
cv2.FONT_HERSHEY_COMPLEX,
0.3,
(255,255,255,255)
)

cv2.putText(img,
"Earth",
(20,300),
cv2.FONT_HERSHEY_COMPLEX,
0.5,
(255,255,255,255)
)

cv2.putText(img,
"Mars",
(20,300),
cv2.FONT_HERSHEY_COMPLEX,
0.5,
(255,255,255,255)
)

cv2.putText(img,
"Jupitar",
(20,300),
cv2.FONT_HERSHEY_COMPLEX,
0.5,
(255,255,255,255)
)

cv2.putText(img,
"Saturn",
(20,300),
cv2.FONT_HERSHEY_COMPLEX,
0.5,
(255,255,255,255)
)

cv2.putText(img,
"Uranus",
(20,300),
cv2.FONT_HERSHEY_COMPLEX,
0.5,
(255,255,255,255)
)

cv2.putText(img,
"Naptune",
(20,300),
cv2.FONT_HERSHEY_COMPLEX,
0.5,
(255,255,255,255)
)

cv2.imshow("solar-system.jpg",img)
cv2.waitKey(0)
