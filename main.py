from PyQt5 import QtWidgets
from design import Ui_MainWindow
import sys


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.calculate_volume)

        self.actionAbout = QtWidgets.QAction("Об авторе", self)  # Создайте действие
        self.menu.addAction(self.actionAbout)  # Добавьте действие в меню
        self.actionAbout.triggered.connect(self.show_author)  # Подключите действие к методу show_author

    def calculate_volume(self):
        radius = self.spinBox.value()
        height = self.spinBox_3.value()
        volume = (1 / 3) * 3.14 * (radius ** 2) * height
        self.label.setText(f"Объем конуса: {volume}")

    def show_author(self):  # Add this method
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        msgBox.setText("Гений и создатель - Zondaxxx.")
        msgBox.setWindowTitle("About the Author")
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())




