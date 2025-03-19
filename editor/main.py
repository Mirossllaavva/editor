from PyQt5.QtWidgets import QApplication #піключення модулей
from PyQt5.QtWidgets import QMainWindow, QInputDialog, QFileDialog
from ui import Ui_MainWindow
from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
import os
from PIL import Image
from PyQt5.QtGui import QPixmap



class Widget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
def papke_obr():
    files = QFileDialog.getExistingDirectory()
   
    new_files = os.listdir(files)
    ex.ui.listWidget.addItems(new_files)
class Edit():
    def __init__(self):
        pass
    def loadImage(self, filename):
        self.filename = filename 
        self.path1 = os.path.join(files, filename)
        self.open1 = Image.open(self.path1)
    def showImage(self, path1):
        ex.ui.label.hide()
        map_image = QPixmap(path1)
        ex.ui.label.setPixmap(map_image)
image = Edit()
image.loadImage("image2.jpg")






        ex.ui.label.show()




#rozhurenia = [".bmp", ".dib", ".gif", ".ico", "".cur,"" .jpg, .jpeg, .jfif, .pjpeg, .pjp, .png, .apng, .svg, .tif, .tiff, .webp, .avif, .heif, .heic, .raw, .cr2, .nef, .orf, .sr2, .eps, .ai, .psd]









app = QApplication([]) #створення додадку
ex = Widget() #створення віджету
ex.show() #показ вікна






ex.ui.papka_btn.clicked.connect(papke_obr)






app.exec_() #закриття додатку
