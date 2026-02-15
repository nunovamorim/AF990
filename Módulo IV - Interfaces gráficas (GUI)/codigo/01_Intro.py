# Ficheiro: 01_Intro.py

"""Exemplo simples com PyQt5."""

import sys

# 1. Importa `QApplication` e widgets necessarios
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget

# 2. Cria uma instancia QApplication
app = QApplication(sys.argv)

# 3. Cria uma instancia da aplicacao GUI
window = QWidget()
window.setWindowTitle("PyQt5 App")
window.setGeometry(100, 100, 280, 80)
window.move(60, 15)
helloMsg = QLabel("<h1>Olá Mundo!</h1>", parent=window)
helloMsg.move(60, 15)

# 4. Mostra a aplicacao GUI
window.show()

# 5. Corre a aplicacao em loop
sys.exit(app.exec_())
