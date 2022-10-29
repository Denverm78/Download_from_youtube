from PyQt6.QtWidgets import QApplication
import view

if __name__ == "__main__":
    app = QApplication([])
    window = view.MainWindow()
    window.show()
    app.exec()