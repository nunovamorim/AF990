# Ficheiro: 03_QVBoxLayout.py

"""Exemplo de layout vertical."""

import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("QVBoxLayout")
layout = QVBoxLayout()
layout.addWidget(QPushButton("Superior"))
layout.addWidget(QPushButton("Centro"))
layout.addWidget(QPushButton("Inferior"))
window.setLayout(layout)
window.show()
sys.exit(app.exec_())
