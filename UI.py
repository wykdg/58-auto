# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created: Tue May 23 11:55:44 2017
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(1454, 766)
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(40, 60, 451, 421))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.leixing = QtGui.QComboBox(self.groupBox)
        self.leixing.setGeometry(QtCore.QRect(250, 160, 91, 22))
        self.leixing.setObjectName(_fromUtf8("leixing"))
        self.leixing.addItem(_fromUtf8(""))
        self.leixing.addItem(_fromUtf8(""))
        self.leixing.addItem(_fromUtf8(""))
        self.leixing.addItem(_fromUtf8(""))
        self.leixing.addItem(_fromUtf8(""))
        self.huxingting = QtGui.QLineEdit(self.groupBox)
        self.huxingting.setGeometry(QtCore.QRect(90, 80, 41, 21))
        self.huxingting.setObjectName(_fromUtf8("huxingting"))
        self.area = QtGui.QLineEdit(self.groupBox)
        self.area.setGeometry(QtCore.QRect(240, 80, 113, 20))
        self.area.setObjectName(_fromUtf8("area"))
        self.ceng = QtGui.QLineEdit(self.groupBox)
        self.ceng.setGeometry(QtCore.QRect(20, 120, 113, 20))
        self.ceng.setObjectName(_fromUtf8("ceng"))
        self.xiaoqu = QtGui.QLineEdit(self.groupBox)
        self.xiaoqu.setGeometry(QtCore.QRect(70, 40, 331, 21))
        self.xiaoqu.setObjectName(_fromUtf8("xiaoqu"))
        self.huxingshi = QtGui.QLineEdit(self.groupBox)
        self.huxingshi.setGeometry(QtCore.QRect(20, 80, 41, 20))
        self.huxingshi.setObjectName(_fromUtf8("huxingshi"))
        self.huxingwei = QtGui.QLineEdit(self.groupBox)
        self.huxingwei.setGeometry(QtCore.QRect(160, 80, 51, 21))
        self.huxingwei.setObjectName(_fromUtf8("huxingwei"))
        self.zujin = QtGui.QLineEdit(self.groupBox)
        self.zujin.setGeometry(QtCore.QRect(20, 290, 113, 20))
        self.zujin.setObjectName(_fromUtf8("zujin"))
        self.zhuangxiu = QtGui.QComboBox(self.groupBox)
        self.zhuangxiu.setGeometry(QtCore.QRect(130, 160, 69, 22))
        self.zhuangxiu.setObjectName(_fromUtf8("zhuangxiu"))
        self.zhuangxiu.addItem(_fromUtf8(""))
        self.zhuangxiu.addItem(_fromUtf8(""))
        self.zhuangxiu.addItem(_fromUtf8(""))
        self.zhuangxiu.addItem(_fromUtf8(""))
        self.zhuangxiu.addItem(_fromUtf8(""))
        self.fangxiang = QtGui.QComboBox(self.groupBox)
        self.fangxiang.setGeometry(QtCore.QRect(20, 160, 69, 22))
        self.fangxiang.setObjectName(_fromUtf8("fangxiang"))
        self.fangxiang.addItem(_fromUtf8(""))
        self.fangxiang.addItem(_fromUtf8(""))
        self.fangxiang.addItem(_fromUtf8(""))
        self.fangxiang.addItem(_fromUtf8(""))
        self.fangxiang.addItem(_fromUtf8(""))
        self.fangxiang.addItem(_fromUtf8(""))
        self.fangxiang.addItem(_fromUtf8(""))
        self.fangxiang.addItem(_fromUtf8(""))
        self.fangxiang.addItem(_fromUtf8(""))
        self.fangxiang.addItem(_fromUtf8(""))
        self.yajin = QtGui.QComboBox(self.groupBox)
        self.yajin.setGeometry(QtCore.QRect(170, 290, 91, 22))
        self.yajin.setObjectName(_fromUtf8("yajin"))
        self.yajin.addItem(_fromUtf8(""))
        self.yajin.addItem(_fromUtf8(""))
        self.zongceng = QtGui.QLineEdit(self.groupBox)
        self.zongceng.setGeometry(QtCore.QRect(160, 120, 113, 20))
        self.zongceng.setObjectName(_fromUtf8("zongceng"))
        self.checkBox_1 = QtGui.QCheckBox(self.groupBox)
        self.checkBox_1.setGeometry(QtCore.QRect(20, 190, 41, 16))
        self.checkBox_1.setObjectName(_fromUtf8("checkBox_1"))
        self.checkBox_2 = QtGui.QCheckBox(self.groupBox)
        self.checkBox_2.setGeometry(QtCore.QRect(60, 190, 61, 16))
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.checkBox_3 = QtGui.QCheckBox(self.groupBox)
        self.checkBox_3.setGeometry(QtCore.QRect(120, 190, 61, 16))
        self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))
        self.checkBox_4 = QtGui.QCheckBox(self.groupBox)
        self.checkBox_4.setGeometry(QtCore.QRect(180, 190, 61, 16))
        self.checkBox_4.setObjectName(_fromUtf8("checkBox_4"))
        self.checkBox_5 = QtGui.QCheckBox(self.groupBox)
        self.checkBox_5.setGeometry(QtCore.QRect(240, 190, 61, 16))
        self.checkBox_5.setObjectName(_fromUtf8("checkBox_5"))
        self.checkBox_6 = QtGui.QCheckBox(self.groupBox)
        self.checkBox_6.setGeometry(QtCore.QRect(300, 190, 61, 16))
        self.checkBox_6.setObjectName(_fromUtf8("checkBox_6"))
        self.checkBox_7 = QtGui.QCheckBox(self.groupBox)
        self.checkBox_7.setGeometry(QtCore.QRect(360, 190, 61, 16))
        self.checkBox_7.setObjectName(_fromUtf8("checkBox_7"))
        self.checkBox_12 = QtGui.QCheckBox(self.groupBox)
        self.checkBox_12.setGeometry(QtCore.QRect(260, 220, 81, 16))
        self.checkBox_12.setObjectName(_fromUtf8("checkBox_12"))
        self.checkBox_11 = QtGui.QCheckBox(self.groupBox)
        self.checkBox_11.setGeometry(QtCore.QRect(190, 220, 61, 16))
        self.checkBox_11.setObjectName(_fromUtf8("checkBox_11"))
        self.checkBox_13 = QtGui.QCheckBox(self.groupBox)
        self.checkBox_13.setGeometry(QtCore.QRect(360, 220, 61, 16))
        self.checkBox_13.setObjectName(_fromUtf8("checkBox_13"))
        self.checkBox_9 = QtGui.QCheckBox(self.groupBox)
        self.checkBox_9.setGeometry(QtCore.QRect(80, 220, 61, 16))
        self.checkBox_9.setObjectName(_fromUtf8("checkBox_9"))
        self.checkBox_8 = QtGui.QCheckBox(self.groupBox)
        self.checkBox_8.setGeometry(QtCore.QRect(20, 220, 61, 16))
        self.checkBox_8.setObjectName(_fromUtf8("checkBox_8"))
        self.checkBox_10 = QtGui.QCheckBox(self.groupBox)
        self.checkBox_10.setGeometry(QtCore.QRect(130, 220, 61, 16))
        self.checkBox_10.setObjectName(_fromUtf8("checkBox_10"))
        self.image_path = QtGui.QLineEdit(self.groupBox)
        self.image_path.setGeometry(QtCore.QRect(10, 360, 321, 21))
        self.image_path.setObjectName(_fromUtf8("image_path"))
        self.file = QtGui.QPushButton(self.groupBox)
        self.file.setGeometry(QtCore.QRect(340, 360, 75, 23))
        self.file.setObjectName(_fromUtf8("file"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 40, 54, 12))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(70, 80, 54, 12))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(140, 80, 54, 12))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(220, 80, 54, 12))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(360, 80, 54, 12))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(60, 270, 54, 12))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(200, 270, 54, 12))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(280, 120, 54, 12))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(150, 120, 54, 12))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.groupBox_2 = QtGui.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(510, 40, 451, 341))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.miaosu = QtGui.QTextEdit(self.groupBox_2)
        self.miaosu.setGeometry(QtCore.QRect(70, 140, 341, 171))
        self.miaosu.setObjectName(_fromUtf8("miaosu"))
        self.biaoti = QtGui.QLineEdit(self.groupBox_2)
        self.biaoti.setGeometry(QtCore.QRect(70, 50, 341, 21))
        self.biaoti.setObjectName(_fromUtf8("biaoti"))
        self.label_12 = QtGui.QLabel(self.groupBox_2)
        self.label_12.setGeometry(QtCore.QRect(70, 20, 54, 12))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.label_13 = QtGui.QLabel(self.groupBox_2)
        self.label_13.setGeometry(QtCore.QRect(80, 110, 54, 12))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.groupBox_3 = QtGui.QGroupBox(Dialog)
        self.groupBox_3.setGeometry(QtCore.QRect(40, 490, 431, 211))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.lianxiren = QtGui.QLineEdit(self.groupBox_3)
        self.lianxiren.setGeometry(QtCore.QRect(50, 50, 271, 21))
        self.lianxiren.setObjectName(_fromUtf8("lianxiren"))
        self.phone = QtGui.QLineEdit(self.groupBox_3)
        self.phone.setGeometry(QtCore.QRect(50, 120, 271, 21))
        self.phone.setObjectName(_fromUtf8("phone"))
        self.label_10 = QtGui.QLabel(self.groupBox_3)
        self.label_10.setGeometry(QtCore.QRect(50, 30, 54, 12))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.label_11 = QtGui.QLabel(self.groupBox_3)
        self.label_11.setGeometry(QtCore.QRect(50, 90, 54, 12))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.groupBox_4 = QtGui.QGroupBox(Dialog)
        self.groupBox_4.setGeometry(QtCore.QRect(700, 400, 311, 301))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.load = QtGui.QPushButton(self.groupBox_4)
        self.load.setGeometry(QtCore.QRect(120, 250, 75, 23))
        self.load.setObjectName(_fromUtf8("load"))
        self.columnView = QtGui.QColumnView(self.groupBox_4)
        self.columnView.setGeometry(QtCore.QRect(30, 20, 256, 192))
        self.columnView.setObjectName(_fromUtf8("columnView"))
        self.submit = QtGui.QPushButton(Dialog)
        self.submit.setGeometry(QtCore.QRect(510, 630, 151, 61))
        self.submit.setObjectName(_fromUtf8("submit"))
        self.groupBox_5 = QtGui.QGroupBox(Dialog)
        self.groupBox_5.setGeometry(QtCore.QRect(1010, 40, 421, 371))
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.tableWidget = QtGui.QTableWidget(self.groupBox_5)
        self.tableWidget.setGeometry(QtCore.QRect(30, 30, 341, 251))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.groupBox.setTitle(_translate("Dialog", "GroupBox", None))
        self.leixing.setItemText(0, _translate("Dialog", "普通住宅", None))
        self.leixing.setItemText(1, _translate("Dialog", "商住两用", None))
        self.leixing.setItemText(2, _translate("Dialog", "公寓", None))
        self.leixing.setItemText(3, _translate("Dialog", "平房", None))
        self.leixing.setItemText(4, _translate("Dialog", "别墅", None))
        self.zhuangxiu.setItemText(0, _translate("Dialog", "毛坯", None))
        self.zhuangxiu.setItemText(1, _translate("Dialog", "简单装修", None))
        self.zhuangxiu.setItemText(2, _translate("Dialog", "中等装修", None))
        self.zhuangxiu.setItemText(3, _translate("Dialog", "精装修", None))
        self.zhuangxiu.setItemText(4, _translate("Dialog", "豪华装修", None))
        self.fangxiang.setItemText(0, _translate("Dialog", "东", None))
        self.fangxiang.setItemText(1, _translate("Dialog", "南", None))
        self.fangxiang.setItemText(2, _translate("Dialog", "西", None))
        self.fangxiang.setItemText(3, _translate("Dialog", "北", None))
        self.fangxiang.setItemText(4, _translate("Dialog", "南北", None))
        self.fangxiang.setItemText(5, _translate("Dialog", "东西", None))
        self.fangxiang.setItemText(6, _translate("Dialog", "东南", None))
        self.fangxiang.setItemText(7, _translate("Dialog", "西南", None))
        self.fangxiang.setItemText(8, _translate("Dialog", "东北", None))
        self.fangxiang.setItemText(9, _translate("Dialog", "西北", None))
        self.yajin.setItemText(0, _translate("Dialog", "押一付一", None))
        self.yajin.setItemText(1, _translate("Dialog", "押一付二", None))
        self.checkBox_1.setText(_translate("Dialog", "床", None))
        self.checkBox_2.setText(_translate("Dialog", "衣柜", None))
        self.checkBox_3.setText(_translate("Dialog", "沙发", None))
        self.checkBox_4.setText(_translate("Dialog", "电视", None))
        self.checkBox_5.setText(_translate("Dialog", "冰箱", None))
        self.checkBox_6.setText(_translate("Dialog", "洗衣机", None))
        self.checkBox_7.setText(_translate("Dialog", "空调", None))
        self.checkBox_12.setText(_translate("Dialog", "独立卫生间", None))
        self.checkBox_11.setText(_translate("Dialog", "可做饭", None))
        self.checkBox_13.setText(_translate("Dialog", "阳台", None))
        self.checkBox_9.setText(_translate("Dialog", "宽带", None))
        self.checkBox_8.setText(_translate("Dialog", "热水器", None))
        self.checkBox_10.setText(_translate("Dialog", "暖气", None))
        self.file.setText(_translate("Dialog", "浏览", None))
        self.label.setText(_translate("Dialog", "小区名", None))
        self.label_2.setText(_translate("Dialog", "室", None))
        self.label_3.setText(_translate("Dialog", "厅", None))
        self.label_4.setText(_translate("Dialog", "卫", None))
        self.label_5.setText(_translate("Dialog", "平方", None))
        self.label_6.setText(_translate("Dialog", "租金", None))
        self.label_7.setText(_translate("Dialog", "押金", None))
        self.label_8.setText(_translate("Dialog", "层", None))
        self.label_9.setText(_translate("Dialog", "/", None))
        self.groupBox_2.setTitle(_translate("Dialog", "GroupBox", None))
        self.label_12.setText(_translate("Dialog", "标题", None))
        self.label_13.setText(_translate("Dialog", "详细描述", None))
        self.groupBox_3.setTitle(_translate("Dialog", "GroupBox", None))
        self.label_10.setText(_translate("Dialog", "联系人", None))
        self.label_11.setText(_translate("Dialog", "电话", None))
        self.groupBox_4.setTitle(_translate("Dialog", "GroupBox", None))
        self.load.setText(_translate("Dialog", "导入", None))
        self.submit.setText(_translate("Dialog", "发布", None))
        self.groupBox_5.setTitle(_translate("Dialog", "GroupBox", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "小区名", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "账号", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "状态", None))

