from PyQt5.QtWidgets import QApplication #піключення модулей
from PyQt5.QtWidgets import QMainWindow, QInputDialog, QFileDialog
from ui import Ui_MainWindow
from PyQt5.QtCore import QUrl, Qt
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
import os
from PIL import Image, ImageFilter
from PyQt5.QtGui import QPixmap

files = 0



class Widget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
def papke_obr():
    global files
    files = QFileDialog.getExistingDirectory() #путь к папке
   
    new_files = os.listdir(files) #все файлы
    result_files = []
    for file in new_files:
        for roz in rozhurenia:
            if file.endswith(roz):
                result_files.append(file)

    #print(new_files)
    ex.ui.listWidget.addItems(result_files)
class Edit():
    def __init__(self):
        self.save_folder = "\path_obrob_photo"
        
    def loadImage(self, filename):
        global files
        self.filename = filename 
        self.path1 = os.path.join(files, filename)
        self.open1 = Image.open(self.path1) #картинка как объект 
        # self.open1.show()
    def showImage(self, path1):
        ex.ui.label.hide()
        map_image = QPixmap(path1)
        print(path1)
        widght,high = ex.ui.label.width(), ex.ui.label.height()
        map_image = map_image.scaled(widght,high, Qt.KeepAspectRatio)
        ex.ui.label.setPixmap(map_image)
        ex.ui.label.show()
    def black(self):
        self.open1 = self.open1.convert("L")
        self.save_im() #буд. метод 
        vrem_path = os.path.join(files, self.save_folder, self.filename)
        self.showImage(vrem_path)
    def save_im(self):
        path = os.path.join(files,self.save_folder)
        if not(os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)
        image_path = os.path.join(path, self.filename)
        self.open1.save(image_path)
    def mirror(self):
        self.open1 = self.open1.transpose(Image.FLIP_LEFT_RIGHT)
        self.save_im()
        vrem_path2 = os.path.join(files, self.save_folder,self.filename)
        self.showImage(vrem_path2)
    def left(self):
        self.open1 = self.open1.rotate(10)
        self.save_im()
        vrem_path3 = os.path.join(files, self.save_folder, self.filename)
        self.showImage(vrem_path3)
    def right(self):
        self.open1 = self.open1.rotate(-10)
        self.save_im()
        vrem_path4 = os.path.join(files, self.save_folder, self.filename)
        self.showImage(vrem_path4)
    def blur(self):
        self.open1 = self.open1.filter(ImageFilter.BLUR)
        self.save_im()
        vrem_path5 = os.path.join(files, self.save_folder, self.filename)
        self.showImage(vrem_path5)
    def finish_save(self):
        window = QFileDialog.getExistingDirectory()
        path = os.path.join(window,"finish_photo.png")
        self.open1.save(path)
       

        
        
        
        

image1 = Edit()
def image():
    global files
    if ex.ui.listWidget.currentRow() >= 0:
        name_im = ex.ui.listWidget.currentItem().text()
        image1.loadImage(name_im)
        #path_im = os.path.join(files,name_im)
        
        image1.showImage(image1.path1)

        
     





rozhurenia = [
    ".bmp", ".dib", ".gif", ".ico", ".cur",
    ".jpg", ".jpeg", ".jfif", ".pjpeg", ".pjp",
    ".png", ".apng", ".svg", ".tif", ".tiff",
    ".webp", ".heif", ".heic", ".raw",
    ".cr2", ".nef", ".orf", ".sr2", ".eps",
    ".ai", ".psd"
]








app = QApplication([]) #створення додадку
ex = Widget() #створення віджету
ex.show() #показ вікна






ex.ui.papka_btn.clicked.connect(papke_obr)
ex.ui.listWidget.currentRowChanged.connect(image)
ex.ui.cb_btn.clicked.connect(image1.black)
ex.ui.window_btn.clicked.connect(image1.mirror)
ex.ui.right_btn.clicked.connect(image1.left)
ex.ui.left_btn.clicked.connect(image1.right)
ex.ui.riz_btn.clicked.connect(image1.blur)
ex.ui.save_btn.clicked.connect(image1.finish_save)






app.exec_() #закриття додатку
