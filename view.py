from PyQt6.QtWidgets import QMainWindow, QLabel, QPushButton, QLineEdit, QProgressBar
import controller


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
       
        self.setWindowTitle("Скачивание видео с YouTube")
        self.resize(400, 300)
        self.label = QLabel("Вставьте ссылку на видео:", self) 
        self.label.setGeometry(20, 10, 280, 25) 
        self.input = QLineEdit(self)
        self.input.setGeometry(20, 40, 280, 25)
        self.label_1 = QLabel('', self) 
        self.label_1.setGeometry(20, 70, 280, 25) 
        self.label = QLabel('Для начала скачивания нажмите кнопку "Старт"', self) 
        self.label.setGeometry(20, 100, 280, 30) 
        self.button = QPushButton("Старт", self) 
        self.button.move(20, 140)
        self.button.pressed.connect(self.initDownload)
        self.progressBar = QProgressBar(self)
        self.progressBar.setGeometry(20, 200, 300, 25)
    
    def initDownload(self):
        myLink = self.input.text()
        self.label.setText("Идет скачивание файла . . .")
        self.button.setEnabled(False)
        self.input.clear()
        nameFile = controller.getNameFile(myLink)
        if len(nameFile) < 30: 
            self.label_1.setText(f"Найден файл: {nameFile}")
        else:
            self.label_1.setText(f"Найден файл: {nameFile[:30]}. . .")
        print(nameFile)
        self.downloader = controller.Downloader(myLink, nameFile)
        self.downloader.setCurrentProgress.connect(self.progressBar.setValue)
        self.downloader.succeeded.connect(self.downloadSucceeded)
        self.downloader.finished.connect(self.downloadFinished)
        self.downloader.start()

    def downloadSucceeded(self):
        self.progressBar.setValue(self.progressBar.maximum())
        self.label.setText("Скачивание завершено.\nФайл находится в папке с программой.")
    
    def downloadFinished(self):
        self.button.setEnabled(True)
        del self.downloader


