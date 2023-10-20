from app import App
from PyQt5.QtWidgets import QApplication
import sys


if __name__ == '__main__':
	app = QApplication(sys.argv)

	app_win = App()

	app_win.show()

	sys.exit(app.exec())
