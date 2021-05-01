# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Fri Dec 21 18:23:30 2012
#      by: PyQt4 UI code generator 4.9.6
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(612, 645)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(_fromUtf8(""))
        self.centralWidget = QtGui.QWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralWidget.sizePolicy().hasHeightForWidth())
        self.centralWidget.setSizePolicy(sizePolicy)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.frame = QtGui.QFrame(self.centralWidget)
        self.frame.setGeometry(QtCore.QRect(40, 10, 531, 561))
        self.frame.setStyleSheet(_fromUtf8("border-image:url(:/new/prefix1/chessboard.png)"))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setLineWidth(10)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.layoutWidget = QtGui.QWidget(self.centralWidget)
        self.layoutWidget.setGeometry(QtCore.QRect(50, 290, 511, 281))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayout_down = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout_down.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.gridLayout_down.setMargin(0)
        self.gridLayout_down.setObjectName(_fromUtf8("gridLayout_down"))
        self.pushButton_82 = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_82.setMinimumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_82.setFont(font)
        self.pushButton_82.setText(_fromUtf8(""))
        self.pushButton_82.setObjectName(_fromUtf8("pushButton_82"))
        self.gridLayout_down.addWidget(self.pushButton_82, 3, 1, 1, 1)
        self.pushButton_94 = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_94.setMinimumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_94.setFont(font)
        self.pushButton_94.setStyleSheet(_fromUtf8("QPushButton{\n"
"background:qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.56892, fx:0.5, fy:0.35259, stop:0.0397727 rgba(255, 211, 224, 255), stop:0.573864 rgba(255, 168, 88, 255), stop:0.653409 rgba(255, 0, 4, 255), stop:0.681818 rgba(255, 255, 255, 255), stop:0.767045 rgba(48, 26, 13, 255), stop:0.920455 rgba(255, 247, 250, 255));\n"
"border-radius:20px;\n"
"color:red;\n"
"}\n"
"QPushButton:hover{\n"
"background: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.56892, fx:0.5, fy:0.35259, stop:0.0397727 rgba(255, 211, 224, 255), stop:0.573864 rgba(255, 228, 17, 255), stop:0.653409 rgba(255, 4, 0, 255), stop:0.681818 rgba(255, 255, 255, 255), stop:0.767045 rgba(48, 26, 13, 255), stop:0.920455 rgba(255, 247, 250, 255));\n"
"border-radius:20px;\n"
"}\n"
"QPushButton:pressed{\n"
"background:qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.56892, fx:0.5, fy:0.35259, stop:0.0397727 rgba(255, 211, 224, 255), stop:0.573864 rgba(128, 1, 22, 255), stop:0.653409 rgba(255, 4, 0, 255), stop:0.681818 rgba(255, 255, 255, 255), stop:0.767045 rgba(48, 26, 13, 255), stop:0.920455 rgba(255, 247, 250, 255));\n"
"border-radius:20px\n"
"}"))
        self.pushButton_94.setObjectName(_fromUtf8("pushButton_94"))
        self.gridLayout_down.addWidget(self.pushButton_94, 4, 3, 1, 1)
        self.pushButton_78 = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_78.setMinimumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_78.setFont(font)
        self.pushButton_78.setStyleSheet(_fromUtf8("QPushButton{\n"
"background:qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.56892, fx:0.5, fy:0.35259, stop:0.0397727 rgba(255, 211, 224, 255), stop:0.573864 rgba(255, 168, 88, 255), stop:0.653409 rgba(255, 0, 4, 255), stop:0.681818 rgba(255, 255, 255, 255), stop:0.767045 rgba(48, 26, 13, 255), stop:0.920455 rgba(255, 247, 250, 255));\n"
"border-radius:20px;\n"
"color:red;\n"
"}\n"
"QPushButton:hover{\n"
"background: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.56892, fx:0.5, fy:0.35259, stop:0.0397727 rgba(255, 211, 224, 255), stop:0.573864 rgba(255, 228, 17, 255), stop:0.653409 rgba(255, 4, 0, 255), stop:0.681818 rgba(255, 255, 255, 255), stop:0.767045 rgba(48, 26, 13, 255), stop:0.920455 rgba(255, 247, 250, 255));\n"
"border-radius:20px;\n"
"}\n"
"QPushButton:pressed{\n"
"background:qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.56892, fx:0.5, fy:0.35259, stop:0.0397727 rgba(255, 211, 224, 255), stop:0.573864 rgba(128, 1, 22, 255), stop:0.653409 rgba(255, 4, 0, 255), stop:0.681818 rgba(255, 255, 255, 255), stop:0.767045 rgba(48, 26, 13, 255), stop:0.920455 rgba(255, 247, 250, 255));\n"
"border-radius:20px\n"
"}"))
        self.pushButton_78.setObjectName(_fromUtf8("pushButton_78"))
        self.gridLayout_down.addWidget(self.pushButton_78, 2, 7, 1, 1)
        self.pushButton_84 = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_84.setMinimumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_84.setFont(font)
        self.pushButton_84.setText(_fromUtf8(""))
        self.pushButton_84.setObjectName(_fromUtf8("pushButton_84"))
        self.gridLayout_down.addWidget(self.pushButton_84, 3, 3, 1, 1)
        self.pushButton_61 = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_61.setMinimumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_61.setFont(font)
        self.pushButton_61.setStyleSheet(_fromUtf8("QPushButton{\n"
"background:qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.56892, fx:0.5, fy:0.35259, stop:0.0397727 rgba(255, 211, 224, 255), stop:0.573864 rgba(255, 168, 88, 255), stop:0.653409 rgba(255, 0, 4, 255), stop:0.681818 rgba(255, 255, 255, 255), stop:0.767045 rgba(48, 26, 13, 255), stop:0.920455 rgba(255, 247, 250, 255));\n"
"border-radius:20px;\n"
"color:red;\n"
"}\n"
"QPushButton:hover{\n"
"background: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.56892, fx:0.5, fy:0.35259, stop:0.0397727 rgba(255, 211, 224, 255), stop:0.573864 rgba(255, 228, 17, 255), stop:0.653409 rgba(255, 4, 0, 255), stop:0.681818 rgba(255, 255, 255, 255), stop:0.767045 rgba(48, 26, 13, 255), stop:0.920455 rgba(255, 247, 250, 255));\n"
"border-radius:20px;\n"
"}\n"
"QPushButton:pressed{\n"
"background:qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.56892, fx:0.5, fy:0.35259, stop:0.0397727 rgba(255, 211, 224, 255), stop:0.573864 rgba(128, 1, 22, 255), stop:0.653409 rgba(255, 4, 0, 255), stop:0.681818 rgba(255, 255, 255, 255), stop:0.767045 rgba(48, 26, 13, 255), stop:0.920455 rgba(255, 247, 250, 255));\n"
"border-radius:20px\n"
"}"))
        self.pushButton_61.setObjectName(_fromUtf8("pushButton_61"))
        self.gridLayout_down.addWidget(self.pushButton_61, 1, 0, 1, 1)
        self.pushButton_83 = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_83.setMinimumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_83.setFont(font)
        self.pushButton_83.setText(_fromUtf8(""))
        self.pushButton_83.setObjectName(_fromUtf8("pushButton_83"))
        self.gridLayout_down.addWidget(self.pushButton_83, 3, 2, 1, 1)
        self.pushButton_85 = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_85.setMinimumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_85.setFont(font)
        self.pushButton_85.setText(_fromUtf8(""))
        self.pushButton_85.setObjectName(_fromUtf8("pushButton_85"))
        self.gridLayout_down.addWidget(self.pushButton_85, 3, 4, 1, 1)
        self.pushButton_77 = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_77.setMinimumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_77.setFont(font)
        self.pushButton_77.setText(_fromUtf8(""))
        self.pushButton_77.setObjectName(_fromUtf8("pushButton_77"))
        self.gridLayout_down.addWidget(self.pushButton_77, 2, 6, 1, 1)
        self.pushButton_93 = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_93.setMinimumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_93.setFont(font)
        self.pushButton_93.setStyleSheet(_fromUtf8("QPushButton{\n"
"background:qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.56892, fx:0.5, fy:0.35259, stop:0.0397727 rgba(255, 211, 224, 255), stop:0.573864 rgba(255, 168, 88, 255), stop:0.653409 rgba(255, 0, 4, 255), stop:0.681818 rgba(255, 255, 255, 255), stop:0.767045 rgba(48, 26, 13, 255), stop:0.920455 rgba(255, 247, 250, 255));\n"
"border-radius:20px;\n"
"color:red;\n"
"}\n"
"QPushButton:hover{\n"
"background: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.56892, fx:0.5, fy:0.35259, stop:0.0397727 rgba(255, 211, 224, 255), stop:0.573864 rgba(255, 228, 17, 255), stop:0.653409 rgba(255, 4, 0, 255), stop:0.681818 rgba(255, 255, 255, 255), stop:0.767045 rgba(48, 26, 13, 255), stop:0.920455 rgba(255, 247, 250, 255));\n"
"border-radius:20px;\n"
"}\n"
"QPushButton:pressed{\n"
"background:qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.56892, fx:0.5, fy:0.35259, stop:0.0397727 rgba(255, 211, 224, 255), stop:0.573864 rgba(128, 1, 22, 255), stop:0.653409 rgba(255, 4, 0, 255), stop:0.681818 rgba(255, 255, 255, 255), stop:0.767045 rgba(48, 26, 13, 255), stop:0.920455 rgba(255, 247, 250, 255));\n"
"border-radius:20px\n"
"}"))
        self.pushButton_93.setObjectName(_fromUtf8("pushButton_93"))
        self.gridLayout_down.addWidget(self.pushButton_93, 4, 2, 1, 1)
        self.pushButton_54 = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_54.setMinimumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_54.setFont(font)
        self.pushButton_54.setText(_fromUtf8(""))
        self.pushButton_54.setObjectName(_fromUtf8("pushButton_54"))
        self.gridLayout_down.addWidget(self.pushButton_54, 0, 3, 1, 1)
        self.pushButton_73 = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_73.setMinimumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_73.setFont(font)
        self.pushButton_73.setText(_fromUtf8(""))
        self.pushButton_73.setObjectName(_fromUtf8("pushButton_73"))
        self.gridLayout_down.addWidget(self.pushButton_73, 2, 2, 1, 1)
        self.pushButton_92 = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_92.setMinimumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_92.setFont(font)
        self.pushButton_92.setStyleSheet(_fromUtf8("QPushButton{\n"
"background:qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.56892, fx:0.5, fy:0.35259, stop:0.0397727 rgba(255, 211, 224, 255), stop:0.573864 rgba(255, 168, 88, 255), stop:0.653409 rgba(255, 0, 4, 255), stop:0.681818 rgba(255, 255, 255, 255), stop:0.767045 rgba(48, 26, 13, 255), stop:0.920455 rgba(255, 247, 250, 255));\n"
"border-radius:20px;\n"
"color:red;\n"
"}\n"
"QPushButton:hover{\n"
"background: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.56892, fx:0.5, fy:0.35259, stop:0.0397727 rgba(255, 211, 224, 255), stop:0.573864 rgba(255, 228, 17, 255), stop:0.653409 rgba(255, 4, 0, 255), stop:0.681818 rgba(255, 255, 255, 255), stop:0.767045 rgba(48, 26, 13, 255), stop:0.920455 rgba(255, 247, 250, 255));\n"
"border-radius:20px;\n"
"}\n"
"QPushButton:pressed{\n"
"background:qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.56892, fx:0.5, fy:0.35259, stop:0.0397727 rgba(255, 211, 224, 255), stop:0.573864 rgba(128, 1, 22, 255), stop:0.653409 rgba(255, 4, 0, 255), stop:0.681818 rgba(255, 255, 255, 255), stop:0.767045 rgba(48, 26, 13, 255), stop:0.920455 rgba(255, 247, 250, 255));\n"
"border-radius:20px\n"
"}"))
        self.pushButton_92.setObjectName(_fromUtf8("pushButton_92"))
        self.gridLayout_down.addWidget(self.pushButton_92, 4, 1, 1, 1)
        self.pushButton_64 = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_64.setEnabled(True)
        self.pushButton_64.setMinimumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_64.setFont(font)
        self.pushButton_64.setText(_fromUtf8(""))
        self.pushButton_64.setCheckable(False)
        self.pushButton_64.setObjectName(_fromUtf8("pushButton_64"))
        self.gridLayout_down.addWidget(self.pushButton_64, 1, 3, 1, 1)
        self.pushButton_76 = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_76.setMinimumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_76.setFont(font)
        self.pushButton_76.setText(_fromUtf8(""))
        self.pushButton_76.setObjectName(_fromUtf8("pushButton_76"))
        self.gridLayout_down.addWidget(self.pushButton_76, 2, 5, 1, 1)
        self.pushButton_74 = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_74.setMinimumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_74.setFont(font)
        self.pushButton_74.setText(_fromUtf8(""))
        self.pushButton_74.setObjectName(_fromUtf8("pushButton_74"))
        self.gridLayout_down.addWidget(self.pushButton_74, 2, 3, 1, 1)
        self.pushButton_57 = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_57.setMinimumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_57.setFont(font)
        self.pushButton_57.setText(_fromUtf8(""))
        self.pushButton_57.setObjectName(_fromUtf8("pushButton_57"))
        self.gridLayout_down.addWidget(self.pushButton_57, 0, 6, 1, 1)
        self.pushButton_91 = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_91.setMinimumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_91.setFont(font)
        self.pushButton_91.setStyleSheet(_fromUtf8("QPushButton{\n"
"background:qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.56892, fx:0.5, fy:0.35259, stop:0.0397727 rgba(255, 211, 224, 255), stop:0.573864 rgba(255, 168, 88, 255), stop:0.653409 rgba(255, 0, 4, 255), stop:0.681818 rgba(255, 255, 255, 255), stop:0.767045 rgba(48, 26, 13, 255), stop:0.920455 rgba(255, 247, 250, 255));\n"
"border-radius:20px;\n"
"color:red;\n"
"}\n"
"QPushButton:hover{\n"
"background: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.56892, fx:0.5, fy:0.35259, stop:0.0397727 rgba(255, 211, 224, 255), stop:0.573864 rgba(255, 228, 17, 255), stop:0.653409 rgba(255, 4, 0, 255), stop:0.681818 rgba(255, 255, 255, 255), stop:0.767045 rgba(48, 26, 13, 255), stop:0.920455 rgba(255, 247, 250, 255));\n"
"border-radius:20px;\n"
"}\n"
"QPushButton:pressed{\n"
"background:qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.56892, fx:0.5, fy:0.35259, stop:0.0397727 rgba(255, 211, 224, 255), stop:0.573864 rgba(128, 1, 22, 255), stop:0.653409 rgba(255, 4, 0, 255), stop:0.681818 rgba(255, 255, 255, 255), stop:0.767045 rgba(48, 26, 13, 255), stop:0.920455 rgba(255, 247, 250, 255));\n"
"border-radius:20px\n"
"}"))
        self.pushButton_91.setObjectName(_fromUtf8("pushButton_91"))
        self.gridLayout_down.addWidget(self.pushButton_91, 4, 0, 1, 1)
        self.pushButton_99 = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_99.setMinimumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_99.setFont(font)
        self.pushButton_99.setStyleSheet(_fromUtf8("QPushButton{\n"
"background:qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.56892, fx:0.5, fy:0.35259, stop:0.0397727 rgba(255, 211, 224, 255), stop:0.573864 rgba(255, 168, 88, 255), stop:0.653409 rgba(255, 0, 4, 255), stop:0.681818 rgba(255, 255, 255, 255), stop:0.767045 rgba(48, 26, 13, 255), stop:0.920455 rgba(255, 247, 250, 255));\n"
"border-radius:20px;\n"
"color:red;\n"
"}\n"
"QPushButton:hover{\n"
"background: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.56892, fx:0.5, fy:0.35259, stop:0.0397727 rgba(255, 211, 224, 255), stop:0.573864 rgba(255, 228, 17, 255), stop:0.653409 rgba(255, 4, 0, 255), stop:0.681818 rgba(255, 255, 255, 255), stop:0.767045 rgba(48, 26, 13, 255), stop:0.920455 rgba(255, 247, 250, 255));\n"
"border-radius:20px;\n"
"}\n"
"QPushButton:pressed{\n"
"background:qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.56892, fx:0.5, fy:0.35259, stop:0.0397727 rgba(255, 211, 224, 255), stop:0.573864 rgba(128, 1, 22, 255), stop:0.653409 rgba(255, 4, 0, 255), stop:0.681818 rgba(255, 255, 255, 255), stop:0.767045 rgba(48, 26, 13, 255), stop:0.920455 rgba(255, 247, 250, 255));\n"
"border-radius:20px\n"
"}"))
        self.pushButton_99.setObjectName(_fromUtf8("pushButton_99"))
        self.gridLayout_down.addWidget(self.pushButton_99, 4, 8, 1, 1)
        self.pushButton_68 = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_68.setMinimumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_68.setFont(font)
        self.pushButton_68.setText(_fromUtf8(""))
        self.pushButton_68.setObjectName(_fromUtf8("pushButton_68"))
        self.gridLayout_down.addWidget(self.pushButton_68, 1, 7, 1, 1)
        self.pushButton_87 = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_87.setMinimumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_87.setFont(font)
        self.pushButton_87.setText(_fromUtf8(""))
        self.pushButton_87.setObjectName(_fromUtf8("pushButton_87"))
        self.gridLayout_down.addWidget(self.pushButton_87, 3, 6, 1, 1)
        self.pushButton_81 = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_81.setMinimumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_81.setFont(font)
        self.pushButton_81.setText(_fromUtf8(""))
        self.pushButton_81.setObjectName(_fromUtf8("pushButton_81"))
        self.gridLayout_down.addWidget(self.pushButton_81, 3, 0, 1, 1)
        self.pushButton_51 = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_51.setMinimumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_51.setFont(font)
        self.pushButton_51.setStyleSheet(_fromUtf8("selection-color:rgb(255, 255, 0);selection-background-color:rgb(255, 255, 0)"))
        self.pushButton_51.setText(_fromUtf8(""))
        self.pushButton_51.setObjectName(_fromUtf8("pushButton_51"))
        self.gridLayout_down.addWidget(self.pushButton_51, 0, 0, 1, 1)
        self.pushButton_86 = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_86.setMinimumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_86.setFont(font)
        self.pushButton_86.setText(_fromUtf8(""))
        self.pushButton_86.setObjectName(_fromUtf8("pushButton_86"))
        self.gridLayout_down.addWidget(self.pushButton_86, 3, 5, 1, 1)
        self.pushButton_66 = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_66.setMinimumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_66.setFont(font)
        self.pushButton_66.setText(_fromUtf8(""))
        self.pushButton_66.setObjectName(_fromUtf8("pushButton_66"))
        self.gridLayout_down.addWidget(self.pushButton_66, 1, 5, 1, 1)
        self.pushButton_75 = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_75.setMinimumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_75.setFont(font)
        self.pushButton_75.setText(_fromUtf8(""))
        self.pushButton_75.setObjectName(_fromUtf8("pushButton_75"))
        self.gridLayout_down.addWidget(self.pushButton_75, 2, 4, 1, 1)
        self.pushButton_53 = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_53.setMinimumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_53.setFont(font)
        self.pushButton_53.setText(_fromUtf8(""))
        self.pushButton_53.setObjectName(_fromUtf8("pushButton_53"))
        self.gridLayout_down.addWidget(self.pushButton_53, 0, 2, 1, 1)
        self.pushButton_71 = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_71.setMinimumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_71.setFont(font)
        self.pushButton_71.setText(_fromUtf8(""))
        self.pushButton_71.setObjectName(_fromUtf8("pushButton_71"))
        self.gridLayout_down.addWidget(self.pushButton_71, 2, 0, 1, 1)
        self.pushButton_97 = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_97.setMinimumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_97.setFont(font)
        self.pushButton_97.setStyleSheet(_fromUtf8("QPushButton{\n"
"background:qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.56892, fx:0.5, fy:0.35259, stop:0.0397727 rgba(255, 211, 224, 255), stop:0.573864 rgba(255, 168, 88, 255), stop:0.653409 rgba(255, 0, 4, 255), stop:0.681818 rgba(255, 255, 255, 255), stop:0.767045 rgba(48, 26, 13, 255), stop:0.920455 rgba(255, 247, 250, 255));\n"
"border-radius:20px;\n"
"color:red;\n"
"}\n"
"QPushButton:hover{\n"
"background: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.56892, fx:0.5, fy:0.35259, stop:0.0397727 rgba(255, 211, 224, 255), stop:0.573864 rgba(255, 228, 17, 255), stop:0.653409 rgba(255, 4, 0, 255), stop:0.681818 rgba(255, 255, 255, 255), stop:0.767045 rgba(48, 26, 13, 255), stop:0.920455 rgba(255, 247, 250, 255));\n"
"border-radius:20px;\n"
"}\n"
"QPushButton:pressed{\n"
"background:qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.56892, fx:0.5, fy:0.35259, stop:0.0397727 rgba(255, 211, 224, 255), stop:0.573864 rgba(128, 1, 22, 255), stop:0.653409 rgba(255, 4, 0, 255), stop:0.681818 rgba(255, 255, 255, 255), stop:0.767045 rgba(48, 26, 13, 255), stop:0.920455 rgba(255, 247, 250, 255));\n"
"border-radius:20px\n"
"}"))
        self.pushButton_97.setObjectName(_fromUtf8("pushButton_97"))
        self.gridLayout_down.addWidget(self.pushButton_97, 4, 6, 1, 1)
        self.pushButton_59 = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_59.setMinimumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_59.setFont(font)
        self.pushButton_59.setText(_fromUtf8(""))
        self.pushButton_59.setObjectName(_fromUtf8("pushButton_59"))
        self.gridLayout_down.addWidget(self.pushButton_59, 0, 8, 1, 1)
        self.pushButton_58 = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_58.setMinimumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_58.setFont(font)
        self.pushButton_58.setText(_fromUtf8(""))
        self.pushButton_58.setObjectName(_fromUtf8("pushButton_58"))
        self.gridLayout_down.addWidget(self.pushButton_58, 0, 7, 1, 1)
        self.pushButton_98 = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_98.setMinimumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_98.setFont(font)
        self.pushButton_98.setStyleSheet(_fromUtf8("QPushButton{\n"
"background:qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.56892, fx:0.5, fy:0.35259, stop:0.0397727 rgba(255, 211, 224, 255), stop:0.573864 rgba(255, 168, 88, 255), stop:0.653409 rgba(255, 0, 4, 255), stop:0.681818 rgba(255, 255, 255, 255), stop:0.767045 rgba(48, 26, 13, 255), stop:0.920455 rgba(255, 247, 250, 255));\n"
"border-radius:20px;\n"
"color:red;\n"
"}\n"
"QPushButton:hover{\n"
"background: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.56892, fx:0.5, fy:0.35259, stop:0.0397727 rgba(255, 211, 224, 255), stop:0.573864 rgba(255, 228, 17, 255), stop:0.653409 rgba(255, 4, 0, 255), stop:0.681818 rgba(255, 255, 255, 255), stop:0.767045 rgba(48, 26, 13, 255), stop:0.920455 rgba(255, 247, 250, 255));\n"
"border-radius:20px;\n"
"}\n"
"QPushButton:pressed{\n"
"background:qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.56892, fx:0.5, fy:0.35259, stop:0.0397727 rgba(255, 211, 224, 255), stop:0.573864 rgba(128, 1, 22, 255), stop:0.653409 rgba(255, 4, 0, 255), stop:0.681818 rgba(255, 255, 255, 255), stop:0.767045 rgba(48, 26, 13, 255), stop:0.920455 rgba(255, 247, 250, 255));\n"
"border-radius:20px\n"
"}"))
        self.pushButton_98.setObjectName(_fromUtf8("pushButton_98"))
        self.gridLayout_down.addWidget(self.pushButton_98, 4, 7, 1, 1)
        self.pushButton_79 = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_79.setMinimumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_79.setFont(font)
        self.pushButton_79.setText(_fromUtf8(""))
        self.pushButton_79.setObjectName(_fromUtf8("pushButton_79"))
        self.gridLayout_down.addWidget(self.pushButton_79, 2, 8, 1, 1)
        self.pushButton_62 = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_62.setMinimumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_62.setFont(font)
        self.pushButton_62.setText(_fromUtf8(""))
        self.pushButton_62.setObjectName(_fromUtf8("pushButton_62"))
        self.gridLayout_down.addWidget(self.pushButton_62, 1, 1, 1, 1)
        self.pushButton_89 = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_89.setMinimumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_89.setFont(font)
        self.pushButton_89.setStyleSheet(_fromUtf8(""))
        self.pushButton_89.setText(_fromUtf8(""))
        self.pushButton_89.setObjectName(_fromUtf8("pushButton_89"))
        self.gridLayout_down.addWidget(self.pushButton_89, 3, 8, 1, 1)
        self.pushButton_63 = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_63.setMinimumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_63.setFont(font)
        self.pushButton_63.setStyleSheet(_fromUtf8("QPushButton{\n"
"background:qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.56892, fx:0.5, fy:0.35259, stop:0.0397727 rgba(255, 211, 224, 255), stop:0.573864 rgba(255, 168, 88, 255), stop:0.653409 rgba(255, 0, 4, 255), stop:0.681818 rgba(255, 255, 255, 255), stop:0.767045 rgba(48, 26, 13, 255), stop:0.920455 rgba(255, 247, 250, 255));\n"
"border-radius:20px;\n"
"color:red;\n"
"}\n"
"QPushButton:hover{\n"
"background: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.56892, fx:0.5, fy:0.35259, stop:0.0397727 rgba(255, 211, 224, 255), stop:0.573864 rgba(255, 228, 17, 255), stop:0.653409 rgba(255, 4, 0, 255), stop:0.681818 rgba(255, 255, 255, 255), stop:0.767045 rgba(48, 26, 13, 255), stop:0.920455 rgba(255, 247, 250, 255));\n"
"border-radius:20px;\n"
"}\n"
"QPushButton:pressed{\n"
"background:qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.56892, fx:0.5, fy:0.35259, stop:0.0397727 rgba(255, 211, 224, 255), stop:0.573864 rgba(128, 1, 22, 255), stop:0.653409 rgba(255, 4, 0, 255), stop:0.681818 rgba(255, 255, 255, 255), stop:0.767045 rgba(48, 26, 13, 255), stop:0.920455 rgba(255, 247, 250, 255));\n"
"border-radius:20px\n"
"}"))
        self.pushButton_63.setObjectName(_fromUtf8("pushButton_63"))
        self.gridLayout_down.addWidget(self.pushButton_63, 1, 2, 1, 1)
        self.pushButton_88 = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_88.setMinimumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_88.setFont(font)
        self.pushButton_88.setText(_fromUtf8(""))
        self.pushButton_88.setObjectName(_fromUtf8("pushButton_88"))
        self.gridLayout_down.addWidget(self.pushButton_88, 3, 7, 1, 1)
        self.pushButton_55 = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_55.setMinimumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_55.setFont(font)
        self.pushButton_55.setText(_fromUtf8(""))
        self.pushButton_55.setObjectName(_fromUtf8("pushButton_55"))
        self.gridLayout_down.addWidget(self.pushButton_55, 0, 4, 1, 1)
        self.pushButton_96 = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_96.setMinimumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_96.setFont(font)
        self.pushButton_96.setStyleSheet(_fromUtf8("QPushButton{\n"
"background:qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.56892, fx:0.5, fy:0.35259, stop:0.0397727 rgba(255, 211, 224, 255), stop:0.573864 rgba(255, 168, 88, 255), stop:0.653409 rgba(255, 0, 4, 255), stop:0.681818 rgba(255, 255, 255, 255), stop:0.767045 rgba(48, 26, 13, 255), stop:0.920455 rgba(255, 247, 250, 255));\n"
"border-radius:20px;\n"
"color:red;\n"
"}\n"
"QPushButton:hover{\n"
"background: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.56892, fx:0.5, fy:0.35259, stop:0.0397727 rgba(255, 211, 224, 255), stop:0.573864 rgba(255, 228, 17, 255), stop:0.653409 rgba(255, 4, 0, 255), stop:0.681818 rgba(255, 255, 255, 255), stop:0.767045 rgba(48, 26, 13, 255), stop:0.920455 rgba(255, 247, 250, 255));\n"
"border-radius:20px;\n"
"}\n"
"QPushButton:pressed{\n"
"background:qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.56892, fx:0.5, fy:0.35259, stop:0.0397727 rgba(255, 211, 224, 255), stop:0.573864 rgba(128, 1, 22, 255), stop:0.653409 rgba(255, 4, 0, 255), stop:0.681818 rgba(255, 255, 255, 255), stop:0.767045 rgba(48, 26, 13, 255), stop:0.920455 rgba(255, 247, 250, 255));\n"
"border-radius:20px\n"
"}"))
        self.pushButton_96.setObjectName(_fromUtf8("pushButton_96"))
        self.gridLayout_down.addWidget(self.pushButton_96, 4, 5, 1, 1)
        self.pushButton_67 = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_67.setMinimumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_67.setFont(font)
        self.pushButton_67.setStyleSheet(_fromUtf8("QPushButton{\n"
"background:qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.56892, fx:0.5, fy:0.35259, stop:0.0397727 rgba(255, 211, 224, 255), stop:0.573864 rgba(255, 168, 88, 255), stop:0.653409 rgba(255, 0, 4, 255), stop:0.681818 rgba(255, 255, 255, 255), stop:0.767045 rgba(48, 26, 13, 255), stop:0.920455 rgba(255, 247, 250, 255));\n"
"border-radius:20px;\n"
"color:red;\n"
"}\n"
"QPushButton:hover{\n"
"background: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.56892, fx:0.5, fy:0.35259, stop:0.0397727 rgba(255, 211, 224, 255), stop:0.573864 rgba(255, 228, 17, 255), stop:0.653409 rgba(255, 4, 0, 255), stop:0.681818 rgba(255, 255, 255, 255), stop:0.767045 rgba(48, 26, 13, 255), stop:0.920455 rgba(255, 247, 250, 255));\n"
"border-radius:20px;\n"
"}\n"
"QPushButton:pressed{\n"
"background:qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.56892, fx:0.5, fy:0.35259, stop:0.0397727 rgba(255, 211, 224, 255), stop:0.573864 rgba(128, 1, 22, 255), stop:0.653409 rgba(255, 4, 0, 255), stop:0.681818 rgba(255, 255, 255, 255), stop:0.767045 rgba(48, 26, 13, 255), stop:0.920455 rgba(255, 247, 250, 255));\n"
"border-radius:20px\n"
"}"))
        self.pushButton_67.setObjectName(_fromUtf8("pushButton_67"))
        self.gridLayout_down.addWidget(self.pushButton_67, 1, 6, 1, 1)
        self.pushButton_95 = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_95.setMinimumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_95.setFont(font)
        self.pushButton_95.setStyleSheet(_fromUtf8("QPushButton{\n"
"background:qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.56892, fx:0.5, fy:0.35259, stop:0.0397727 rgba(255, 211, 224, 255), stop:0.573864 rgba(255, 168, 88, 255), stop:0.653409 rgba(255, 0, 4, 255), stop:0.681818 rgba(255, 255, 255, 255), stop:0.767045 rgba(48, 26, 13, 255), stop:0.920455 rgba(255, 247, 250, 255));\n"
"border-radius:20px;\n"
"color:red;\n"
"}\n"
"QPushButton:hover{\n"
"background: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.56892, fx:0.5, fy:0.35259, stop:0.0397727 rgba(255, 211, 224, 255), stop:0.573864 rgba(255, 228, 17, 255), stop:0.653409 rgba(255, 4, 0, 255), stop:0.681818 rgba(255, 255, 255, 255), stop:0.767045 rgba(48, 26, 13, 255), stop:0.920455 rgba(255, 247, 250, 255));\n"
"border-radius:20px;\n"
"}\n"
"QPushButton:pressed{\n"
"background:qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.56892, fx:0.5, fy:0.35259, stop:0.0397727 rgba(255, 211, 224, 255), stop:0.573864 rgba(128, 1, 22, 255), stop:0.653409 rgba(255, 4, 0, 255), stop:0.681818 rgba(255, 255, 255, 255), stop:0.767045 rgba(48, 26, 13, 255), stop:0.920455 rgba(255, 247, 250, 255));\n"
"border-radius:20px\n"
"}"))
        self.pushButton_95.setObjectName(_fromUtf8("pushButton_95"))
        self.gridLayout_down.addWidget(self.pushButton_95, 4, 4, 1, 1)
        self.pushButton_52 = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_52.setMinimumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_52.setFont(font)
        self.pushButton_52.setText(_fromUtf8(""))
        self.pushButton_52.setObjectName(_fromUtf8("pushButton_52"))
        self.gridLayout_down.addWidget(self.pushButton_52, 0, 1, 1, 1)
        self.pushButton_56 = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_56.setMinimumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_56.setFont(font)
        self.pushButton_56.setText(_fromUtf8(""))
        self.pushButton_56.setObjectName(_fromUtf8("pushButton_56"))
        self.gridLayout_down.addWidget(self.pushButton_56, 0, 5, 1, 1)
        self.pushButton_72 = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_72.setMinimumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_72.setFont(font)
        self.pushButton_72.setStyleSheet(_fromUtf8("QPushButton{\n"
"background:qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.56892, fx:0.5, fy:0.35259, stop:0.0397727 rgba(255, 211, 224, 255), stop:0.573864 rgba(255, 168, 88, 255), stop:0.653409 rgba(255, 0, 4, 255), stop:0.681818 rgba(255, 255, 255, 255), stop:0.767045 rgba(48, 26, 13, 255), stop:0.920455 rgba(255, 247, 250, 255));\n"
"border-radius:20px;\n"
"color:red;\n"
"}\n"
"QPushButton:hover{\n"
"background: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.56892, fx:0.5, fy:0.35259, stop:0.0397727 rgba(255, 211, 224, 255), stop:0.573864 rgba(255, 228, 17, 255), stop:0.653409 rgba(255, 4, 0, 255), stop:0.681818 rgba(255, 255, 255, 255), stop:0.767045 rgba(48, 26, 13, 255), stop:0.920455 rgba(255, 247, 250, 255));\n"
"border-radius:20px;\n"
"}\n"
"QPushButton:pressed{\n"
"background:qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.56892, fx:0.5, fy:0.35259, stop:0.0397727 rgba(255, 211, 224, 255), stop:0.573864 rgba(128, 1, 22, 255), stop:0.653409 rgba(255, 4, 0, 255), stop:0.681818 rgba(255, 255, 255, 255), stop:0.767045 rgba(48, 26, 13, 255), stop:0.920455 rgba(255, 247, 250, 255));\n"
"border-radius:20px\n"
"}"))
        self.pushButton_72.setObjectName(_fromUtf8("pushButton_72"))
        self.gridLayout_down.addWidget(self.pushButton_72, 2, 1, 1, 1)
        self.pushButton_65 = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_65.setMinimumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_65.setFont(font)
        self.pushButton_65.setStyleSheet(_fromUtf8("QPushButton{\n"
"background:qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.56892, fx:0.5, fy:0.35259, stop:0.0397727 rgba(255, 211, 224, 255), stop:0.573864 rgba(255, 168, 88, 255), stop:0.653409 rgba(255, 0, 4, 255), stop:0.681818 rgba(255, 255, 255, 255), stop:0.767045 rgba(48, 26, 13, 255), stop:0.920455 rgba(255, 247, 250, 255));\n"
"border-radius:20px;\n"
"color:red;\n"
"}\n"
"QPushButton:hover{\n"
"background: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.56892, fx:0.5, fy:0.35259, stop:0.0397727 rgba(255, 211, 224, 255), stop:0.573864 rgba(255, 228, 17, 255), stop:0.653409 rgba(255, 4, 0, 255), stop:0.681818 rgba(255, 255, 255, 255), stop:0.767045 rgba(48, 26, 13, 255), stop:0.920455 rgba(255, 247, 250, 255));\n"
"border-radius:20px;\n"
"}\n"
"QPushButton:pressed{\n"
"background:qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.56892, fx:0.5, fy:0.35259, stop:0.0397727 rgba(255, 211, 224, 255), stop:0.573864 rgba(128, 1, 22, 255), stop:0.653409 rgba(255, 4, 0, 255), stop:0.681818 rgba(255, 255, 255, 255), stop:0.767045 rgba(48, 26, 13, 255), stop:0.920455 rgba(255, 247, 250, 255));\n"
"border-radius:20px\n"
"}"))
        self.pushButton_65.setObjectName(_fromUtf8("pushButton_65"))
        self.gridLayout_down.addWidget(self.pushButton_65, 1, 4, 1, 1)
        self.pushButton_69 = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_69.setMinimumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_69.setFont(font)
        self.pushButton_69.setStyleSheet(_fromUtf8("QPushButton{\n"
"background:qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.56892, fx:0.5, fy:0.35259, stop:0.0397727 rgba(255, 211, 224, 255), stop:0.573864 rgba(255, 168, 88, 255), stop:0.653409 rgba(255, 0, 4, 255), stop:0.681818 rgba(255, 255, 255, 255), stop:0.767045 rgba(48, 26, 13, 255), stop:0.920455 rgba(255, 247, 250, 255));\n"
"border-radius:20px;\n"
"color:red;\n"
"}\n"
"QPushButton:hover{\n"
"background: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.56892, fx:0.5, fy:0.35259, stop:0.0397727 rgba(255, 211, 224, 255), stop:0.573864 rgba(255, 228, 17, 255), stop:0.653409 rgba(255, 4, 0, 255), stop:0.681818 rgba(255, 255, 255, 255), stop:0.767045 rgba(48, 26, 13, 255), stop:0.920455 rgba(255, 247, 250, 255));\n"
"border-radius:20px;\n"
"}\n"
"QPushButton:pressed{\n"
"background:qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.56892, fx:0.5, fy:0.35259, stop:0.0397727 rgba(255, 211, 224, 255), stop:0.573864 rgba(128, 1, 22, 255), stop:0.653409 rgba(255, 4, 0, 255), stop:0.681818 rgba(255, 255, 255, 255), stop:0.767045 rgba(48, 26, 13, 255), stop:0.920455 rgba(255, 247, 250, 255));\n"
"border-radius:20px\n"
"}"))
        self.pushButton_69.setObjectName(_fromUtf8("pushButton_69"))
        self.gridLayout_down.addWidget(self.pushButton_69, 1, 8, 1, 1)
        self.layoutWidget_2 = QtGui.QWidget(self.centralWidget)
        self.layoutWidget_2.setGeometry(QtCore.QRect(50, 20, 511, 281))
        self.layoutWidget_2.setObjectName(_fromUtf8("layoutWidget_2"))
        self.gridLayout_up = QtGui.QGridLayout(self.layoutWidget_2)
        self.gridLayout_up.setMargin(0)
        self.gridLayout_up.setObjectName(_fromUtf8("gridLayout_up"))
        self.pushButton_32 = QtGui.QPushButton(self.layoutWidget_2)
        self.pushButton_32.setMinimumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_32.setFont(font)
        self.pushButton_32.setText(_fromUtf8(""))
        self.pushButton_32.setObjectName(_fromUtf8("pushButton_32"))
        self.gridLayout_up.addWidget(self.pushButton_32, 3, 1, 1, 1)
        self.pushButton_44 = QtGui.QPushButton(self.layoutWidget_2)
        self.pushButton_44.setMinimumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_44.setFont(font)
        self.pushButton_44.setText(_fromUtf8(""))
        self.pushButton_44.setObjectName(_fromUtf8("pushButton_44"))
        self.gridLayout_up.addWidget(self.pushButton_44, 4, 3, 1, 1)
        self.pushButton_28 = QtGui.QPushButton(self.layoutWidget_2)
        self.pushButton_28.setMinimumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_28.setFont(font)
        self.pushButton_28.setStyleSheet(_fromUtf8("QPushButton{\n"
"background:qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.56892, fx:0.5, fy:0.35259, stop:0.0397727 rgba(255, 211, 224, 255), stop:0.573864 rgba(255, 168, 88, 255), stop:0.653409 rgba(5, 0, 0, 255), stop:0.681818 rgba(255, 255, 255, 255), stop:0.767045 rgba(48, 26, 13, 255), stop:0.920455 rgba(255, 247, 250, 255));\n"
"border-radius:20px;\n"
"}\n"
"QPushButton:hover{\n"
"background: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.56892, fx:0.5, fy:0.35259, stop:0.0397727 rgba(255, 211, 224, 255), stop:0.573864 rgba(255, 228, 17, 255), stop:0.653409 rgba(255, 4, 0, 255), stop:0.681818 rgba(255, 255, 255, 255), stop:0.767045 rgba(48, 26, 13, 255), stop:0.920455 rgba(255, 247, 250, 255));\n"
"border-radius:20px;\n"
"}\n"
"QPushButton:pressed{\n"
"background:qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.56892, fx:0.5, fy:0.35259, stop:0.0397727 rgba(255, 211, 224, 255), stop:0.573864 rgba(128, 1, 22, 255), stop:0.653409 rgba(255, 4, 0, 255), stop:0.681818 rgba(255, 255, 255, 255), stop:0.767045 rgba(48, 26, 13, 255), stop:0.920455 rgba(255, 247, 250, 255));\n"
"border-radius:20px\n"
"}"))
        self.pushButton_28.setObjectName(_fromUtf8("pushButton_28"))
        self.gridLayout_up.addWidget(self.pushButton_28, 2, 7, 1, 1)
        self.pushButton_11 = QtGui.QPushButton(self.layoutWidget_2)
        self.pushButton_11.setMinimumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setText(_fromUtf8(""))
        self.pushButton_11.setObjectName(_fromUtf8("pushButton_11"))
        self.gridLayout_up.addWidget(self.pushButton_11, 1, 0, 1, 1)
        self.pushButton_34 = QtGui.QPushButton(self.layoutWidget_2)
        self.pushButton_34.setMinimumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_34.setFont(font)
        self.pushButton_34.setText(_fromUtf8(""))
        self.pushButton_34.setObjectName(_fromUtf8("pushButton_34"))
        self.gridLayout_up.addWidget(self.pushButton_34, 3, 3, 1, 1)
        self.pushButton_33 = QtGui.QPushButton(self.layoutWidget_2)
        self.pushButton_33.setMinimumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_33.setFont(font)
        self.pushButton_33.setStyleSheet(_fromUtf8("QPushButton{\n"
"background:qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.56892, fx:0.5, fy:0.35259, stop:0.0397727 rgba(255, 211, 224, 255), stop:0.573864 rgba(255, 168, 88, 255), stop:0.653409 rgba(5, 0, 0, 255), stop:0.681818 rgba(255, 255, 255, 255), stop:0.767045 rgba(48, 26, 13, 255), stop:0.920455 rgba(255, 247, 250, 255));\n"
"border-radius:20px;\n"
"}\n"
"QPushButton:hover{\n"
"background: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.56892, fx:0.5, fy:0.35259, stop:0.0397727 rgba(255, 211, 224, 255), stop:0.573864 rgba(255, 228, 17, 255), stop:0.653409 rgba(255, 4, 0, 255), stop:0.681818 rgba(255, 255, 255, 255), stop:0.767045 rgba(48, 26, 13, 255), stop:0.920455 rgba(255, 247, 250, 255));\n"
"border-radius:20px;\n"
"}\n"
"QPushButton:pressed{\n"
"background:qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.56892, fx:0.5, fy:0.35259, stop:0.0397727 rgba(255, 211, 224, 255), stop:0.573864 rgba(128, 1, 22, 255), stop:0.653409 rgba(255, 4, 0, 255), stop:0.681818 rgba(255, 255, 255, 255), stop:0.767045 rgba(48, 26, 13, 255), stop:0.920455 rgba(255, 247, 250, 255));\n"
"border-radius:20px\n"
"}"))
        self.pushButton_33.setObjectName(_fromUtf8("pushButton_33"))
        self.gridLayout_up.addWidget(self.pushButton_33, 3, 2, 1, 1)
        self.pushButton_35 = QtGui.QPushButton(self.layoutWidget_2)
        self.pushButton_35.setMinimumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_35.setFont(font)
        self.pushButton_35.setStyleSheet(_fromUtf8("QPushButton{\n"
"background:qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.56892, fx:0.5, fy:0.35259, stop:0.0397727 rgba(255, 211, 224, 255), stop:0.573864 rgba(255, 168, 88, 255), stop:0.653409 rgba(5, 0, 0, 255), stop:0.681818 rgba(255, 255, 255, 255), stop:0.767045 rgba(48, 26, 13, 255), stop:0.920455 rgba(255, 247, 250, 255));\n"
"border-radius:20px;\n"
"}\n"
"QPushButton:hover{\n"
"background: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.56892, fx:0.5, fy:0.35259, stop:0.0397727 rgba(255, 211, 224, 255), stop:0.573864 rgba(255, 228, 17, 255), stop:0.653409 rgba(255, 4, 0, 255), stop:0.681818 rgba(255, 255, 255, 255), stop:0.767045 rgba(48, 26, 13, 255), stop:0.920455 rgba(255, 247, 250, 255));\n"
"border-radius:20px;\n"
"}\n"
"QPushButton:pressed{\n"
"background:qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.56892, fx:0.5, fy:0.35259, stop:0.0397727 rgba(255, 211, 224, 255), stop:0.573864 rgba(128, 1, 22, 255), stop:0.653409 rgba(255, 4, 0, 255), stop:0.681818 rgba(255, 255, 255, 255), stop:0.767045 rgba(48, 26, 13, 255), stop:0.920455 rgba(255, 247, 250, 255));\n"
"border-radius:20px\n"
"}"))
        self.pushButton_35.setObjectName(_fromUtf8("pushButton_35"))
        self.gridLayout_up.addWidget(self.pushButton_35, 3, 4, 1, 1)
        self.pushButton_27 = QtGui.QPushButton(self.layoutWidget_2)
        self.pushButton_27.setMinimumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_27.setFont(font)
        self.pushButton_27.setText(_fromUtf8(""))
        self.pushButton_27.setObjectName(_fromUtf8("pushButton_27"))
        self.gridLayout_up.addWidget(self.pushButton_27, 2, 6, 1, 1)
        self.pushButton_43 = QtGui.QPushButton(self.layoutWidget_2)
        self.pushButton_43.setMinimumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_43.setFont(font)
        self.pushButton_43.setText(_fromUtf8(""))
        self.pushButton_43.setObjectName(_fromUtf8("pushButton_43"))
        self.gridLayout_up.addWidget(self.pushButton_43, 4, 2, 1, 1)
        self.pushButton_04 = QtGui.QPushButton(self.layoutWidget_2)
        self.pushButton_04.setMinimumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_04.setFont(font)
        self.pushButton_04.setStyleSheet(_fromUtf8("QPushButton{\n"
"background:qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.56892, fx:0.5, fy:0.35259, stop:0.0397727 rgba(255, 211, 224, 255), stop:0.573864 rgba(255, 168, 88, 255), stop:0.653409 rgba(5, 0, 0, 255), stop:0.681818 rgba(255, 255, 255, 255), stop:0.767045 rgba(48, 26, 13, 255), stop:0.920455 rgba(255, 247, 250, 255));\n"
"border-radius:20px;\n"
"}\n"
"QPushButton:hover{\n"
"background: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.56892, fx:0.5, fy:0.35259, stop:0.0397727 rgba(255, 211, 224, 255), stop:0.573864 rgba(255, 228, 17, 255), stop:0.653409 rgba(255, 4, 0, 255), stop:0.681818 rgba(255, 255, 255, 255), stop:0.767045 rgba(48, 26, 13, 255), stop:0.920455 rgba(255, 247, 250, 255));\n"
"border-radius:20px;\n"
"}\n"
"QPushButton:pressed{\n"
"background:qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.56892, fx:0.5, fy:0.35259, stop:0.0397727 rgba(255, 211, 224, 255), stop:0.573864 rgba(128, 1, 22, 255), stop:0.653409 rgba(255, 4, 0, 255), stop:0.681818 rgba(255, 255, 255, 255), stop:0.767045 rgba(48, 26, 13, 255), stop:0.920455 rgba(255, 247, 250, 255));\n"
"border-radius:20px\n"
"}"))
        self.pushButton_04.setObjectName(_fromUtf8("pushButton_04"))
        self.gridLayout_up.addWidget(self.pushButton_04, 0, 3, 1, 1)
        self.pushButton_23 = QtGui.QPushButton(self.layoutWidget_2)
        self.pushButton_23.setMinimumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_23.setFont(font)
        self.pushButton_23.setText(_fromUtf8(""))
        self.pushButton_23.setObjectName(_fromUtf8("pushButton_23"))
        self.gridLayout_up.addWidget(self.pushButton_23, 2, 2, 1, 1)
        self.pushButton_42 = QtGui.QPushButton(self.layoutWidget_2)
        self.pushButton_42.setMinimumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_42.setFont(font)
        self.pushButton_42.setText(_fromUtf8(""))
        self.pushButton_42.setObjectName(_fromUtf8("pushButton_42"))
        self.gridLayout_up.addWidget(self.pushButton_42, 4, 1, 1, 1)
        self.pushButton_14 = QtGui.QPushButton(self.layoutWidget_2)
        self.pushButton_14.setEnabled(True)
        self.pushButton_14.setMinimumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setText(_fromUtf8(""))
        self.pushButton_14.setCheckable(False)
        self.pushButton_14.setObjectName(_fromUtf8("pushButton_14"))
        self.gridLayout_up.addWidget(self.pushButton_14, 1, 3, 1, 1)
        self.pushButton_26 = QtGui.QPushButton(self.layoutWidget_2)
        self.pushButton_26.setMinimumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_26.setFont(font)
        self.pushButton_26.setText(_fromUtf8(""))
        self.pushButton_26.setObjectName(_fromUtf8("pushButton_26"))
        self.gridLayout_up.addWidget(self.pushButton_26, 2, 5, 1, 1)
        self.pushButton_24 = QtGui.QPushButton(self.layoutWidget_2)
        self.pushButton_24.setMinimumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_24.setFont(font)
        self.pushButton_24.setText(_fromUtf8(""))
        self.pushButton_24.setObjectName(_fromUtf8("pushButton_24"))
        self.gridLayout_up.addWidget(self.pushButton_24, 2, 3, 1, 1)
        self.pushButton_07 = QtGui.QPushButton(self.layoutWidget_2)
        self.pushButton_07.setMinimumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_07.setFont(font)
        self.pushButton_07.setStyleSheet(_fromUtf8("QPushButton{\n"
"background:qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.56892, fx:0.5, fy:0.35259, stop:0.0397727 rgba(255, 211, 224, 255), stop:0.573864 rgba(255, 168, 88, 255), stop:0.653409 rgba(5, 0, 0, 255), stop:0.681818 rgba(255, 255, 255, 255), stop:0.767045 rgba(48, 26, 13, 255), stop:0.920455 rgba(255, 247, 250, 255));\n"
"border-radius:20px;\n"
"}\n"
"QPushButton:hover{\n"
"background: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.56892, fx:0.5, fy:0.35259, stop:0.0397727 rgba(255, 211, 224, 255), stop:0.573864 rgba(255, 228, 17, 255), stop:0.653409 rgba(255, 4, 0, 255), stop:0.681818 rgba(255, 255, 255, 255), stop:0.767045 rgba(48, 26, 13, 255), stop:0.920455 rgba(255, 247, 250, 255));\n"
"border-radius:20px;\n"
"}\n"
"QPushButton:pressed{\n"
"background:qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.56892, fx:0.5, fy:0.35259, stop:0.0397727 rgba(255, 211, 224, 255), stop:0.573864 rgba(128, 1, 22, 255), stop:0.653409 rgba(255, 4, 0, 255), stop:0.681818 rgba(255, 255, 255, 255), stop:0.767045 rgba(48, 26, 13, 255), stop:0.920455 rgba(255, 247, 250, 255));\n"
"border-radius:20px\n"
"}"))
        self.pushButton_07.setObjectName(_fromUtf8("pushButton_07"))
        self.gridLayout_up.addWidget(self.pushButton_07, 0, 6, 1, 1)
        self.pushButton_41 = QtGui.QPushButton(self.layoutWidget_2)
        self.pushButton_41.setMinimumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_41.setFont(font)
        self.pushButton_41.setText(_fromUtf8(""))
        self.pushButton_41.setObjectName(_fromUtf8("pushButton_41"))
        self.gridLayout_up.addWidget(self.pushButton_41, 4, 0, 1, 1)
        self.pushButton_49 = QtGui.QPushButton(self.layoutWidget_2)
        self.pushButton_49.setMinimumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_49.setFont(font)
        self.pushButton_49.setText(_fromUtf8(""))
        self.pushButton_49.setObjectName(_fromUtf8("pushButton_49"))
        self.gridLayout_up.addWidget(self.pushButton_49, 4, 8, 1, 1)
        self.pushButton_18 = QtGui.QPushButton(self.layoutWidget_2)
        self.pushButton_18.setMinimumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_18.setFont(font)
        self.pushButton_18.setText(_fromUtf8(""))
        self.pushButton_18.setObjectName(_fromUtf8("pushButton_18"))
        self.gridLayout_up.addWidget(self.pushButton_18, 1, 7, 1, 1)
        self.pushButton_37 = QtGui.QPushButton(self.layoutWidget_2)
        self.pushButton_37.setMinimumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_37.setFont(font)
        self.pushButton_37.setStyleSheet(_fromUtf8("QPushButton{\n"
"background:qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.56892, fx:0.5, fy:0.35259, stop:0.0397727 rgba(255, 211, 224, 255), stop:0.573864 rgba(255, 168, 88, 255), stop:0.653409 rgba(5, 0, 0, 255), stop:0.681818 rgba(255, 255, 255, 255), stop:0.767045 rgba(48, 26, 13, 255), stop:0.920455 rgba(255, 247, 250, 255));\n"
"border-radius:20px;\n"
"}\n"
"QPushButton:hover{\n"
"background: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.56892, fx:0.5, fy:0.35259, stop:0.0397727 rgba(255, 211, 224, 255), stop:0.573864 rgba(255, 228, 17, 255), stop:0.653409 rgba(255, 4, 0, 255), stop:0.681818 rgba(255, 255, 255, 255), stop:0.767045 rgba(48, 26, 13, 255), stop:0.920455 rgba(255, 247, 250, 255));\n"
"border-radius:20px;\n"
"}\n"
"QPushButton:pressed{\n"
"background:qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.56892, fx:0.5, fy:0.35259, stop:0.0397727 rgba(255, 211, 224, 255), stop:0.573864 rgba(128, 1, 22, 255), stop:0.653409 rgba(255, 4, 0, 255), stop:0.681818 rgba(255, 255, 255, 255), stop:0.767045 rgba(48, 26, 13, 255), stop:0.920455 rgba(255, 247, 250, 255));\n"
"border-radius:20px\n"
"}"))
        self.pushButton_37.setObjectName(_fromUtf8("pushButton_37"))
        self.gridLayout_up.addWidget(self.pushButton_37, 3, 6, 1, 1)
        self.pushButton_31 = QtGui.QPushButton(self.layoutWidget_2)
        self.pushButton_31.setMinimumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_31.setFont(font)
        self.pushButton_31.setStyleSheet(_fromUtf8("QPushButton{\n"
"background:qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.56892, fx:0.5, fy:0.35259, stop:0.0397727 rgba(255, 211, 224, 255), stop:0.573864 rgba(255, 168, 88, 255), stop:0.653409 rgba(5, 0, 0, 255), stop:0.681818 rgba(255, 255, 255, 255), stop:0.767045 rgba(48, 26, 13, 255), stop:0.920455 rgba(255, 247, 250, 255));\n"
"border-radius:20px;\n"
"}\n"
"QPushButton:hover{\n"
"background: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.56892, fx:0.5, fy:0.35259, stop:0.0397727 rgba(255, 211, 224, 255), stop:0.573864 rgba(255, 228, 17, 255), stop:0.653409 rgba(255, 4, 0, 255), stop:0.681818 rgba(255, 255, 255, 255), stop:0.767045 rgba(48, 26, 13, 255), stop:0.920455 rgba(255, 247, 250, 255));\n"
"border-radius:20px;\n"
"}\n"
"QPushButton:pressed{\n"
"background:qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.56892, fx:0.5, fy:0.35259, stop:0.0397727 rgba(255, 211, 224, 255), stop:0.573864 rgba(128, 1, 22, 255), stop:0.653409 rgba(255, 4, 0, 255), stop:0.681818 rgba(255, 255, 255, 255), stop:0.767045 rgba(48, 26, 13, 255), stop:0.920455 rgba(255, 247, 250, 255));\n"
"border-radius:20px\n"
"}"))
        self.pushButton_31.setObjectName(_fromUtf8("pushButton_31"))
        self.gridLayout_up.addWidget(self.pushButton_31, 3, 0, 1, 1)
        self.pushButton_01 = QtGui.QPushButton(self.layoutWidget_2)
        self.pushButton_01.setMinimumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_01.setFont(font)
        self.pushButton_01.setStyleSheet(_fromUtf8("QPushButton{\n"
"background:qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.56892, fx:0.5, fy:0.35259, stop:0.0397727 rgba(255, 211, 224, 255), stop:0.573864 rgba(255, 168, 88, 255), stop:0.653409 rgba(5, 0, 0, 255), stop:0.681818 rgba(255, 255, 255, 255), stop:0.767045 rgba(48, 26, 13, 255), stop:0.920455 rgba(255, 247, 250, 255));\n"
"border-radius:20px;\n"
"}\n"
"QPushButton:hover{\n"
"background: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.56892, fx:0.5, fy:0.35259, stop:0.0397727 rgba(255, 211, 224, 255), stop:0.573864 rgba(255, 228, 17, 255), stop:0.653409 rgba(255, 4, 0, 255), stop:0.681818 rgba(255, 255, 255, 255), stop:0.767045 rgba(48, 26, 13, 255), stop:0.920455 rgba(255, 247, 250, 255));\n"
"border-radius:20px;\n"
"}\n"
"QPushButton:pressed{\n"
"background:qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.56892, fx:0.5, fy:0.35259, stop:0.0397727 rgba(255, 211, 224, 255), stop:0.573864 rgba(128, 1, 22, 255), stop:0.653409 rgba(255, 4, 0, 255), stop:0.681818 rgba(255, 255, 255, 255), stop:0.767045 rgba(48, 26, 13, 255), stop:0.920455 rgba(255, 247, 250, 255));\n"
"border-radius:20px\n"
"}"))
        self.pushButton_01.setObjectName(_fromUtf8("pushButton_01"))
        self.gridLayout_up.addWidget(self.pushButton_01, 0, 0, 1, 1)
        self.pushButton_36 = QtGui.QPushButton(self.layoutWidget_2)
        self.pushButton_36.setMinimumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_36.setFont(font)
        self.pushButton_36.setText(_fromUtf8(""))
        self.pushButton_36.setObjectName(_fromUtf8("pushButton_36"))
        self.gridLayout_up.addWidget(self.pushButton_36, 3, 5, 1, 1)
        self.pushButton_25 = QtGui.QPushButton(self.layoutWidget_2)
        self.pushButton_25.setMinimumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_25.setFont(font)
        self.pushButton_25.setText(_fromUtf8(""))
        self.pushButton_25.setObjectName(_fromUtf8("pushButton_25"))
        self.gridLayout_up.addWidget(self.pushButton_25, 2, 4, 1, 1)
        self.pushButton_16 = QtGui.QPushButton(self.layoutWidget_2)
        self.pushButton_16.setMinimumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_16.setFont(font)
        self.pushButton_16.setText(_fromUtf8(""))
        self.pushButton_16.setObjectName(_fromUtf8("pushButton_16"))
        self.gridLayout_up.addWidget(self.pushButton_16, 1, 5, 1, 1)
        self.pushButton_03 = QtGui.QPushButton(self.layoutWidget_2)
        self.pushButton_03.setMinimumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_03.setFont(font)
        self.pushButton_03.setStyleSheet(_fromUtf8("QPushButton{\n"
"background:qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.56892, fx:0.5, fy:0.35259, stop:0.0397727 rgba(255, 211, 224, 255), stop:0.573864 rgba(255, 168, 88, 255), stop:0.653409 rgba(5, 0, 0, 255), stop:0.681818 rgba(255, 255, 255, 255), stop:0.767045 rgba(48, 26, 13, 255), stop:0.920455 rgba(255, 247, 250, 255));\n"
"border-radius:20px;\n"
"}\n"
"QPushButton:hover{\n"
"background: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.56892, fx:0.5, fy:0.35259, stop:0.0397727 rgba(255, 211, 224, 255), stop:0.573864 rgba(255, 228, 17, 255), stop:0.653409 rgba(255, 4, 0, 255), stop:0.681818 rgba(255, 255, 255, 255), stop:0.767045 rgba(48, 26, 13, 255), stop:0.920455 rgba(255, 247, 250, 255));\n"
"border-radius:20px;\n"
"}\n"
"QPushButton:pressed{\n"
"background:qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.56892, fx:0.5, fy:0.35259, stop:0.0397727 rgba(255, 211, 224, 255), stop:0.573864 rgba(128, 1, 22, 255), stop:0.653409 rgba(255, 4, 0, 255), stop:0.681818 rgba(255, 255, 255, 255), stop:0.767045 rgba(48, 26, 13, 255), stop:0.920455 rgba(255, 247, 250, 255));\n"
"border-radius:20px\n"
"}"))
        self.pushButton_03.setObjectName(_fromUtf8("pushButton_03"))
        self.gridLayout_up.addWidget(self.pushButton_03, 0, 2, 1, 1)
        self.pushButton_47 = QtGui.QPushButton(self.layoutWidget_2)
        self.pushButton_47.setMinimumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_47.setFont(font)
        self.pushButton_47.setText(_fromUtf8(""))
        self.pushButton_47.setObjectName(_fromUtf8("pushButton_47"))
        self.gridLayout_up.addWidget(self.pushButton_47, 4, 6, 1, 1)
        self.pushButton_21 = QtGui.QPushButton(self.layoutWidget_2)
        self.pushButton_21.setMinimumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_21.setFont(font)
        self.pushButton_21.setText(_fromUtf8(""))
        self.pushButton_21.setObjectName(_fromUtf8("pushButton_21"))
        self.gridLayout_up.addWidget(self.pushButton_21, 2, 0, 1, 1)
        self.pushButton_09 = QtGui.QPushButton(self.layoutWidget_2)
        self.pushButton_09.setMinimumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_09.setFont(font)
        self.pushButton_09.setStyleSheet(_fromUtf8("QPushButton{\n"
"background:qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.56892, fx:0.5, fy:0.35259, stop:0.0397727 rgba(255, 211, 224, 255), stop:0.573864 rgba(255, 168, 88, 255), stop:0.653409 rgba(5, 0, 0, 255), stop:0.681818 rgba(255, 255, 255, 255), stop:0.767045 rgba(48, 26, 13, 255), stop:0.920455 rgba(255, 247, 250, 255));\n"
"border-radius:20px;\n"
"}\n"
"QPushButton:hover{\n"
"background: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.56892, fx:0.5, fy:0.35259, stop:0.0397727 rgba(255, 211, 224, 255), stop:0.573864 rgba(255, 228, 17, 255), stop:0.653409 rgba(255, 4, 0, 255), stop:0.681818 rgba(255, 255, 255, 255), stop:0.767045 rgba(48, 26, 13, 255), stop:0.920455 rgba(255, 247, 250, 255));\n"
"border-radius:20px;\n"
"}\n"
"QPushButton:pressed{\n"
"background:qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.56892, fx:0.5, fy:0.35259, stop:0.0397727 rgba(255, 211, 224, 255), stop:0.573864 rgba(128, 1, 22, 255), stop:0.653409 rgba(255, 4, 0, 255), stop:0.681818 rgba(255, 255, 255, 255), stop:0.767045 rgba(48, 26, 13, 255), stop:0.920455 rgba(255, 247, 250, 255));\n"
"border-radius:20px\n"
"}"))
        self.pushButton_09.setObjectName(_fromUtf8("pushButton_09"))
        self.gridLayout_up.addWidget(self.pushButton_09, 0, 8, 1, 1)
        self.pushButton_08 = QtGui.QPushButton(self.layoutWidget_2)
        self.pushButton_08.setMinimumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_08.setFont(font)
        self.pushButton_08.setStyleSheet(_fromUtf8("QPushButton{\n"
"background:qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.56892, fx:0.5, fy:0.35259, stop:0.0397727 rgba(255, 211, 224, 255), stop:0.573864 rgba(255, 168, 88, 255), stop:0.653409 rgba(5, 0, 0, 255), stop:0.681818 rgba(255, 255, 255, 255), stop:0.767045 rgba(48, 26, 13, 255), stop:0.920455 rgba(255, 247, 250, 255));\n"
"border-radius:20px;\n"
"}\n"
"QPushButton:hover{\n"
"background: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.56892, fx:0.5, fy:0.35259, stop:0.0397727 rgba(255, 211, 224, 255), stop:0.573864 rgba(255, 228, 17, 255), stop:0.653409 rgba(255, 4, 0, 255), stop:0.681818 rgba(255, 255, 255, 255), stop:0.767045 rgba(48, 26, 13, 255), stop:0.920455 rgba(255, 247, 250, 255));\n"
"border-radius:20px;\n"
"}\n"
"QPushButton:pressed{\n"
"background:qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.56892, fx:0.5, fy:0.35259, stop:0.0397727 rgba(255, 211, 224, 255), stop:0.573864 rgba(128, 1, 22, 255), stop:0.653409 rgba(255, 4, 0, 255), stop:0.681818 rgba(255, 255, 255, 255), stop:0.767045 rgba(48, 26, 13, 255), stop:0.920455 rgba(255, 247, 250, 255));\n"
"border-radius:20px\n"
"}"))
        self.pushButton_08.setObjectName(_fromUtf8("pushButton_08"))
        self.gridLayout_up.addWidget(self.pushButton_08, 0, 7, 1, 1)
        self.pushButton_48 = QtGui.QPushButton(self.layoutWidget_2)
        self.pushButton_48.setMinimumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_48.setFont(font)
        self.pushButton_48.setText(_fromUtf8(""))
        self.pushButton_48.setObjectName(_fromUtf8("pushButton_48"))
        self.gridLayout_up.addWidget(self.pushButton_48, 4, 7, 1, 1)
        self.pushButton_29 = QtGui.QPushButton(self.layoutWidget_2)
        self.pushButton_29.setMinimumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_29.setFont(font)
        self.pushButton_29.setText(_fromUtf8(""))
        self.pushButton_29.setObjectName(_fromUtf8("pushButton_29"))
        self.gridLayout_up.addWidget(self.pushButton_29, 2, 8, 1, 1)
        self.pushButton_12 = QtGui.QPushButton(self.layoutWidget_2)
        self.pushButton_12.setMinimumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setText(_fromUtf8(""))
        self.pushButton_12.setObjectName(_fromUtf8("pushButton_12"))
        self.gridLayout_up.addWidget(self.pushButton_12, 1, 1, 1, 1)
        self.pushButton_39 = QtGui.QPushButton(self.layoutWidget_2)
        self.pushButton_39.setMinimumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_39.setFont(font)
        self.pushButton_39.setStyleSheet(_fromUtf8("QPushButton{\n"
"background:qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.56892, fx:0.5, fy:0.35259, stop:0.0397727 rgba(255, 211, 224, 255), stop:0.573864 rgba(255, 168, 88, 255), stop:0.653409 rgba(5, 0, 0, 255), stop:0.681818 rgba(255, 255, 255, 255), stop:0.767045 rgba(48, 26, 13, 255), stop:0.920455 rgba(255, 247, 250, 255));\n"
"border-radius:20px;\n"
"}\n"
"QPushButton:hover{\n"
"background: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.56892, fx:0.5, fy:0.35259, stop:0.0397727 rgba(255, 211, 224, 255), stop:0.573864 rgba(255, 228, 17, 255), stop:0.653409 rgba(255, 4, 0, 255), stop:0.681818 rgba(255, 255, 255, 255), stop:0.767045 rgba(48, 26, 13, 255), stop:0.920455 rgba(255, 247, 250, 255));\n"
"border-radius:20px;\n"
"}\n"
"QPushButton:pressed{\n"
"background:qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.56892, fx:0.5, fy:0.35259, stop:0.0397727 rgba(255, 211, 224, 255), stop:0.573864 rgba(128, 1, 22, 255), stop:0.653409 rgba(255, 4, 0, 255), stop:0.681818 rgba(255, 255, 255, 255), stop:0.767045 rgba(48, 26, 13, 255), stop:0.920455 rgba(255, 247, 250, 255));\n"
"border-radius:20px\n"
"}"))
        self.pushButton_39.setObjectName(_fromUtf8("pushButton_39"))
        self.gridLayout_up.addWidget(self.pushButton_39, 3, 8, 1, 1)
        self.pushButton_19 = QtGui.QPushButton(self.layoutWidget_2)
        self.pushButton_19.setMinimumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_19.setFont(font)
        self.pushButton_19.setStyleSheet(_fromUtf8(""))
        self.pushButton_19.setText(_fromUtf8(""))
        self.pushButton_19.setObjectName(_fromUtf8("pushButton_19"))
        self.gridLayout_up.addWidget(self.pushButton_19, 1, 8, 1, 1)
        self.pushButton_13 = QtGui.QPushButton(self.layoutWidget_2)
        self.pushButton_13.setMinimumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setText(_fromUtf8(""))
        self.pushButton_13.setObjectName(_fromUtf8("pushButton_13"))
        self.gridLayout_up.addWidget(self.pushButton_13, 1, 2, 1, 1)
        self.pushButton_38 = QtGui.QPushButton(self.layoutWidget_2)
        self.pushButton_38.setMinimumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_38.setFont(font)
        self.pushButton_38.setText(_fromUtf8(""))
        self.pushButton_38.setObjectName(_fromUtf8("pushButton_38"))
        self.gridLayout_up.addWidget(self.pushButton_38, 3, 7, 1, 1)
        self.pushButton_05 = QtGui.QPushButton(self.layoutWidget_2)
        self.pushButton_05.setMinimumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_05.setFont(font)
        self.pushButton_05.setStyleSheet(_fromUtf8("QPushButton{\n"
"background:qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.56892, fx:0.5, fy:0.35259, stop:0.0397727 rgba(255, 211, 224, 255), stop:0.573864 rgba(255, 168, 88, 255), stop:0.653409 rgba(5, 0, 0, 255), stop:0.681818 rgba(255, 255, 255, 255), stop:0.767045 rgba(48, 26, 13, 255), stop:0.920455 rgba(255, 247, 250, 255));\n"
"border-radius:20px;\n"
"}\n"
"QPushButton:hover{\n"
"background: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.56892, fx:0.5, fy:0.35259, stop:0.0397727 rgba(255, 211, 224, 255), stop:0.573864 rgba(255, 228, 17, 255), stop:0.653409 rgba(255, 4, 0, 255), stop:0.681818 rgba(255, 255, 255, 255), stop:0.767045 rgba(48, 26, 13, 255), stop:0.920455 rgba(255, 247, 250, 255));\n"
"border-radius:20px;\n"
"}\n"
"QPushButton:pressed{\n"
"background:qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.56892, fx:0.5, fy:0.35259, stop:0.0397727 rgba(255, 211, 224, 255), stop:0.573864 rgba(128, 1, 22, 255), stop:0.653409 rgba(255, 4, 0, 255), stop:0.681818 rgba(255, 255, 255, 255), stop:0.767045 rgba(48, 26, 13, 255), stop:0.920455 rgba(255, 247, 250, 255));\n"
"border-radius:20px\n"
"}"))
        self.pushButton_05.setObjectName(_fromUtf8("pushButton_05"))
        self.gridLayout_up.addWidget(self.pushButton_05, 0, 4, 1, 1)
        self.pushButton_46 = QtGui.QPushButton(self.layoutWidget_2)
        self.pushButton_46.setMinimumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_46.setFont(font)
        self.pushButton_46.setText(_fromUtf8(""))
        self.pushButton_46.setObjectName(_fromUtf8("pushButton_46"))
        self.gridLayout_up.addWidget(self.pushButton_46, 4, 5, 1, 1)
        self.pushButton_17 = QtGui.QPushButton(self.layoutWidget_2)
        self.pushButton_17.setMinimumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_17.setFont(font)
        self.pushButton_17.setText(_fromUtf8(""))
        self.pushButton_17.setObjectName(_fromUtf8("pushButton_17"))
        self.gridLayout_up.addWidget(self.pushButton_17, 1, 6, 1, 1)
        self.pushButton_45 = QtGui.QPushButton(self.layoutWidget_2)
        self.pushButton_45.setMinimumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_45.setFont(font)
        self.pushButton_45.setText(_fromUtf8(""))
        self.pushButton_45.setObjectName(_fromUtf8("pushButton_45"))
        self.gridLayout_up.addWidget(self.pushButton_45, 4, 4, 1, 1)
        self.pushButton_02 = QtGui.QPushButton(self.layoutWidget_2)
        self.pushButton_02.setMinimumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_02.setFont(font)
        self.pushButton_02.setStyleSheet(_fromUtf8("QPushButton{\n"
"background:qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.56892, fx:0.5, fy:0.35259, stop:0.0397727 rgba(255, 211, 224, 255), stop:0.573864 rgba(255, 168, 88, 255), stop:0.653409 rgba(5, 0, 0, 255), stop:0.681818 rgba(255, 255, 255, 255), stop:0.767045 rgba(48, 26, 13, 255), stop:0.920455 rgba(255, 247, 250, 255));\n"
"border-radius:20px;\n"
"}\n"
"QPushButton:hover{\n"
"background: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.56892, fx:0.5, fy:0.35259, stop:0.0397727 rgba(255, 211, 224, 255), stop:0.573864 rgba(255, 228, 17, 255), stop:0.653409 rgba(255, 4, 0, 255), stop:0.681818 rgba(255, 255, 255, 255), stop:0.767045 rgba(48, 26, 13, 255), stop:0.920455 rgba(255, 247, 250, 255));\n"
"border-radius:20px;\n"
"}\n"
"QPushButton:pressed{\n"
"background:qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.56892, fx:0.5, fy:0.35259, stop:0.0397727 rgba(255, 211, 224, 255), stop:0.573864 rgba(128, 1, 22, 255), stop:0.653409 rgba(255, 4, 0, 255), stop:0.681818 rgba(255, 255, 255, 255), stop:0.767045 rgba(48, 26, 13, 255), stop:0.920455 rgba(255, 247, 250, 255));\n"
"border-radius:20px\n"
"}"))
        self.pushButton_02.setObjectName(_fromUtf8("pushButton_02"))
        self.gridLayout_up.addWidget(self.pushButton_02, 0, 1, 1, 1)
        self.pushButton_06 = QtGui.QPushButton(self.layoutWidget_2)
        self.pushButton_06.setMinimumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_06.setFont(font)
        self.pushButton_06.setStyleSheet(_fromUtf8("QPushButton{\n"
"background:qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.56892, fx:0.5, fy:0.35259, stop:0.0397727 rgba(255, 211, 224, 255), stop:0.573864 rgba(255, 168, 88, 255), stop:0.653409 rgba(5, 0, 0, 255), stop:0.681818 rgba(255, 255, 255, 255), stop:0.767045 rgba(48, 26, 13, 255), stop:0.920455 rgba(255, 247, 250, 255));\n"
"border-radius:20px;\n"
"}\n"
"QPushButton:hover{\n"
"background: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.56892, fx:0.5, fy:0.35259, stop:0.0397727 rgba(255, 211, 224, 255), stop:0.573864 rgba(255, 228, 17, 255), stop:0.653409 rgba(255, 4, 0, 255), stop:0.681818 rgba(255, 255, 255, 255), stop:0.767045 rgba(48, 26, 13, 255), stop:0.920455 rgba(255, 247, 250, 255));\n"
"border-radius:20px;\n"
"}\n"
"QPushButton:pressed{\n"
"background:qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.56892, fx:0.5, fy:0.35259, stop:0.0397727 rgba(255, 211, 224, 255), stop:0.573864 rgba(128, 1, 22, 255), stop:0.653409 rgba(255, 4, 0, 255), stop:0.681818 rgba(255, 255, 255, 255), stop:0.767045 rgba(48, 26, 13, 255), stop:0.920455 rgba(255, 247, 250, 255));\n"
"border-radius:20px\n"
"}"))
        self.pushButton_06.setObjectName(_fromUtf8("pushButton_06"))
        self.gridLayout_up.addWidget(self.pushButton_06, 0, 5, 1, 1)
        self.pushButton_22 = QtGui.QPushButton(self.layoutWidget_2)
        self.pushButton_22.setMinimumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_22.setFont(font)
        self.pushButton_22.setStyleSheet(_fromUtf8("QPushButton{\n"
"background:qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.56892, fx:0.5, fy:0.35259, stop:0.0397727 rgba(255, 211, 224, 255), stop:0.573864 rgba(255, 168, 88, 255), stop:0.653409 rgba(5, 0, 0, 255), stop:0.681818 rgba(255, 255, 255, 255), stop:0.767045 rgba(48, 26, 13, 255), stop:0.920455 rgba(255, 247, 250, 255));\n"
"border-radius:20px;\n"
"}\n"
"QPushButton:hover{\n"
"background: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.56892, fx:0.5, fy:0.35259, stop:0.0397727 rgba(255, 211, 224, 255), stop:0.573864 rgba(255, 228, 17, 255), stop:0.653409 rgba(255, 4, 0, 255), stop:0.681818 rgba(255, 255, 255, 255), stop:0.767045 rgba(48, 26, 13, 255), stop:0.920455 rgba(255, 247, 250, 255));\n"
"border-radius:20px;\n"
"}\n"
"QPushButton:pressed{\n"
"background:qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.56892, fx:0.5, fy:0.35259, stop:0.0397727 rgba(255, 211, 224, 255), stop:0.573864 rgba(128, 1, 22, 255), stop:0.653409 rgba(255, 4, 0, 255), stop:0.681818 rgba(255, 255, 255, 255), stop:0.767045 rgba(48, 26, 13, 255), stop:0.920455 rgba(255, 247, 250, 255));\n"
"border-radius:20px\n"
"}"))
        self.pushButton_22.setObjectName(_fromUtf8("pushButton_22"))
        self.gridLayout_up.addWidget(self.pushButton_22, 2, 1, 1, 1)
        self.pushButton_15 = QtGui.QPushButton(self.layoutWidget_2)
        self.pushButton_15.setMinimumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_15.setFont(font)
        self.pushButton_15.setText(_fromUtf8(""))
        self.pushButton_15.setObjectName(_fromUtf8("pushButton_15"))
        self.gridLayout_up.addWidget(self.pushButton_15, 1, 4, 1, 1)
        self.label = QtGui.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(40, 275, 531, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 612, 21))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuFile = QtGui.QMenu(self.menuBar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuActions = QtGui.QMenu(self.menuBar)
        self.menuActions.setObjectName(_fromUtf8("menuActions"))
        self.menuHelp = QtGui.QMenu(self.menuBar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        self.menuAbout = QtGui.QMenu(self.menuBar)
        self.menuAbout.setObjectName(_fromUtf8("menuAbout"))
        self.menuSettings = QtGui.QMenu(self.menuBar)
        self.menuSettings.setObjectName(_fromUtf8("menuSettings"))
        self.menuMode = QtGui.QMenu(self.menuSettings)
        self.menuMode.setObjectName(_fromUtf8("menuMode"))
        self.menuLanguage = QtGui.QMenu(self.menuSettings)
        self.menuLanguage.setObjectName(_fromUtf8("menuLanguage"))
        self.menuLevel = QtGui.QMenu(self.menuSettings)
        self.menuLevel.setObjectName(_fromUtf8("menuLevel"))
        self.menuVersion = QtGui.QMenu(self.menuBar)
        self.menuVersion.setObjectName(_fromUtf8("menuVersion"))
        MainWindow.setMenuBar(self.menuBar)
        self.actionNew = QtGui.QAction(MainWindow)
        self.actionNew.setObjectName(_fromUtf8("actionNew"))
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionSave_as = QtGui.QAction(MainWindow)
        self.actionSave_as.setObjectName(_fromUtf8("actionSave_as"))
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionLoad = QtGui.QAction(MainWindow)
        self.actionLoad.setObjectName(_fromUtf8("actionLoad"))
        self.actionRegret = QtGui.QAction(MainWindow)
        self.actionRegret.setObjectName(_fromUtf8("actionRegret"))
        self.actionHint = QtGui.QAction(MainWindow)
        self.actionHint.setCheckable(False)
        self.actionHint.setChecked(False)
        self.actionHint.setObjectName(_fromUtf8("actionHint"))
        self.actionHelp_content = QtGui.QAction(MainWindow)
        self.actionHelp_content.setObjectName(_fromUtf8("actionHelp_content"))
        self.actionAbout_author = QtGui.QAction(MainWindow)
        self.actionAbout_author.setObjectName(_fromUtf8("actionAbout_author"))
        self.actionAbout_Chinese_chess = QtGui.QAction(MainWindow)
        self.actionAbout_Chinese_chess.setObjectName(_fromUtf8("actionAbout_Chinese_chess"))
        self.actionPyQt = QtGui.QAction(MainWindow)
        self.actionPyQt.setObjectName(_fromUtf8("actionPyQt"))
        self.actionPython = QtGui.QAction(MainWindow)
        self.actionPython.setObjectName(_fromUtf8("actionPython"))
        self.actionHvsC = QtGui.QAction(MainWindow)
        self.actionHvsC.setCheckable(True)
        self.actionHvsC.setChecked(True)
        self.actionHvsC.setObjectName(_fromUtf8("actionHvsC"))
        self.actionCvsC = QtGui.QAction(MainWindow)
        self.actionCvsC.setCheckable(True)
        self.actionCvsC.setObjectName(_fromUtf8("actionCvsC"))
        self.actionHvsH = QtGui.QAction(MainWindow)
        self.actionHvsH.setCheckable(True)
        self.actionHvsH.setEnabled(True)
        self.actionHvsH.setObjectName(_fromUtf8("actionHvsH"))
        self.actionChinese = QtGui.QAction(MainWindow)
        self.actionChinese.setCheckable(True)
        self.actionChinese.setChecked(True)
        self.actionChinese.setObjectName(_fromUtf8("actionChinese"))
        self.actionEnglish = QtGui.QAction(MainWindow)
        self.actionEnglish.setCheckable(True)
        self.actionEnglish.setObjectName(_fromUtf8("actionEnglish"))
        self.actionEasy = QtGui.QAction(MainWindow)
        self.actionEasy.setCheckable(True)
        self.actionEasy.setChecked(True)
        self.actionEasy.setObjectName(_fromUtf8("actionEasy"))
        self.actionMiddle = QtGui.QAction(MainWindow)
        self.actionMiddle.setCheckable(True)
        self.actionMiddle.setObjectName(_fromUtf8("actionMiddle"))
        self.actionHard = QtGui.QAction(MainWindow)
        self.actionHard.setCheckable(True)
        self.actionHard.setObjectName(_fromUtf8("actionHard"))
        self.actionSurrender = QtGui.QAction(MainWindow)
        self.actionSurrender.setObjectName(_fromUtf8("actionSurrender"))
        self.actionVersion = QtGui.QAction(MainWindow)
        self.actionVersion.setObjectName(_fromUtf8("actionVersion"))
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_as)
        self.menuFile.addAction(self.actionLoad)
        self.menuFile.addAction(self.actionQuit)
        self.menuActions.addAction(self.actionRegret)
        self.menuActions.addAction(self.actionHint)
        self.menuActions.addAction(self.actionSurrender)
        self.menuHelp.addAction(self.actionHelp_content)
        self.menuAbout.addAction(self.actionAbout_author)
        self.menuAbout.addAction(self.actionAbout_Chinese_chess)
        self.menuAbout.addAction(self.actionPyQt)
        self.menuMode.addAction(self.actionHvsC)
        self.menuMode.addAction(self.actionCvsC)
        self.menuMode.addAction(self.actionHvsH)
        self.menuLanguage.addAction(self.actionChinese)
        self.menuLanguage.addAction(self.actionEnglish)
        self.menuLevel.addAction(self.actionEasy)
        self.menuLevel.addAction(self.actionMiddle)
        self.menuLevel.addAction(self.actionHard)
        self.menuSettings.addAction(self.menuMode.menuAction())
        self.menuSettings.addAction(self.menuLanguage.menuAction())
        self.menuSettings.addAction(self.menuLevel.menuAction())
        self.menuVersion.addAction(self.actionVersion)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuSettings.menuAction())
        self.menuBar.addAction(self.menuActions.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())
        self.menuBar.addAction(self.menuAbout.menuAction())
        self.menuBar.addAction(self.menuVersion.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.actionQuit, QtCore.SIGNAL(_fromUtf8("activated()")), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "中国象棋-万志程", None))
        self.pushButton_94.setText(_translate("MainWindow", "仕", None))
        self.pushButton_78.setText(_translate("MainWindow", "炮", None))
        self.pushButton_61.setText(_translate("MainWindow", "兵", None))
        self.pushButton_93.setText(_translate("MainWindow", "相", None))
        self.pushButton_92.setText(_translate("MainWindow", "傌", None))
        self.pushButton_91.setText(_translate("MainWindow", "車", None))
        self.pushButton_99.setText(_translate("MainWindow", "車", None))
        self.pushButton_97.setText(_translate("MainWindow", "相", None))
        self.pushButton_98.setText(_translate("MainWindow", "傌", None))
        self.pushButton_63.setText(_translate("MainWindow", "兵", None))
        self.pushButton_96.setText(_translate("MainWindow", "仕", None))
        self.pushButton_67.setText(_translate("MainWindow", "兵", None))
        self.pushButton_95.setText(_translate("MainWindow", "帅", None))
        self.pushButton_72.setText(_translate("MainWindow", "炮", None))
        self.pushButton_65.setText(_translate("MainWindow", "兵", None))
        self.pushButton_69.setText(_translate("MainWindow", "兵", None))
        self.pushButton_28.setText(_translate("MainWindow", "砲", None))
        self.pushButton_33.setText(_translate("MainWindow", "卒", None))
        self.pushButton_35.setText(_translate("MainWindow", "卒", None))
        self.pushButton_04.setText(_translate("MainWindow", "士", None))
        self.pushButton_07.setText(_translate("MainWindow", "象", None))
        self.pushButton_37.setText(_translate("MainWindow", "卒", None))
        self.pushButton_31.setText(_translate("MainWindow", "卒", None))
        self.pushButton_01.setText(_translate("MainWindow", "车", None))
        self.pushButton_03.setText(_translate("MainWindow", "象", None))
        self.pushButton_09.setText(_translate("MainWindow", "车", None))
        self.pushButton_08.setText(_translate("MainWindow", "马", None))
        self.pushButton_39.setText(_translate("MainWindow", "卒", None))
        self.pushButton_05.setText(_translate("MainWindow", "将", None))
        self.pushButton_02.setText(_translate("MainWindow", "马", None))
        self.pushButton_06.setText(_translate("MainWindow", "士", None))
        self.pushButton_22.setText(_translate("MainWindow", "砲", None))
        self.label.setText(_translate("MainWindow", "楚河                 汉界", None))
        self.menuFile.setTitle(_translate("MainWindow", "文件", None))
        self.menuActions.setTitle(_translate("MainWindow", "行动", None))
        self.menuHelp.setTitle(_translate("MainWindow", "帮助", None))
        self.menuAbout.setTitle(_translate("MainWindow", "关于", None))
        self.menuSettings.setTitle(_translate("MainWindow", "设置", None))
        self.menuMode.setTitle(_translate("MainWindow", "模式", None))
        self.menuLanguage.setTitle(_translate("MainWindow", "语言", None))
        self.menuLevel.setTitle(_translate("MainWindow", "难度", None))
        self.menuVersion.setTitle(_translate("MainWindow", "版本", None))
        self.actionNew.setText(_translate("MainWindow", "新游戏", None))
        self.actionSave.setText(_translate("MainWindow", "保存", None))
        self.actionSave_as.setText(_translate("MainWindow", "另存为", None))
        self.actionQuit.setText(_translate("MainWindow", "退出", None))
        self.actionLoad.setText(_translate("MainWindow", "读取", None))
        self.actionRegret.setText(_translate("MainWindow", "悔棋", None))
        self.actionHint.setText(_translate("MainWindow", "提示", None))
        self.actionHelp_content.setText(_translate("MainWindow", "用户手册", None))
        self.actionAbout_author.setText(_translate("MainWindow", "关于作者", None))
        self.actionAbout_Chinese_chess.setText(_translate("MainWindow", "关于中国象棋", None))
        self.actionPyQt.setText(_translate("MainWindow", "关于PyQt", None))
        self.actionPython.setText(_translate("MainWindow", "关于Python", None))
        self.actionHvsC.setText(_translate("MainWindow", "人机对战", None))
        self.actionCvsC.setText(_translate("MainWindow", "自动对战", None))
        self.actionHvsH.setText(_translate("MainWindow", "自我推敲", None))
        self.actionChinese.setText(_translate("MainWindow", "中文", None))
        self.actionEnglish.setText(_translate("MainWindow", "English", None))
        self.actionEasy.setText(_translate("MainWindow", "入门", None))
        self.actionMiddle.setText(_translate("MainWindow", "中级", None))
        self.actionHard.setText(_translate("MainWindow", "高手", None))
        self.actionSurrender.setText(_translate("MainWindow", "认输", None))
        self.actionVersion.setText(_translate("MainWindow", "版权声明", None))

import ChineseChess_rc
