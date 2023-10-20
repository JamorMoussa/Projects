import ultralytics as ut
import cv2
import numpy as np
import pytesseract as ps
import sys
from config import path

model = ut.YOLO(f"{path}/own_model/model.pt")

print("Hello")

class Model:
	img_plate = None

	def fit_image(self, img_path):
		img = cv2.imread(self.imgPath)
		
		r_img = cv2.resize(img, (600, 400))

		res = model.predict(r_img)

		box = np.array(res[0].boxes.xyxy.cpu().numpy(), dtype=int)

		x, y , x1, y1 = box[0]

		self.img_plate = r_img[y:y1, x:x1]

		return self

	def get_text(self):
		return ps.image_to_string(thick_font(self.img_plate))

