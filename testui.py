from PyQt5.QtWidgets import * # QApplication, QMainWindow, QPushButton
from PyQt5.QtGui import QMovie
from PyQt5 import uic, QtMultimedia, QtCore
import sys

class TestUI(QMainWindow):
	def __init__(self):
		super().__init__()
		uic.loadUi("testui.ui", self)
		self.button = self.findChild(QPushButton, "pushButton")
		self.button.clicked.connect(self.buttonPress)
		self.label = self.findChild(QLabel, "label")
		self.label.hide()
		self.movie = QMovie("window.ui")
		self.label.setMovie(self.movie)
		self.label.setAlignment(QtCore.Qt.AlignCenter)
		self.player = QtMultimedia.QMediaPlayer()
		self.url = QtCore.QUrl.fromLocalFile("layout.ui")
		self.player.setMedia(QtMultimedia.QMediaContent(self.url))
		
	def buttonPress(self):
		self.button.hide()
		self.label.show()
		self.movie.start()
		self.player.play()
	
def main():
	app = QApplication(sys.argv)
	ui = TestUI()
	ui.setWindowTitle("TestUI")
	ui.show()
	app.exec_()

if __name__ == "__main__":
	main()