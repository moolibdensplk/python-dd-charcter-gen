import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from internal.app_main_window import DDMainMenuWindow

app = QtWidgets.QApplication(sys.argv)
main_window = DDMainMenuWindow()
main_window.show()

sys.exit(app.exec_())
