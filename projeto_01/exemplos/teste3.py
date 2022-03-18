import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.Qt import *
import sys

from PyQt5. QtWidgets import *


class Widget(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.button = QPushButton("Select")
        self.button.clicked.connect(self.on_clicled)                                     # +++
        
        self.lineEdit = QLineEdit()
        self.current_text = None                                                         # +++
        
        self.combo = QComboBox(self)
        self.combo.addItems(["Select one...", "Apple", "Orange", "Banana"])
        self.combo.currentTextChanged.connect(self.on_combobox_func)                     # +++

        v_box = QVBoxLayout()
        v_box.addWidget(self.button)
        v_box.addStretch()
        v_box.addWidget(self.combo)

        h_box = QHBoxLayout(self)
        h_box.addLayout(v_box)
        h_box.addWidget(self.lineEdit)   


    def on_combobox_func(self, text):                                                    # +++
        self.current_text  = text 
        
    def on_clicled(self):                                                                # +++
        if self.current_text == "Apple":
            print("APPLE IS RED")
            self.lineEdit.setText("APPLE IS RED")
        elif self.current_text == "Orange":
            print("ORANGE IS ORANGE")
            self.lineEdit.setText("ORANGE IS ORANGE")    
        elif self.current_text == "Banana":
            print("BANANA IS YELLOW")
            self.lineEdit.setText("BANANA IS YELLOW")  
        else: self.lineEdit.setText("Select one...")             
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Widget()
    demo.show()
    sys.exit(app.exec_())