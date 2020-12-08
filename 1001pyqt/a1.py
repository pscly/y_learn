# coding: utf-8
# 作者:Pscly
# 创建日期: 
# 用意：

# import sys, time
# from PyQt5 import QtWidgets
#
# app = QtWidgets.QApplication([])
# windows = QtWidgets.QWidget()
#
# windows.resize(500,500)
# windows.show()
# sys.exit(app.exec_())

import sys
from PyQt5 import QtWidgets,QtGui

app = QtWidgets.QApplication(sys.argv)
windows = QtWidgets.QWidget()
windows.resize(500,500)
windows.move(100,100)

windows.setWindowTitle('Title')
# set icon
windows.setWindowIcon(QtGui.QIcon('a1.png'))
windows.show()
sys.exit(app.exec_())
