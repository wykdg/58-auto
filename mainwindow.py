# -*- coding: utf-8 -*-

from PyQt4 import QtGui
from UI import *
from main import publish
class MainWindow(QtGui.QDialog):
    class info:
        pass
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

    def get_info(self):
        i=self.info()
        i.check_states = [eval('self.ui.checkBox_' + str(x)).checkState() for x in range(1, 14)]
        i.xiaoqu = self.ui.xiaoqu.text().__str__()
        i.huxingshi = self.ui.huxingshi.text().__str__()
        i.huxingting = self.ui.huxingting.text().__str__()
        i.huxingwei = self.ui.huxingwei.text().__str__()
        i.area = self.ui.area.text().__str__()
        i.ceng = self.ui.ceng.text().__str__()
        i.zongceng = self.ui.zongceng.text().__str__()
        i.toward = self.ui.fangxiang.currentText().__str__()
        i.zhuangxiq = self.ui.zhuangxiu.currentText().__str__()
        i.leixing = self.ui.leixing.currentText().__str__()
        i.zujin = self.ui.zujin.text().__str__()
        i.yajin = self.ui.yajin.currentText().__str__()
        i.biaoti = self.ui.biaoti.text().__str__()
        i.miaosu = self.ui.miaosu.toPlainText().__str__()
        i.lianxiren = self.ui.lianxiren.text().__str__()
        i.phone = self.ui.phone.text().__str__()

        return i



    @QtCore.pyqtSlot()
    def submit(self):
        info=self.get_info()
        publish(None,info)



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