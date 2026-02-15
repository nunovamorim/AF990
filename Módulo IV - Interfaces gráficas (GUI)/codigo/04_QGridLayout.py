# Ficheiro: 04_QGridLayout.py

"""Exemplo de layout em grelha."""

import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QWidget

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("QGridLayout")
layout = QGridLayout()
layout.addWidget(QPushButton("Butao (0, 0)"), 0, 0)
layout.addWidget(QPushButton("Butao (0, 1)"), 0, 1)
layout.addWidget(QPushButton("Butao (0, 2)"), 0, 2)
layout.addWidget(QPushButton("Butao (1, 0)"), 1, 0)
layout.addWidget(QPushButton("Butao (1, 1)"), 1, 1)
layout.addWidget(QPushButton("Butao (1, 2)"), 1, 2)
layout.addWidget(QPushButton("Butao (2, 0)"), 2, 0)
layout.addWidget(QPushButton("Butao (2, 1) + 2 Espaco Colunas"), 2, 1, 1, 2)
window.setLayout(layout)
window.show()
sys.exit(app.exec_())
