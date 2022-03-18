from PyQt5.QtWidgets import QApplication, QWidget,QPushButton,QComboBox
from PyQt5.Qt import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtPrintSupport import *
import sys

from principal import Ui_MainWIndow

# METODO CONSTRUTOR
class Conversor(QMainWindow,Ui_MainWIndow):
    def __init__(self):
        super(Conversor,self).__init__()
        self.setupUi(self)
        
        self.pushButton.clicked.connect(self.converter_num)
        self.pushButton_2.clicked.connect(self.sair)
        self.pushButton_3.clicked.connect(self.sobre)
        self.comboBox.addItem('Binário para Decimal')
        self.comboBox.addItem('Decimal para Binário')
        self.comboBox.currentTextChanged.connect(self.combo_func)
        #self.comboBox.activated[str].connect(self.opcao_selecionada)

    def combo_func(self,text):
        self.val = text

# FUNÇÃO PARA CONVERTER EM BINÁRIO O NUMERO
    def convert_binario(self):
        try:
            caracter = int(self.lineEdit.text())
            letra = str()
            print(f'O número {caracter} em decimal é este em binário--- > {bin(caracter)[2::]}')
            if letra != caracter:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setWindowTitle('Consulta')
                msg.setText(f'Resultado: {bin(caracter)[2::]}')
                msg.exec()
        except:
            print('não foi possivel com letras!')
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle('Aviso!')
            msg.setText('Não foi possivel com letras! Favor digitar numeros!')
            msg.exec()

# FUNÇÃO PARA CONVERTER EM DECIMAL O NÚMERO
    def convert_decimal(self):
        try:
            numero = self.lineEdit.text()
            print(f'O número {numero} em binário é este em decimal ---> {int(numero,2)}')
        
            if '10' in numero or '11'in numero or '00' in numero or '01' in numero :
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setWindowTitle('Consulta')
                msg.setText(f'Resultado: {int(numero,2)}')
                msg.exec()
        except:
            print('Erro! Tente novamente mas somente com numeros 1 e 0!')
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle('Aviso')
            msg.setText('''Não foi possivel converter em decimal! 
            \nTente Novamente com números 1 e 0!''')
            msg.exec()

    def converter_num(self):
       if self.val == 'Decimal para Binário':
           self.convert_binario()
           
       else:
           self.convert_decimal()
           
       
    def sair(self):
        window.close()
        print('Saindo do programa de conversão binária... Até mais!')

    def sobre(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle('Sobre o programa')
        msg.setText('''Este é um Programa criado pelo Paulo Ricardo.
Utilize-o para transformar números em Binarios e Decimais.''')
        msg.exec()
        print('Este Programa é do Paulo Ricardo')


#EXECUTANDO A CLASSE CHAMANDO A JANELA

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Conversor()
    window.show()
    app.exec()

