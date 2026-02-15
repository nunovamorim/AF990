# Ficheiro: 08_Funcoes.py

"""Sinais e Slots."""

import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget


def saudacao():
    """Funcao Slot."""
    if msg.text():
        msg.setText("")
    else:
        msg.setText("Olá Mundo!")


app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Sinais e Slots")
layout = QVBoxLayout()

btn = QPushButton("Saudacao")
btn.clicked.connect(saudacao)  # Faz a linkagem à funcao saudacao()

layout.addWidget(btn)
msg = QLabel("")
layout.addWidget(msg)
window.setLayout(layout)
window.show()
sys.exit(app.exec_())
