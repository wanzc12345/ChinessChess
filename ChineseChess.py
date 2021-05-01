# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""
import PyQt4.QtGui, sys, codecs
from PyQt4.QtGui import QMainWindow, QMessageBox, QApplication, QFileDialog
from PyQt4.QtCore import pyqtSignature, Qt
from Ui_mainwindow import Ui_MainWindow
import time
import random
class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent = None):
        """
        Constructor
        """
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        
        self.logo = self.label.text()
        self.__isPickup = False
        self.__isEnd = False
        self.__currentPiece = ""
        self.__currentSide = True
        self.__isHvsC = True
        self.__level = 1
        self.__language = "Chinese"
        self.__currentPosition = 0
        self.__currentHighlights = []
    
        self.types = {"兵":self.pushButton_61.text(), "卒":self.pushButton_31.text(), "炮":self.pushButton_72.text(), "砲":self.pushButton_22.text()
                    , "车":self.pushButton_01.text(), "車":self.pushButton_91.text(), "马":self.pushButton_02.text(), "傌":self.pushButton_92.text()
                    , "象":self.pushButton_03.text(), "相":self.pushButton_93.text(), "士":self.pushButton_04.text(), "仕":self.pushButton_94.text()
                    , "将":self.pushButton_05.text(), "帅":self.pushButton_95.text(), "RedStyle":"QPushButton{\n"
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
                                                 "}", "BlackStyle":"QPushButton{\n"
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
                                                 "}"}
        self.pieces = ['By Jensen', self.pushButton_01, self.pushButton_02, self.pushButton_03, self.pushButton_04, self.pushButton_05,
                                 self.pushButton_06, self.pushButton_07, self.pushButton_08, self.pushButton_09, 'wan', self.pushButton_11, 
                                 self.pushButton_12, self.pushButton_13, self.pushButton_14, self.pushButton_15, self.pushButton_16,
                                 self.pushButton_17, self.pushButton_18, self.pushButton_19, 'zhi', self.pushButton_21, self.pushButton_22,
                                 self.pushButton_23, self.pushButton_24, self.pushButton_25, self.pushButton_26, self.pushButton_27,
                                 self.pushButton_28, self.pushButton_29, 'cheng', self.pushButton_31, self.pushButton_32, self.pushButton_33,
                                 self.pushButton_34, self.pushButton_35, self.pushButton_36, self.pushButton_37, self.pushButton_38,
                                 self.pushButton_39, 'li', self.pushButton_41, self.pushButton_42, self.pushButton_43,
                                 self.pushButton_44, self.pushButton_45, self.pushButton_46, self.pushButton_47, self.pushButton_48,
                                 self.pushButton_49, 'mei', self.pushButton_51, self.pushButton_52, self.pushButton_53, self.pushButton_54,
                                 self.pushButton_55, self.pushButton_56, self.pushButton_57, self.pushButton_58, self.pushButton_59,
                                 'xuan', self.pushButton_61, self.pushButton_62, self.pushButton_63, self.pushButton_64, self.pushButton_65,
                                 self.pushButton_66, self.pushButton_67, self.pushButton_68, self.pushButton_69, 'love', self.pushButton_71,
                                 self.pushButton_72, self.pushButton_73, self.pushButton_74, self.pushButton_75, self.pushButton_76,
                                 self.pushButton_77, self.pushButton_78, self.pushButton_79, 'each', self.pushButton_81, self.pushButton_82,
                                 self.pushButton_83, self.pushButton_84, self.pushButton_85, self.pushButton_86, self.pushButton_87,
                                 self.pushButton_88, self.pushButton_89, 'other', self.pushButton_91, self.pushButton_92, self.pushButton_93,
                                 self.pushButton_94, self.pushButton_95, self.pushButton_96, self.pushButton_97, self.pushButton_98, self.pushButton_99]
        
        self.pushButton_11.setStyleSheet("border-radius:10px");
        self.pushButton_12.setStyleSheet("border-radius:10px");
        self.pushButton_13.setStyleSheet("border-radius:10px");
        self.pushButton_14.setStyleSheet("border-radius:10px");
        self.pushButton_15.setStyleSheet("border-radius:10px");
        self.pushButton_16.setStyleSheet("border-radius:10px");
        self.pushButton_17.setStyleSheet("border-radius:10px");
        self.pushButton_18.setStyleSheet("border-radius:10px");
        self.pushButton_19.setStyleSheet("border-radius:10px");

        self.pushButton_21.setStyleSheet("border-radius:10px");
        self.pushButton_23.setStyleSheet("border-radius:10px");
        self.pushButton_24.setStyleSheet("border-radius:10px");
        self.pushButton_25.setStyleSheet("border-radius:10px");
        self.pushButton_26.setStyleSheet("border-radius:10px");
        self.pushButton_27.setStyleSheet("border-radius:10px");
        self.pushButton_29.setStyleSheet("border-radius:10px");

        self.pushButton_32.setStyleSheet("border-radius:10px");
        self.pushButton_34.setStyleSheet("border-radius:10px");
        self.pushButton_36.setStyleSheet("border-radius:10px");
        self.pushButton_38.setStyleSheet("border-radius:10px");

        self.pushButton_41.setStyleSheet("border-radius:10px");
        self.pushButton_42.setStyleSheet("border-radius:10px");
        self.pushButton_43.setStyleSheet("border-radius:10px");
        self.pushButton_44.setStyleSheet("border-radius:10px");
        self.pushButton_45.setStyleSheet("border-radius:10px");
        self.pushButton_46.setStyleSheet("border-radius:10px");
        self.pushButton_47.setStyleSheet("border-radius:10px");
        self.pushButton_48.setStyleSheet("border-radius:10px");
        self.pushButton_49.setStyleSheet("border-radius:10px");

        self.pushButton_51.setStyleSheet("border-radius:10px");
        self.pushButton_52.setStyleSheet("border-radius:10px");
        self.pushButton_53.setStyleSheet("border-radius:10px");
        self.pushButton_54.setStyleSheet("border-radius:10px");
        self.pushButton_55.setStyleSheet("border-radius:10px");
        self.pushButton_56.setStyleSheet("border-radius:10px");
        self.pushButton_57.setStyleSheet("border-radius:10px");
        self.pushButton_58.setStyleSheet("border-radius:10px");
        self.pushButton_59.setStyleSheet("border-radius:10px");

        self.pushButton_62.setStyleSheet("border-radius:10px");
        self.pushButton_64.setStyleSheet("border-radius:10px");
        self.pushButton_66.setStyleSheet("border-radius:10px");
        self.pushButton_68.setStyleSheet("border-radius:10px");

        self.pushButton_71.setStyleSheet("border-radius:10px");
        self.pushButton_73.setStyleSheet("border-radius:10px");
        self.pushButton_74.setStyleSheet("border-radius:10px");
        self.pushButton_75.setStyleSheet("border-radius:10px");
        self.pushButton_76.setStyleSheet("border-radius:10px");
        self.pushButton_77.setStyleSheet("border-radius:10px");
        self.pushButton_79.setStyleSheet("border-radius:10px");

        self.pushButton_81.setStyleSheet("border-radius:10px");
        self.pushButton_82.setStyleSheet("border-radius:10px");
        self.pushButton_83.setStyleSheet("border-radius:10px");
        self.pushButton_84.setStyleSheet("border-radius:10px");
        self.pushButton_85.setStyleSheet("border-radius:10px");
        self.pushButton_86.setStyleSheet("border-radius:10px");
        self.pushButton_87.setStyleSheet("border-radius:10px");
        self.pushButton_88.setStyleSheet("border-radius:10px");
        self.pushButton_89.setStyleSheet("border-radius:10px");
    
    def __getValidDestination(self):
        result = list()
        
        if self.__currentPiece.__eq__(self.types["兵"]):
            if self.__currentPosition > 10:
                result.append(self.__currentPosition - 10)
            if self.__currentPosition < 50:
                if self.__currentPosition % 10 != 1:
                    result.append(self.__currentPosition - 1)
                if self.__currentPosition % 10 != 9:
                    result.append(self.__currentPosition + 1)
                    
        if self.__currentPiece.__eq__(self.types["卒"]):
            if self.__currentPosition < 90:
                result.append(self.__currentPosition + 10)
            if self.__currentPosition > 50:
                if self.__currentPosition % 10 != 1:
                    result.append(self.__currentPosition - 1)
                if self.__currentPosition % 10 != 9:
                    result.append(self.__currentPosition + 1)
                    
        if self.__currentPiece.__eq__(self.types["炮"]) or self.__currentPiece.__eq__(self.types["砲"]):
            tmp = self.__currentPosition - 10
            while tmp > 0:
                if self.pieces[tmp].text().compare(""):
                    tmp = tmp - 10
                    while tmp > 0:
                        if self.pieces[tmp].text().compare(""):
                            result.append(tmp)
                            tmp = 0
                            break
                        tmp = tmp - 10
                else:
                    result.append(tmp)
                tmp = tmp - 10
                        
            tmp = self.__currentPosition + 10
            while tmp < 100:
                if self.pieces[tmp].text().compare(""):
                    tmp = tmp + 10
                    while tmp < 100:
                        if self.pieces[tmp].text().compare(""):
                            result.append(tmp)
                            tmp = 100
                            break
                        tmp = tmp + 10
                else:
                    result.append(tmp)
                tmp = tmp + 10
                
            tmp = self.__currentPosition - 1
            while tmp % 10 > 0 and tmp % 10 < self.__currentPosition % 10:
                if self.pieces[tmp].text().compare(""):
                    tmp = tmp - 1
                    while tmp % 10 > 0 and tmp % 10 < self.__currentPosition % 10:
                        if self.pieces[tmp].text().compare(""):
                            result.append(tmp)
                            tmp = 1
                            break
                        tmp = tmp - 1
                else:
                    result.append(tmp)
                tmp = tmp - 1
                
            tmp = self.__currentPosition + 1
            while tmp % 10 > self.__currentPosition % 10:
                if self.pieces[tmp].text().compare(""):
                    tmp = tmp + 1
                    while tmp % 10 > self.__currentPosition % 10:
                        if self.pieces[tmp].text().compare(""):
                            result.append(tmp)
                            tmp = -1
                            break
                        tmp = tmp + 1
                else:
                    result.append(tmp)
                tmp = tmp + 1
                
        if self.__currentPiece.__eq__(self.types["仕"]):
            if self.__currentPosition == 85:
                result.extend([74, 76, 94, 96])
            else:
                result.append(85)
                
        if self.__currentPiece.__eq__(self.types["士"]):
            if self.__currentPosition == 15:
                result.extend([4, 6, 24, 26])
            else:
                result.append(15)
                
        if self.__currentPiece.__eq__(self.types["车"]) or self.__currentPiece.__eq__(self.types["車"]):
            tmp = self.__currentPosition - 10
            while tmp > 0:
                result.append(tmp)
                if self.pieces[tmp].text().compare(""):
                    break
                tmp = tmp - 10
            tmp = self.__currentPosition + 10
            while tmp < 100:
                result.append(tmp)
                if self.pieces[tmp].text().compare(""):
                    break
                tmp = tmp + 10
            tmp = self.__currentPosition - 1
            while tmp % 10 != 0:
                result.append(tmp)
                if self.pieces[tmp].text().compare(""):
                    break
                tmp = tmp - 1
            tmp = self.__currentPosition + 1
            while tmp % 10 != 0:
                result.append(tmp)
                if self.pieces[tmp].text().compare(""):
                    break
                tmp = tmp + 1
                
        if self.__currentPiece.__eq__(self.types["相"]) or self.__currentPiece.__eq__(self.types["象"]):
            if self.__currentPosition == 75 or self.__currentPosition == 25:
                result.extend([self.__currentPosition-22, self.__currentPosition-18,
                               self.__currentPosition+22, self.__currentPosition+18])
            if self.__currentPosition / 10 == 9 or self.__currentPosition / 10 == 4:
                result.extend([self.__currentPosition-22, self.__currentPosition-18])
            if self.__currentPosition / 10 == 0 or self.__currentPosition / 10 == 5:
                result.extend([self.__currentPosition+22, self.__currentPosition+18])
            if self.__currentPosition % 10 == 1:
                result.extend([self.__currentPosition+22, self.__currentPosition-18])
            if self.__currentPosition % 10 == 9:
                result.extend([self.__currentPosition-22, self.__currentPosition+18])
                    
        if self.__currentPiece.__eq__(self.types["将"]):
            if self.__currentPosition / 10 > 0:
                result.append(self.__currentPosition - 10)
            if self.__currentPosition / 10 < 2:
                result.append(self.__currentPosition + 10)
            if self.__currentPosition % 10 > 4:
                result.append(self.__currentPosition - 1)
            if self.__currentPosition % 10 < 6:
                result.append(self.__currentPosition + 1)
                
        if self.__currentPiece.__eq__(self.types["帅"]):
            if self.__currentPosition / 10 > 7:
                result.append(self.__currentPosition - 10)
            if self.__currentPosition / 10 < 9:
                result.append(self.__currentPosition + 10)
            if self.__currentPosition % 10 > 4:
                result.append(self.__currentPosition - 1)
            if self.__currentPosition % 10 < 6:
                result.append(self.__currentPosition + 1)
        
        if self.__currentPiece.__eq__(self.types["马"]) or self.__currentPiece.__eq__(self.types["傌"]):
            if self.__currentPosition > 20 and self.pieces[self.__currentPosition-10].text().__eq__(""):
                if self.__currentPosition % 10 > 1:
                    result.append(self.__currentPosition - 21)
                if self.__currentPosition % 10 < 9:
                    result.append(self.__currentPosition - 19)
            if self.__currentPosition < 80 and self.pieces[self.__currentPosition+10].text().__eq__(""):
                if self.__currentPosition % 10 > 1:
                    result.append(self.__currentPosition + 19)
                if self.__currentPosition % 10 < 9:
                    result.append(self.__currentPosition + 21)
            if self.__currentPosition % 10 > 2 and self.pieces[self.__currentPosition-1].text().__eq__(""):
                if self.__currentPosition > 10:
                    result.append(self.__currentPosition - 12)
                if self.__currentPosition < 90:
                    result.append(self.__currentPosition + 8)
            if self.__currentPosition % 10 < 8 and self.pieces[self.__currentPosition+1].text().__eq__(""):
                if self.__currentPosition > 10:
                    result.append(self.__currentPosition - 8)
                if self.__currentPosition < 90:
                    result.append(self.__currentPosition + 12)
                    
        return result
    
    def __clickReaction(self, index):
        if not self.__isPickup:
            if self.pieces[index].text().compare(""): 
                if (self.__currentSide and self.__isRedPiece(self.pieces[index].text())) or (not self.__currentSide and not self.__isRedPiece(self.pieces[index].text())):
                    self.__isPickup = True
                    self.__currentPiece = self.pieces[index].text()
                    self.__currentPosition = index
                    self.__setHighlight(self.__getValidDestination())
                    self.label.setText(self.logo)
                else:
                    self.label.setText(QApplication.translate("MainWindow", "那不是你的棋子！", None, QApplication.UnicodeUTF8))
            else:
                self.label.setText(QApplication.translate("MainWindow", "那里没有棋子!", None, QApplication.UnicodeUTF8))
        else:
            if self.pieces[index].text().compare("") and self.__isAlly(self.pieces[index].text(), self.__currentPiece):
                self.__cancelHighlight()
                self.__isPickup = True
                self.__currentPiece = self.pieces[index].text()
                self.__currentPosition = index
                self.__setHighlight(self.__getValidDestination())
                self.label.setText(self.logo)
            else:
                if self.__getValidDestination().__contains__(index):
                    self.__isPickup = False;
                    self.__cancelHighlight()
                    if(self.pieces[index].text().__eq__(self.types["帅"])):
                        self.__end(QApplication.translate("MainWindow", "黑方", None, QApplication.UnicodeUTF8))
                        return
                    if(self.pieces[index].text().__eq__(self.types["将"])):
                        self.__end(QApplication.translate("MainWindow", "红方", None, QApplication.UnicodeUTF8))
                        return
                    self.__movePieceToPosition(index);
                    self.__currentSide = not self.__currentSide
                    self.label.setText(self.logo)
                else:
                    self.label.setText(QApplication.translate("MainWindow", "不能走到那里!", None, QApplication.UnicodeUTF8))
    
    def __movePieceToPosition(self, destination):
        self.pieces[destination].setStyleSheet(self.pieces[self.__currentPosition].styleSheet())
        self.pieces[destination].setText(self.__currentPiece)
        self.pieces[self.__currentPosition].setStyleSheet("border-radius:10px")
        self.pieces[self.__currentPosition].setText("")
        self.__lastPosition = self.__currentPosition
        self.__currentPosition = destination
    
    def __setHighlight(self, destinationList):
        self.__currentHighlights = []
        for p in destinationList:
            if self.pieces[p].text().compare(""):
                if not self.__isAlly(self.pieces[p].text(), self.__currentPiece):
                    self.pieces[p].setStyleSheet("QPushButton{\n"
                                                 "background:qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.56892, fx:0.5, fy:0.35259, stop:0.0397727 rgba(255, 211, 224, 255), stop:0.573864 rgba(128, 1, 22, 255), stop:0.653409 rgba(255, 4, 0, 255), stop:0.681818 rgba(255, 255, 255, 255), stop:0.767045 rgba(48, 26, 13, 255), stop:0.920455 rgba(255, 247, 250, 255));\n"
                                                 "border-radius:20px\n"
                                                 "}"
                                                 "QPushButton:hover{\n"
                                                 "background: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.56892, fx:0.5, fy:0.35259, stop:0.0397727 rgba(255, 211, 224, 255), stop:0.573864 rgba(255, 228, 17, 255), stop:0.653409 rgba(255, 4, 0, 255), stop:0.681818 rgba(255, 255, 255, 255), stop:0.767045 rgba(48, 26, 13, 255), stop:0.920455 rgba(255, 247, 250, 255));\n"
                                                 "border-radius:20px;\n"
                                                 "}\n"
                                                 "QPushButton:pressed{\n"
                                                 "background:qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.56892, fx:0.5, fy:0.35259, stop:0.0397727 rgba(255, 211, 224, 255), stop:0.573864 rgba(128, 1, 22, 255), stop:0.653409 rgba(255, 4, 0, 255), stop:0.681818 rgba(255, 255, 255, 255), stop:0.767045 rgba(48, 26, 13, 255), stop:0.920455 rgba(255, 247, 250, 255));\n"
                                                 "border-radius:20px\n"
                                                 "}")
                    self.__currentHighlights.append(p)
            else:
                self.pieces[p].setStyleSheet("border:1px groove gray;border-radius:20px")
                self.__currentHighlights.append(p)
    
    def __isAlly(self, piece1, piece2):
        if (self.__isRedPiece(piece1) and self.__isRedPiece(piece2)) or (self.__isBlackPiece(piece1) and self.__isBlackPiece(piece2)):
            return True
        else:
            return False
    
    def __cancelHighlight(self):
        for p in self.__currentHighlights:
            if self.pieces[p].text().compare(""):
                if self.__isRedPiece(self.pieces[p].text()):
                    self.pieces[p].setStyleSheet(self.types["RedStyle"])
                else:
                    self.pieces[p].setStyleSheet(self.types["BlackStyle"])
            else:
                self.pieces[p].setStyleSheet("border-radius:1px")
        self.__currentHighlights = []
    
    def __isRedPiece(self, pieceName):
        if pieceName in [self.types["兵"], self.types["炮"], self.types["傌"], self.types["帅"]
                         , self.types["車"], self.types["仕"], self.types["相"]]:
            return True
        else:
            return False
        
    def __isBlackPiece(self, pieceName):
        if pieceName in [self.types["卒"], self.types["砲"], self.types["马"], self.types["将"]
                         , self.types["车"], self.types["士"], self.types["象"]]:
            return True
        else:
            return False
    
    def __end(self, side):
        dialog = QMessageBox.information(self, "Message", side+QApplication.translate("MainWindow"
                    , "胜！", None, QApplication.UnicodeUTF8), QMessageBox.Ok | QMessageBox.Cancel, QMessageBox.Ok)
        self.__isEnd = True
        self.label.setText(QApplication.translate("MainWindow", "胜败乃兵家常事，大侠请重新来过", None, QApplication.UnicodeUTF8))
    
    def autoRun(self):
        while not self.__isEnd:
            self.computerMove()
            self.repaint()
            time.sleep(1)
        
    def computerMove(self):
        if self.__level == 3:
            for i in range(1, 100):
                if i % 10 != 0 and self.pieces[i].text().compare(""):
                    self.__clickReaction(i)
                    for j in self.__currentHighlights:
                        if self.pieces[j].text().compare("") and not self.__isAlly(self.pieces[i].text(), self.pieces[j].text()) and self.isNoLessThan(self.pieces[j].text(), self.pieces[i].text()):
                            self.__clickReaction(j)
                            return
        elif self.__level == 2:
            for i in range(1, 100):
                if i % 10 != 0 and self.pieces[i].text().compare(""):
                    self.__clickReaction(i)
                    for j in self.__currentHighlights:
                        if self.pieces[j].text().compare("") and not self.__isAlly(self.pieces[i].text(), self.pieces[j].text()):
                            self.__clickReaction(j)
                            return                 
        while True:
                j = random.randrange(1, 100)
                if j % 10 != 0:
                    if j in self.__currentHighlights:
                        self.__clickReaction(j)
                        break           
                    else:
                        self.__clickReaction(j)
    
    def isNoLessThan(self, piece1, piece2):
        if piece1.__eq__(self.types["车"]) or piece1.__eq__(self.types["車"]):
            return True
        elif piece1.__eq__(self.types["炮"]) or piece1.__eq__(self.types["砲"]):
            if piece2.__eq__(self.types["车"]) or piece2.__eq__(self.types["車"]):
                return False
            else:
                return True
        elif piece1.__eq__(self.types["马"]) or piece1.__eq__(self.types["傌"]):
            if piece2.__eq__(self.types["车"]) or piece2.__eq__(self.types["車"]) or piece2.__eq__(self.types["炮"]) or piece2.__eq__(self.types["砲"]):
                return False
            else:
                return True
        else:
            if piece2.__eq__(self.types["车"]) or piece2.__eq__(self.types["車"]) or piece2.__eq__(self.types["炮"]) or piece2.__eq__(self.types["砲"]) or piece2.__eq__(self.types["马"]) or piece2.__eq__(self.types["傌"]):
                return False
            else:
                return True
    
    @pyqtSignature("")
    def on_actionSave_triggered(self):
        f = codecs.open("last.wan", 'w', 'utf-8')
        for i in range(100):
            if i % 10 != 0:
                f.write(self.pieces[i].text()+"\n")
        f.write(str(self.__isPickup)+"\n")
        f.write(str(self.__isEnd)+"\n")
        f.write(str(self.__currentPiece)+"\n")
        f.write(str(self.__currentSide)+"\n")
        f.write(str(self.__isHvsC)+"\n")
        f.write(str(self.__level)+"\n")
        f.write(str(self.__language)+"\n")
        f.write(str(self.__currentPosition)+"\n")
        f.writelines(self.__currentHighlights)
        f.close()
        dialog = QMessageBox.information(self, "Message", QApplication.translate("MainWindow", "保存成功！", None, QApplication.UnicodeUTF8), QMessageBox.Ok)
  
    @pyqtSignature("")
    def on_actionNew_triggered(self):
        """
        Slot documentation goes here.
        """
        self.__isPickup = False
        self.__isEnd = False
        self.__currentPiece = ""
        self.__currentSide = True
        self.__isHvsC = True
        self.__currentPosition = 0
        self.__currentHighlights = []

       	for i in range(1, 100):
            if i in [1, 9]:
                self.pieces[i].setText(self.types["车"])
                self.pieces[i].setStyleSheet(self.types["BlackStyle"])
            elif i in [2, 8]:
                self.pieces[i].setText(self.types["马"])
                self.pieces[i].setStyleSheet(self.types["BlackStyle"])
            elif i in [3, 7]:
                self.pieces[i].setText(self.types["象"])
                self.pieces[i].setStyleSheet(self.types["BlackStyle"])
            elif i in [4, 6]:
                self.pieces[i].setText(self.types["士"])
                self.pieces[i].setStyleSheet(self.types["BlackStyle"])
            elif i == 5:
                self.pieces[i].setText(self.types["将"])
                self.pieces[i].setStyleSheet(self.types["BlackStyle"])
            elif i in [22, 28]:
                self.pieces[i].setText(self.types["砲"])
                self.pieces[i].setStyleSheet(self.types["BlackStyle"])
            elif i in [31, 33, 35, 37, 39]:
                self.pieces[i].setText(self.types["卒"])
                self.pieces[i].setStyleSheet(self.types["BlackStyle"])
            elif i in [61, 63, 65, 67, 69]:
                self.pieces[i].setText(self.types["兵"])
                self.pieces[i].setStyleSheet(self.types["RedStyle"])
            elif i in [72, 78]:
                self.pieces[i].setText(self.types["炮"])
                self.pieces[i].setStyleSheet(self.types["RedStyle"])
            elif i == 95:
                self.pieces[i].setText(self.types["帅"])
                self.pieces[i].setStyleSheet(self.types["RedStyle"])
            elif i in [94, 96]:
                self.pieces[i].setText(self.types["仕"])
                self.pieces[i].setStyleSheet(self.types["RedStyle"])
            elif i in [93, 97]:
                self.pieces[i].setText(self.types["相"])
                self.pieces[i].setStyleSheet(self.types["RedStyle"])
            elif i in [92, 98]:
                self.pieces[i].setText(self.types["傌"])
                self.pieces[i].setStyleSheet(self.types["RedStyle"])
            elif i in [91, 99]:
                self.pieces[i].setText(self.types["車"])
                self.pieces[i].setStyleSheet(self.types["RedStyle"])
            elif i % 10 != 0:
                self.pieces[i].setText("")
                self.pieces[i].setStyleSheet("border-radius:1px")

    @pyqtSignature("")
    def on_actionSave_as_triggered(self):
        """
        Slot documentation goes here.
        """
        fileName = QFileDialog.getSaveFileName(self, "Save As", "last","Chess Files(*.wan)")
        f = codecs.open(fileName, 'w', 'utf-8')
        for i in range(100):
            if i % 10 != 0:
                f.write(self.pieces[i].text().decode("utf-8")+"\n")
        f.write(str(self.__isPickup)+"\n")
        f.write(str(self.__isEnd)+"\n")
        f.write(str(self.__currentPiece)+"\n")
        f.write(str(self.__currentSide)+"\n")
        f.write(str(self.__isHvsC)+"\n")
        f.write(str(self.__level)+"\n")
        f.write(str(self.__language)+"\n")
        f.write(str(self.__currentPosition)+"\n")
        f.writelines(self.__currentHighlights)
        f.close()
        dialog = QMessageBox.information(self, "Message", QApplication.translate("MainWindow", "保存成功！", None, QApplication.UnicodeUTF8), QMessageBox.Ok)
    
    @pyqtSignature("")
    def on_actionQuit_triggered(self):
        """
        Slot documentation goes here.
        """
        self.close()
    
    @pyqtSignature("")
    def on_actionLoad_triggered(self):
        """
        Slot documentation goes here.
        """
        fileName = QFileDialog.getOpenFileName(self, "Load File", "last","Chess Files(*.wan)")
        f = codecs.open(fileName, 'r', 'utf-8')
        for i in range(100):
            if i % 10 != 0:
                self.pieces[i].setText(f.readline().strip("\n"))
                if self.__isRedPiece(self.pieces[i].text()):
                    self.pieces[i].setStyleSheet(self.types["RedStyle"])
                elif self.__isBlackPiece(self.pieces[i].text()):
                    self.pieces[i].setStyleSheet(self.types["BlackStyle"])
                else:
                    self.pieces[i].setStyleSheet("border:2px")
        dialog = QMessageBox.information(self, "Message", QApplication.translate("MainWindow"
                                        , "读取成功！", None, QApplication.UnicodeUTF8), QMessageBox.Ok)
    
    @pyqtSignature("")
    def on_actionEasy_triggered(self):
        """
        Slot documentation goes here.
        """
        self.actionEasy.setChecked(True)
        self.actionMiddle.setChecked(False)
        self.actionHard.setChecked(False)
        self.__level = 1
        
    @pyqtSignature("")
    def on_actionMiddle_triggered(self):
        """
        Slot documentation goes here.
        """
        self.actionEasy.setChecked(False)
        self.actionMiddle.setChecked(True)
        self.actionHard.setChecked(False)
        self.__level = 2
        
    @pyqtSignature("")
    def on_actionHard_triggered(self):
        """
        Slot documentation goes here.
        """
        self.actionEasy.setChecked(False)
        self.actionMiddle.setChecked(False)
        self.actionHard.setChecked(True)
        self.__level = 3
    
    @pyqtSignature("")
    def on_actionRegret_triggered(self):
        """
        Slot documentation goes here.
        """
        dialog = QMessageBox.information(self, "Message", QApplication.translate("MainWindow"
                            , "起手无回大丈夫！", None, QApplication.UnicodeUTF8), QMessageBox.Ok | QMessageBox.Cancel, QMessageBox.Ok)
        self.__movePieceToPosition(self.__lastPosition)

    def on_actionSurrender_triggered(self):
        dialog = QMessageBox.information(self, "Message"
                        , QApplication.translate("MainWindow","黑方胜！", None, QApplication.UnicodeUTF8), QMessageBox.Ok)

    @pyqtSignature("")
    def on_actionHint_triggered(self):
        """
        Slot documentation goes here.
        """
        while True:
            i = random.randrange(100)
            if i % 10 != 0 and self.__isRedPiece(self.pieces[i].text()):
                self.pieces[i].setStyleSheet("background: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.56892, fx:0.5, fy:0.35259, stop:0.0397727 rgba(255, 211, 224, 255), stop:0.573864 rgba(255, 228, 17, 255), stop:0.653409 rgba(255, 4, 0, 255), stop:0.681818 rgba(255, 255, 255, 255), stop:0.767045 rgba(48, 26, 13, 255), stop:0.920455 rgba(255, 247, 250, 255));\n"
                                                 "border-radius:20px;\n")
                self.repaint()
                time.sleep(1)
                self.pieces[i].setStyleSheet(self.types["RedStyle"])
                break
    
    @pyqtSignature("")
    def on_actionHelp_content_triggered(self):
        """
        Slot documentation goes here.
        """
        dialog = QMessageBox.information(self, QApplication.translate("MainWindow","中国象棋-万志程", None, QApplication.UnicodeUTF8)
                                         , QApplication.translate("MainWindow", "1.新开游戏：文件->新游戏\n"
                                                                                 "2.存储当前游戏：文件->保存\n"
                                                                                 "3.存储为其他文件：文件->另存为\n"
                                                                                 "4.读取以往记录：文件->读取\n"
                                                                                 "5.退出游戏：文件->退出\n"
                                                                                 "6.改变游戏模式：设置->模式，共三种（人机对战，自动对战，自我推敲）\n"
                                                                                 "7.更改显示语言：设置->语言，共两种（中文，English）\n"
                                                                                 "8.更改AI难度：设置->难度，共三种（入门，中级，高手）\n"
                                                                                 "9.认输：动作->认输\n"
                                                                                 "10.悔棋：动作->悔棋\n"
                                                                                 "11.提示：动作->提示\n"
                                                                                 "12.帮助内容：帮助->用户手册\n"
                                                                                 "13.查看作者信息：关于->关于作者\n"
                                                                                 "14.查看中国象棋介绍：关于->关于中国象棋\n"
                                                                                 "15.查看开发工具介绍：关于->关于PyQt\n"
                                                                                 "16.查看版本信息：版本->版权声明", None, QApplication.UnicodeUTF8)
                                         , QMessageBox.Ok)
    
    @pyqtSignature("")
    def on_actionAbout_author_triggered(self):
        """
        Slot documentation goes here.
        """
        dialog = QMessageBox.information(self, QApplication.translate("MainWindow","Jensen", None, QApplication.UnicodeUTF8), 
                                         QApplication.translate("MainWindow", "本人是上海交通大学软件学院大四在读学生，"
                                                                "因见各Linux发行版游戏库中都缺少中国象棋这一中华国粹，"
                                                                "故奋而做此小品以弥补缺憾，同时也可供大家研究赏玩。"
                                                                "但因本人水平有限，如有任何疏漏和谬误，还请大家批评指正。\n"
                                                                "\nEmail: wanzhicheng12345@163.com", None, QApplication.UnicodeUTF8)
                                         , QMessageBox.Ok)
    
    @pyqtSignature("")
    def on_actionAbout_Chinese_chess_triggered(self):
        """
        Slot documentation goes here.
        """
        dialog = QMessageBox.information(self, QApplication.translate("MainWindow","中国象棋", None, QApplication.UnicodeUTF8), 
                                         QApplication.translate("MainWindow", "中国象棋棋盘与棋子象棋是由两人轮流走子，"
                                         "以“将死”或“困毙”对方将（帅）为胜的一种棋类运动，有着数以亿计的爱好者。它不仅能丰富文化生活，"
                                         "陶冶情操，更有助于开发智力，启迪思维，锻炼辨证分析能力和培养顽强的意志。[1]"
                                         "对局时，由执红棋的一方先走，双方轮流各走一着，直至分出胜、负、和，对局即终了。"
                                         "轮到走棋的一方，将某个棋子从一个交叉点走到另一个交叉点，或者吃掉对方的棋子而占领其交叉点，"
                                         "都算走一着。双方各走一着，称为一个回合。"
                                         "象棋是中华民族的传统文化，不仅在国内深受群众喜爱，而且流传国外。\n", None, QApplication.UnicodeUTF8)
                                         , QMessageBox.Ok)
    
    @pyqtSignature("")
    def on_actionPyQt_triggered(self):
        """
        Slot documentation goes here.
        """
        dialog = QMessageBox.information(self, "PyQt", 
                                         QApplication.translate("MainWindow", "PyQt是一个创建GUI应用程序的工具包。"
                                                                "它是Python编程语言和Qt库的成功融合。Qt库是目前最强大的库之一。"
                                                                "PyQt是由Phil Thompson 开发。 PyQt实现了一个Python模块集。"
                                                                "它有超过300类，将近6000个函数和方法。它是一个多平台的工具包，"
                                                                "可以运行在所有主要操作系统上，包括UNIX，Windows和Mac。\n"
                                         , None, QApplication.UnicodeUTF8), QMessageBox.Ok)
        
    @pyqtSignature("")
    def on_actionVersion_triggered(self):
        """
        Slot documentation goes here.
        """
        dialog = QMessageBox.information(self, "Copyright", 
                                         QApplication.translate("MainWindow", "版权所有：\nCopyright @ Jensen 2012.12"
                                         , None, QApplication.UnicodeUTF8), QMessageBox.Ok)
    
    @pyqtSignature("")
    def on_actionHvsC_triggered(self):
        """
        Slot documentation goes here.
        """
        self.actionHvsC.setChecked(True)
        self.actionCvsC.setChecked(False)
        self.actionHvsH.setChecked(False)
        self.__isHvsC = True
    
    @pyqtSignature("")
    def on_actionCvsC_triggered(self):
        """
        Slot documentation goes here.
        """
        self.actionHvsC.setChecked(False)
        self.actionCvsC.setChecked(True)
        self.actionHvsH.setChecked(False)
        self.autoRun()
    
    @pyqtSignature("")
    def on_actionHvsH_triggered(self):
        """
        Slot documentation goes here.
        """
        self.actionHvsC.setChecked(False)
        self.actionCvsC.setChecked(False)
        self.actionHvsH.setChecked(True)
        self.__isHvsC = False
    
    @pyqtSignature("")
    def on_actionChinese_triggered(self):
        """
        Slot documentation goes here.
        """
        self.actionChinese.setChecked(True)
        self.actionEnglish.setChecked(False)
        
        self.menuFile.setTitle(QApplication.translate("MainWindow", '文件', None, QApplication.UnicodeUTF8))
        self.actionNew.setText(QApplication.translate("MainWindow", '新建', None, QApplication.UnicodeUTF8))
        self.actionSave.setText(QApplication.translate("MainWindow", '保存', None, QApplication.UnicodeUTF8))
        self.actionSave_as.setText(QApplication.translate("MainWindow", '另存为', None, QApplication.UnicodeUTF8))
        self.actionLoad.setText(QApplication.translate("MainWindow", '读取', None, QApplication.UnicodeUTF8))
        self.actionQuit.setText(QApplication.translate("MainWindow", '退出', None, QApplication.UnicodeUTF8))
        self.menuSettings.setTitle(QApplication.translate("MainWindow", '设置', None, QApplication.UnicodeUTF8))
        self.menuMode.setTitle(QApplication.translate("MainWindow", '模式', None, QApplication.UnicodeUTF8))
        self.actionHvsC.setText(QApplication.translate("MainWindow", '人机对战', None, QApplication.UnicodeUTF8))
        self.actionCvsC.setText(QApplication.translate("MainWindow", '自动对战', None, QApplication.UnicodeUTF8))
        self.actionHvsH.setText(QApplication.translate("MainWindow", '自我推敲', None, QApplication.UnicodeUTF8))
        self.menuLanguage.setTitle(QApplication.translate("MainWindow", '语言', None, QApplication.UnicodeUTF8))
        self.menuLevel.setTitle(QApplication.translate("MainWindow", '难度', None, QApplication.UnicodeUTF8))
        self.actionEasy.setText(QApplication.translate("MainWindow", '入门', None, QApplication.UnicodeUTF8))
        self.actionMiddle.setText(QApplication.translate("MainWindow", '中级', None, QApplication.UnicodeUTF8))
        self.actionHard.setText(QApplication.translate("MainWindow", '高手', None, QApplication.UnicodeUTF8))
        self.menuActions.setTitle(QApplication.translate("MainWindow", '行动', None, QApplication.UnicodeUTF8))
        self.actionRegret.setText(QApplication.translate("MainWindow", '悔棋', None, QApplication.UnicodeUTF8))
        self.actionHint.setText(QApplication.translate("MainWindow", '提示', None, QApplication.UnicodeUTF8))
        self.actionSurrender.setText(QApplication.translate("MainWindow", '认输', None, QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QApplication.translate("MainWindow", '帮助', None, QApplication.UnicodeUTF8))
        self.actionHelp_content.setText(QApplication.translate("MainWindow", '用户手册', None, QApplication.UnicodeUTF8))
        self.menuAbout.setTitle(QApplication.translate("MainWindow", '关于', None, QApplication.UnicodeUTF8))
        self.actionAbout_author.setText(QApplication.translate("MainWindow", '关于作者', None, QApplication.UnicodeUTF8))
        self.actionAbout_Chinese_chess.setText(QApplication.translate("MainWindow", '关于中国象棋', None, QApplication.UnicodeUTF8))
        self.actionPyQt.setText(QApplication.translate("MainWindow", '关于PyQt', None, QApplication.UnicodeUTF8))
        self.menuVersion.setTitle(QApplication.translate("MainWindow", '版本', None, QApplication.UnicodeUTF8))
        self.actionVersion.setText(QApplication.translate("MainWindow", '版本说明', None, QApplication.UnicodeUTF8))     
                          
        dialog = QMessageBox.information(self, "Message", QApplication.translate("MainWindow", '已设置为中文。', None, QApplication.UnicodeUTF8), QMessageBox.Ok)
    
    @pyqtSignature("")
    def on_actionEnglish_triggered(self):
        """
        Slot documentation goes here.
        """
        self.actionChinese.setChecked(False)
        self.actionEnglish.setChecked(True)
        
        self.menuFile.setTitle("File")
        self.actionNew.setText("New")
        self.actionSave.setText("Save")
        self.actionSave_as.setText("Save as")
        self.actionLoad.setText("Load")
        self.actionQuit.setText("Quit")
        self.menuSettings.setTitle("Settings")
        self.menuMode.setTitle("Mode")
        self.actionHvsC.setText("Human vs Computer")
        self.actionCvsC.setText("Computer vs Computer")
        self.actionHvsH.setText("Human vs Human")
        self.menuLanguage.setTitle("Language")
        self.menuLevel.setTitle("AI level")
        self.actionEasy.setText("Easy")
        self.actionMiddle.setText("Normal")
        self.actionHard.setText("Hard")
        self.menuActions.setTitle("Actions")
        self.actionRegret.setText("Regret")
        self.actionHint.setText("Hint")
        self.actionSurrender.setText("Surrender")
        self.menuHelp.setTitle("Help")
        self.actionHelp_content.setText("User Manual")
        self.menuAbout.setTitle("About")
        self.actionAbout_author.setText("About author...")
        self.actionAbout_Chinese_chess.setText("About Chinese chess...")
        self.actionPyQt.setText("About PyQt...")
        self.menuVersion.setTitle("Version")
        self.actionVersion.setText("Version statement")
        
        dialog = QMessageBox.information(self, "Message", "English is set.", QMessageBox.Ok)

    @pyqtSignature("")
    def on_pushButton_55_clicked(self):
        """
        Slot documentation goes here.
        """
        self.__clickReaction(55)
        if not self.__isPickup and self.__isHvsC and not self.__currentSide:
            self.computerMove()
            
    @pyqtSignature("")
    def on_pushButton_65_clicked(self):
        self.__clickReaction(65)
        if not self.__isPickup and self.__isHvsC and not self.__currentSide:
            self.computerMove()

    @pyqtSignature("")
    def on_pushButton_35_clicked(self):
        """
        Slot documentation goes here.
        """
        self.__clickReaction(35)
        if not self.__isPickup and self.__isHvsC and not self.__currentSide:
            self.computerMove()
    
    @pyqtSignature("")
    def on_pushButton_01_clicked(self):
        """
        Slot documentation goes here.
        """
        self.__clickReaction(1)
        if not self.__isPickup and self.__isHvsC and not self.__currentSide:
            self.computerMove()
    
    @pyqtSignature("")
    def on_pushButton_82_clicked(self):
        """
        Slot documentation goes here.
        """
        self.__clickReaction(82)
        if not self.__isPickup and self.__isHvsC and not self.__currentSide:
            self.computerMove()
    
    @pyqtSignature("")
    def on_pushButton_94_clicked(self):
        """
        Slot documentation goes here.
        """
        self.__clickReaction(94)
        if not self.__isPickup and self.__isHvsC and not self.__currentSide:
            self.computerMove()
    
    @pyqtSignature("")
    def on_pushButton_78_clicked(self):
        """
        Slot documentation goes here.
        """
        self.__clickReaction(78)
        if not self.__isPickup and self.__isHvsC and not self.__currentSide:
            self.computerMove()
    
    @pyqtSignature("")
    def on_pushButton_84_clicked(self):
        """
        Slot documentation goes here.
        """
        self.__clickReaction(84)
        if not self.__isPickup and self.__isHvsC and not self.__currentSide:
            self.computerMove()
    
    @pyqtSignature("")
    def on_pushButton_61_clicked(self):
        """
        Slot documentation goes here.
        """
        self.__clickReaction(61)
        if not self.__isPickup and self.__isHvsC and not self.__currentSide:
            self.computerMove()
            
    @pyqtSignature("")
    def on_pushButton_83_clicked(self):
        """
        Slot documentation goes here.
        """
        self.__clickReaction(83)
        if not self.__isPickup and self.__isHvsC and not self.__currentSide:
            self.computerMove()
    
    @pyqtSignature("")
    def on_pushButton_85_clicked(self):
        """
        Slot documentation goes here.
        """
        self.__clickReaction(85)
        if not self.__isPickup and self.__isHvsC and not self.__currentSide:
            self.computerMove()
    
    @pyqtSignature("")
    def on_pushButton_77_clicked(self):
        """
        Slot documentation goes here.
        """
        self.__clickReaction(77)
        if not self.__isPickup and self.__isHvsC and not self.__currentSide:
            self.computerMove()
    
    @pyqtSignature("")
    def on_pushButton_93_clicked(self):
        """
        Slot documentation goes here.
        """
        self.__clickReaction(93)
        if not self.__isPickup and self.__isHvsC and not self.__currentSide:
            self.computerMove()
    
    @pyqtSignature("")
    def on_pushButton_54_clicked(self):
        """
        Slot documentation goes here.
        """
        self.__clickReaction(54)
        if not self.__isPickup and self.__isHvsC and not self.__currentSide:
            self.computerMove()
    
    @pyqtSignature("")
    def on_pushButton_73_clicked(self):
        """
        Slot documentation goes here.
        """
        self.__clickReaction(73)
        if not self.__isPickup and self.__isHvsC and not self.__currentSide:
            self.computerMove()
    
    @pyqtSignature("")
    def on_pushButton_92_clicked(self):
        """
        Slot documentation goes here.
        """
        self.__clickReaction(92)
        if not self.__isPickup and self.__isHvsC and not self.__currentSide:
            self.computerMove()
    
    @pyqtSignature("")
    def on_pushButton_64_clicked(self):
        """
        Slot documentation goes here.
        """
        self.__clickReaction(64)
        if not self.__isPickup and self.__isHvsC and not self.__currentSide:
            self.computerMove()
    
    @pyqtSignature("")
    def on_pushButton_76_clicked(self):
        """
        Slot documentation goes here.
        """
        self.__clickReaction(76)
        if not self.__isPickup and self.__isHvsC and not self.__currentSide:
            self.computerMove()
    
    @pyqtSignature("")
    def on_pushButton_74_clicked(self):
        """
        Slot documentation goes here.
        """
        self.__clickReaction(74)
        if not self.__isPickup and self.__isHvsC and not self.__currentSide:
            self.computerMove()
    
    @pyqtSignature("")
    def on_pushButton_57_clicked(self):
        """
        Slot documentation goes here.
        """
        self.__clickReaction(57)
        if not self.__isPickup and self.__isHvsC and not self.__currentSide:
            self.computerMove()
    
    @pyqtSignature("")
    def on_pushButton_91_clicked(self):
        """
        Slot documentation goes here.
        """
        self.__clickReaction(91)
        if not self.__isPickup and self.__isHvsC and not self.__currentSide:
            self.computerMove()
    
    @pyqtSignature("")
    def on_pushButton_99_clicked(self):
        """
        Slot documentation goes here.
        """
        self.__clickReaction(99)
        if not self.__isPickup and self.__isHvsC and not self.__currentSide:
            self.computerMove()
    
    @pyqtSignature("")
    def on_pushButton_68_clicked(self):
        """
        Slot documentation goes here.
        """
        self.__clickReaction(68)
        if not self.__isPickup and self.__isHvsC and not self.__currentSide:
            self.computerMove()
    
    @pyqtSignature("")
    def on_pushButton_87_clicked(self):
        """
        Slot documentation goes here.
        """
        self.__clickReaction(87)
        if not self.__isPickup and self.__isHvsC and not self.__currentSide:
            self.computerMove()
    
    @pyqtSignature("")
    def on_pushButton_81_clicked(self):
        """
        Slot documentation goes here.
        """
        self.__clickReaction(81)
        if not self.__isPickup and self.__isHvsC and not self.__currentSide:
            self.computerMove()
    
    @pyqtSignature("")
    def on_pushButton_51_clicked(self):
        """
        Slot documentation goes here.
        """
        self.__clickReaction(51)
        if not self.__isPickup and self.__isHvsC and not self.__currentSide:
            self.computerMove()
    
    @pyqtSignature("")
    def on_pushButton_86_clicked(self):
        """
        Slot documentation goes here.
        """
        self.__clickReaction(86)
        if not self.__isPickup and self.__isHvsC and not self.__currentSide:
            self.computerMove()
    
    @pyqtSignature("")
    def on_pushButton_66_clicked(self):
        """
        Slot documentation goes here.
        """
        self.__clickReaction(66)
        if not self.__isPickup and self.__isHvsC and not self.__currentSide:
            self.computerMove()
    
    @pyqtSignature("")
    def on_pushButton_75_clicked(self):
        """
        Slot documentation goes here.
        """
        self.__clickReaction(75)
        if not self.__isPickup and self.__isHvsC and not self.__currentSide:
            self.computerMove()
    
    @pyqtSignature("")
    def on_pushButton_53_clicked(self):
        """
        Slot documentation goes here.
        """
        self.__clickReaction(53)
        if not self.__isPickup and self.__isHvsC and not self.__currentSide:
            self.computerMove()
    
    @pyqtSignature("")
    def on_pushButton_71_clicked(self):
        """
        Slot documentation goes here.
        """
        self.__clickReaction(71)
        if not self.__isPickup and self.__isHvsC and not self.__currentSide:
            self.computerMove()
    
    @pyqtSignature("")
    def on_pushButton_97_clicked(self):
        """
        Slot documentation goes here.
        """
        self.__clickReaction(97)
        if not self.__isPickup and self.__isHvsC and not self.__currentSide:
            self.computerMove()
    
    @pyqtSignature("")
    def on_pushButton_59_clicked(self):
        """
        Slot documentation goes here.
        """
        self.__clickReaction(59)
        if not self.__isPickup and self.__isHvsC and not self.__currentSide:
            self.computerMove()
    
    @pyqtSignature("")
    def on_pushButton_58_clicked(self):
        """
        Slot documentation goes here.
        """
        self.__clickReaction(58)
        if not self.__isPickup and self.__isHvsC and not self.__currentSide:
            self.computerMove()
    
    @pyqtSignature("")
    def on_pushButton_98_clicked(self):
        """
        Slot documentation goes here.
        """
        self.__clickReaction(98)
        if not self.__isPickup and self.__isHvsC and not self.__currentSide:
            self.computerMove()
    
    @pyqtSignature("")
    def on_pushButton_79_clicked(self):
        """
        Slot documentation goes here.
        """
        self.__clickReaction(79)
        if not self.__isPickup and self.__isHvsC and not self.__currentSide:
            self.computerMove()
    
    @pyqtSignature("")
    def on_pushButton_62_clicked(self):
        """
        Slot documentation goes here.
        """
        self.__clickReaction(62)
        if not self.__isPickup and self.__isHvsC and not self.__currentSide:
            self.computerMove()
    
    @pyqtSignature("")
    def on_pushButton_89_clicked(self):
        """
        Slot documentation goes here.
        """
        self.__clickReaction(89)
        if not self.__isPickup and self.__isHvsC and not self.__currentSide:
            self.computerMove()
    
    @pyqtSignature("")
    def on_pushButton_63_clicked(self):
        """
        Slot documentation goes here.
        """
        self.__clickReaction(63)
        if not self.__isPickup and self.__isHvsC and not self.__currentSide:
            self.computerMove()
    
    @pyqtSignature("")
    def on_pushButton_88_clicked(self):
        """
        Slot documentation goes here.
        """
        self.__clickReaction(88)
        if not self.__isPickup and self.__isHvsC and not self.__currentSide:
            self.computerMove()
    
    @pyqtSignature("")
    def on_pushButton_96_clicked(self):
        """
        Slot documentation goes here.
        """
        self.__clickReaction(96)
        if not self.__isPickup and self.__isHvsC and not self.__currentSide:
            self.computerMove()
    
    @pyqtSignature("")
    def on_pushButton_67_clicked(self):
        """
        Slot documentation goes here.
        """
        self.__clickReaction(67)
        if not self.__isPickup and self.__isHvsC and not self.__currentSide:
            self.computerMove()
    
    @pyqtSignature("")
    def on_pushButton_95_clicked(self):
        """
        Slot documentation goes here.
        """
        self.__clickReaction(95)
        if not self.__isPickup and self.__isHvsC and not self.__currentSide:
            self.computerMove()
    
    @pyqtSignature("")
    def on_pushButton_52_clicked(self):
        """
        Slot documentation goes here.
        """
        self.__clickReaction(52)
        if not self.__isPickup and self.__isHvsC and not self.__currentSide:
            self.computerMove()
    
    @pyqtSignature("")
    def on_pushButton_56_clicked(self):
        """
        Slot documentation goes here.
        """
        self.__clickReaction(56)
        if not self.__isPickup and self.__isHvsC and not self.__currentSide:
            self.computerMove()
    
    @pyqtSignature("")
    def on_pushButton_72_clicked(self):
        """
        Slot documentation goes here.
        """
        self.__clickReaction(72)
        if not self.__isPickup and self.__isHvsC and not self.__currentSide:
            self.computerMove()
    
    @pyqtSignature("")
    def on_pushButton_69_clicked(self):
        """
        Slot documentation goes here.
        """
        self.__clickReaction(69)
        if not self.__isPickup and self.__isHvsC and not self.__currentSide:
            self.computerMove()
    
    @pyqtSignature("")
    def on_pushButton_32_clicked(self):
        """
        Slot documentation goes here.
        """
        self.__clickReaction(32)
        if not self.__isPickup and self.__isHvsC and not self.__currentSide:
            self.computerMove()
    
    @pyqtSignature("")
    def on_pushButton_44_clicked(self):
        """
        Slot documentation goes here.
        """
        self.__clickReaction(44)
        if not self.__isPickup and self.__isHvsC and not self.__currentSide:
            self.computerMove()
    
    @pyqtSignature("")
    def on_pushButton_28_clicked(self):
        """
        Slot documentation goes here.
        """
        self.__clickReaction(28)
        if not self.__isPickup and self.__isHvsC and not self.__currentSide:
            self.computerMove()
    
    @pyqtSignature("")
    def on_pushButton_11_clicked(self):
        """
        Slot documentation goes here.
        """
        self.__clickReaction(11)
        if not self.__isPickup and self.__isHvsC and not self.__currentSide:
            self.computerMove()
    
    @pyqtSignature("")
    def on_pushButton_34_clicked(self):
        """
        Slot documentation goes here.
        """
        self.__clickReaction(34)
        if not self.__isPickup and self.__isHvsC and not self.__currentSide:
            self.computerMove()
    
    @pyqtSignature("")
    def on_pushButton_33_clicked(self):
        """
        Slot documentation goes here.
        """
        self.__clickReaction(33)
        if not self.__isPickup and self.__isHvsC and not self.__currentSide:
            self.computerMove()
    
    @pyqtSignature("")
    def on_pushButton_27_clicked(self):
        """
        Slot documentation goes here.
        """
        self.__clickReaction(27)
        if not self.__isPickup and self.__isHvsC and not self.__currentSide:
            self.computerMove()
    
    @pyqtSignature("")
    def on_pushButton_43_clicked(self):
        """
        Slot documentation goes here.
        """
        self.__clickReaction(43)
        if not self.__isPickup and self.__isHvsC and not self.__currentSide:
            self.computerMove()
    
    @pyqtSignature("")
    def on_pushButton_04_clicked(self):
        """
        Slot documentation goes here.
        """
        self.__clickReaction(4)
        if not self.__isPickup and self.__isHvsC and not self.__currentSide:
            self.computerMove()
    
    @pyqtSignature("")
    def on_pushButton_23_clicked(self):
        """
        Slot documentation goes here.
        """
        self.__clickReaction(23)
        if not self.__isPickup and self.__isHvsC and not self.__currentSide:
            self.computerMove()
    
    @pyqtSignature("")
    def on_pushButton_42_clicked(self):
        """
        Slot documentation goes here.
        """
        self.__clickReaction(42)
        if not self.__isPickup and self.__isHvsC and not self.__currentSide:
            self.computerMove()
    
    @pyqtSignature("")
    def on_pushButton_14_clicked(self):
        """
        Slot documentation goes here.
        """
        self.__clickReaction(14)
        if not self.__isPickup and self.__isHvsC and not self.__currentSide:
            self.computerMove()
    
    @pyqtSignature("")
    def on_pushButton_26_clicked(self):
        """
        Slot documentation goes here.
        """
        self.__clickReaction(26)
        if not self.__isPickup and self.__isHvsC and not self.__currentSide:
            self.computerMove()
    
    @pyqtSignature("")
    def on_pushButton_24_clicked(self):
        """
        Slot documentation goes here.
        """
        self.__clickReaction(24)
        if not self.__isPickup and self.__isHvsC and not self.__currentSide:
            self.computerMove()
    
    @pyqtSignature("")
    def on_pushButton_07_clicked(self):
        """
        Slot documentation goes here.
        """
        self.__clickReaction(7)
        if not self.__isPickup and self.__isHvsC and not self.__currentSide:
            self.computerMove()
    
    @pyqtSignature("")
    def on_pushButton_41_clicked(self):
        """
        Slot documentation goes here.
        """
        self.__clickReaction(41)
        if not self.__isPickup and self.__isHvsC and not self.__currentSide:
            self.computerMove()
    
    @pyqtSignature("")
    def on_pushButton_49_clicked(self):
        """
        Slot documentation goes here.
        """
        self.__clickReaction(49)
        if not self.__isPickup and self.__isHvsC and not self.__currentSide:
            self.computerMove()
    
    @pyqtSignature("")
    def on_pushButton_18_clicked(self):
        """
        Slot documentation goes here.
        """
        self.__clickReaction(18)
        if not self.__isPickup and self.__isHvsC and not self.__currentSide:
            self.computerMove()
    
    @pyqtSignature("")
    def on_pushButton_37_clicked(self):
        """
        Slot documentation goes here.
        """
        self.__clickReaction(37)
        if not self.__isPickup and self.__isHvsC and not self.__currentSide:
            self.computerMove()
    
    @pyqtSignature("")
    def on_pushButton_31_clicked(self):
        """
        Slot documentation goes here.
        """
        self.__clickReaction(31)
        if not self.__isPickup and self.__isHvsC and not self.__currentSide:
            self.computerMove()
    
    @pyqtSignature("")
    def on_pushButton_36_clicked(self):
        """
        Slot documentation goes here.
        """
        self.__clickReaction(36)
        if not self.__isPickup and self.__isHvsC and not self.__currentSide:
            self.computerMove()
    
    @pyqtSignature("")
    def on_pushButton_25_clicked(self):
        """
        Slot documentation goes here.
        """
        self.__clickReaction(25)
        if not self.__isPickup and self.__isHvsC and not self.__currentSide:
            self.computerMove()
    
    @pyqtSignature("")
    def on_pushButton_16_clicked(self):
        """
        Slot documentation goes here.
        """
        self.__clickReaction(16)
        if not self.__isPickup and self.__isHvsC and not self.__currentSide:
            self.computerMove()
    
    @pyqtSignature("")
    def on_pushButton_03_clicked(self):
        """
        Slot documentation goes here.
        """
        self.__clickReaction(3)
        if not self.__isPickup and self.__isHvsC and not self.__currentSide:
            self.computerMove()
    
    @pyqtSignature("")
    def on_pushButton_47_clicked(self):
        """
        Slot documentation goes here.
        """
        self.__clickReaction(47)
        if not self.__isPickup and self.__isHvsC and not self.__currentSide:
            self.computerMove()
    
    @pyqtSignature("")
    def on_pushButton_21_clicked(self):
        """
        Slot documentation goes here.
        """
        self.__clickReaction(21)
        if not self.__isPickup and self.__isHvsC and not self.__currentSide:
            self.computerMove()
    
    @pyqtSignature("")
    def on_pushButton_09_clicked(self):
        """
        Slot documentation goes here.
        """
        self.__clickReaction(9)
        if not self.__isPickup and self.__isHvsC and not self.__currentSide:
            self.computerMove()
    
    @pyqtSignature("")
    def on_pushButton_08_clicked(self):
        """
        Slot documentation goes here.
        """
        self.__clickReaction(8)
        if not self.__isPickup and self.__isHvsC and not self.__currentSide:
            self.computerMove()
    
    @pyqtSignature("")
    def on_pushButton_48_clicked(self):
        """
        Slot documentation goes here.
        """
        self.__clickReaction(48)
        if not self.__isPickup and self.__isHvsC and not self.__currentSide:
            self.computerMove()
    
    @pyqtSignature("")
    def on_pushButton_29_clicked(self):
        """
        Slot documentation goes here.
        """
        self.__clickReaction(29)
        if not self.__isPickup and self.__isHvsC and not self.__currentSide:
            self.computerMove()
    
    @pyqtSignature("")
    def on_pushButton_12_clicked(self):
        """
        Slot documentation goes here.
        """
        self.__clickReaction(12)
        if not self.__isPickup and self.__isHvsC and not self.__currentSide:
            self.computerMove()
    
    @pyqtSignature("")
    def on_pushButton_39_clicked(self):
        """
        Slot documentation goes here.
        """
        self.__clickReaction(39)
        if not self.__isPickup and self.__isHvsC and not self.__currentSide:
            self.computerMove()
    
    @pyqtSignature("")
    def on_pushButton_19_clicked(self):
        """
        Slot documentation goes here.
        """
        self.__clickReaction(19)
        if not self.__isPickup and self.__isHvsC and not self.__currentSide:
            self.computerMove()
    
    @pyqtSignature("")
    def on_pushButton_13_clicked(self):
        """
        Slot documentation goes here.
        """
        self.__clickReaction(13)
        if not self.__isPickup and self.__isHvsC and not self.__currentSide:
            self.computerMove()
    
    @pyqtSignature("")
    def on_pushButton_38_clicked(self):
        """
        Slot documentation goes here.
        """
        self.__clickReaction(38)
        if not self.__isPickup and self.__isHvsC and not self.__currentSide:
            self.computerMove()
    
    @pyqtSignature("")
    def on_pushButton_05_clicked(self):
        """
        Slot documentation goes here.
        """
        self.__clickReaction(5)
        if not self.__isPickup and self.__isHvsC and not self.__currentSide:
            self.computerMove()
    
    @pyqtSignature("")
    def on_pushButton_46_clicked(self):
        """
        Slot documentation goes here.
        """
        self.__clickReaction(46)
        if not self.__isPickup and self.__isHvsC and not self.__currentSide:
            self.computerMove()
    
    @pyqtSignature("")
    def on_pushButton_17_clicked(self):
        """
        Slot documentation goes here.
        """
        self.__clickReaction(17)
        if not self.__isPickup and self.__isHvsC and not self.__currentSide:
            self.computerMove()
    
    @pyqtSignature("")
    def on_pushButton_45_clicked(self):
        """
        Slot documentation goes here.
        """
        self.__clickReaction(45)
        if not self.__isPickup and self.__isHvsC and not self.__currentSide:
            self.computerMove()
    
    @pyqtSignature("")
    def on_pushButton_02_clicked(self):
        """
        Slot documentation goes here.
        """
        self.__clickReaction(2)
        if not self.__isPickup and self.__isHvsC and not self.__currentSide:
            self.computerMove()
    
    @pyqtSignature("")
    def on_pushButton_06_clicked(self):
        """
        Slot documentation goes here.
        """
        self.__clickReaction(6)
        if not self.__isPickup and self.__isHvsC and not self.__currentSide:
            self.computerMove()
    
    @pyqtSignature("")
    def on_pushButton_22_clicked(self):
        """
        Slot documentation goes here.
        """
        self.__clickReaction(22)
        if not self.__isPickup and self.__isHvsC and not self.__currentSide:
            self.computerMove()
    
    @pyqtSignature("")
    def on_pushButton_15_clicked(self):
        """
        Slot documentation goes here.
        """
        self.__clickReaction(15)
        if not self.__isPickup and self.__isHvsC and not self.__currentSide:
            self.computerMove()

if __name__ == "__main__":     
        app = PyQt4.QtGui.QApplication(sys.argv)     
        w = MainWindow()
        w.show()
        sys.exit(app.exec_())
    
