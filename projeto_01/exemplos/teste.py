from PyQt5.QtWidgets import(QWidget,QLabel,QHBoxLayout,
QComboBox,QApplication)
import sys

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()
    
    def initUi(self):
        hbox = QHBoxLayout()

        self.lbl = QLabel('Ubuntu',self)

        combo = QComboBox(self)
        combo.addItem('Ubuntu')
        combo.addItem('Xubuntu')
        combo.addItem('Fedora')
        combo.addItem('Arch')
        combo.addItem('Gentoo')

        combo.activated[str].connect(self.onActivated)

        hbox.addWidget(combo)
        hbox.setSpacing(20)

        hbox.addWidget(self.lbl)
        self.setContentsMargins(20,20,20,20)
        self.setLayout(hbox)

        self.move(300,300)
        self.setWindowTitle('QComboBox')
        self.show()

    def onActivated(self,text):
        self.lbl.setText(text)
        self.lbl.adjustSize()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
