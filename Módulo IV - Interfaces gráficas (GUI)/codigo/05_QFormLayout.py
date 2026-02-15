# Ficheiro: 05_QFormLayout.py

"""Exemplo de layout para formulario."""

import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QFormLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QWidget

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("QFormLayout")
layout = QFormLayout()
layout.addRow("Nome:", QLineEdit())
layout.addRow("Idade:", QLineEdit())
layout.addRow("Profissao:", QLineEdit())
layout.addRow("Hobbies:", QLineEdit())
window.setLayout(layout)
window.show()
sys.exit(app.exec_())
