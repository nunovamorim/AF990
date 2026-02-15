# Ficheiro: 07_QMainWindow.py

"""Aplicacao com janela principal da aplicacao."""

import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QStatusBar
from PyQt5.QtWidgets import QToolBar


class Window(QMainWindow):
    """Janela Principal."""

    def __init__(self, parent=None):
        """Inicializador."""
        super().__init__(parent)
        self.setWindowTitle("Janela QMainWindow")
        self.setCentralWidget(QLabel("Este é o Widget Central"))
        self._createMenu()
        self._createToolBar()
        self._createStatusBar()

    def _createMenu(self):
        self.menu = self.menuBar().addMenu("&Menu")
        self.menu.addAction("&Sair", self.close)

    def _createToolBar(self):
        tools = QToolBar()
        self.addToolBar(tools)
        tools.addAction("Sair", self.close)

    def _createStatusBar(self):
        status = QStatusBar()
        status.showMessage("Esta é a barra de estado")
        self.setStatusBar(status)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
