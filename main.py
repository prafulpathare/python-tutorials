import sys
from PyQt5.QtWidgets import *

def window():
    app = QApplication([])
    window = QWidget()
    layout = QFormLayout()
    layout.addWidget(QLabel('hello'))
    layout.addWidget(QTextEdit('username'))
    layout.addWidget(QPushButton('Top'))
    layout.addWidget(QPushButton('Bottom').setStyleSheet({'margin': 10}))
    window.setLayout(layout)
    window.resize(300,600)
    window.show()
    app.exec_()

#    w = QtGui.QWidget()
#    b = QtGui.QLabel(w)
#    b.setText("Hello World!")
#    w.setGeometry(100,100,200,50)
#    b.move(50,20)
#    w.setWindowTitle("PyQt")
#    w.show()
#    sys.exit(app.exec_())
	
if __name__ == '__main__':
   window()
