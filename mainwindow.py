# -*- coding: utf-8 -*-

from PyQt4 import QtGui
from a import *

class MainWindow(QtGui.QDialog):

    def __init__(self,parent=None):

        QtGui.QWidget.__init__(self,parent)
        self.ui=Ui_Dialog()# Ui_Dialog为.ui产生.py文件中窗体类名，经测试类名以Ui_为前缀，加上UI窗体对象名（此处为Dialog，见上图）
        self.ui.setupUi(self)

        self.connect(self.ui.file,QtCore.SIGNAL("clicked()"),
                     self,QtCore.SLOT("choose_path()"))
        self.connect(self.ui.submit, QtCore.SIGNAL("clicked()"),
                   self, QtCore.SLOT("submit()"))

        self.connect(self.ui.load, QtCore.SIGNAL("clicked()"),
                   self, QtCore.SLOT("load_account()"))


    @QtCore.pyqtSlot()
    def choose_path(self):
        x=QtGui.QFileDialog().getExistingDirectory()
        self.ui.image_path.setText(x)

    @QtCore.pyqtSlot()
    def submit(self):
        for i in range(1,14):
            print eval('self.ui.checkBox_'+str(i)).checkState(),
        yajin=self.ui.yajin.currentText()

    @QtCore.pyqtSlot()
    def load_account(self):
        file_path=QtGui.QFileDialog().getOpenFileName()
        for line in open(file_path).readlines():
            print line
            self.ui.accounts.append(line)

if __name__ == "__main__":

    import sys

    app = QtGui.QApplication(sys.argv)
    myapp=MainWindow()
    myapp.show()
    app.exec_()