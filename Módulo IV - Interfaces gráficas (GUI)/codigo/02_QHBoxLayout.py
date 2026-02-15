# Ficheiro: 02_QHBoxLayout.py

"""Exemplo de layout horizontal."""

import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QWidget

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("QHBoxLayout")
layout = QHBoxLayout()
layout.addWidget(QPushButton("Esquerda"))
layout.addWidget(QPushButton("Centro"))
layout.addWidget(QPushButton("Direita"))
window.setLayout(layout)
window.show()
sys.exit(app.exec_())
