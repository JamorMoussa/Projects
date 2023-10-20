from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from own_model import Model


class App(QMainWindow):
	filePath = ""
	def __init__(self):
		super(App, self).__init__()
		uic.loadUi("app/ui/mainwindow.ui", self)
		self.setAcceptDrops(True)


	def dragEnterEvent(self, event):
		if event.mimeData().hasImage:
			event.accept()
		else:
			event.ignore()

	def dragMoveEvent(self, event):
		if event.mimeData().hasImage:
			event.accept()
		else:
			event.ignore()

	def dropEvent(self, event):
		print("Image has been droped")
		if event.mimeData().hasImage:
			event.setDropAction(Qt.CopyAction)
			file_path = event.mimeData().urls()[0].toLocalFile()
			self.set_image(file_path)
			#text = Model().fit_image(file_path).get_text()
			#self.licencePlate.setText(text)
			event.accept()
		else:
			event.ignore()

	def set_image(self, file_path):
		self.filePath = file_path
		resized_img = QPixmap(file_path).scaled(self.ViewerWidget.width(), self.ViewerWidget.height())
		self.ImageViewer.setPixmap(resized_img)

