import ultralytics as ut
import cv2
import numpy as np
import pytesseract as ps
import sys

path = sys.argv[1]

model = ut.YOLO("./model.pt")

img = cv2.imread(path)

r_img = cv2.resize(img, (600, 400))

res = model.predict(r_img)

box = np.array(res[0].boxes.xyxy.cpu().numpy(), dtype=int)

x, y , x1, y1 = box[0]

cv2.retangle(r_img, (x, y), (y, y1), (0, 0, 255), 2)

cv2.imshow("win", r_img)

croped_img = r_img[y:y1, x:x1]

text = ps.image_to_string(croped_img)

print("#"*30)
print("Licenece Plate number: ")
print(text.strip())
print("#"*30)

cv2.imshow("Windows", croped_img)

cv2.waitKey(0)
cv2.destroyAllWindows()

