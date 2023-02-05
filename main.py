from mainWindowForm import MainWindow
import sys
from PyQt5.QtWidgets import QApplication

if __name__=='__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    try:
       sys.exit(app.exec_())
    except:
      print("Exiting")

            