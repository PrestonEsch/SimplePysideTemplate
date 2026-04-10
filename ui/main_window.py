# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(804, 613)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.scoreLabel = QLabel(self.centralwidget)
        self.scoreLabel.setObjectName(u"scoreLabel")
        self.scoreLabel.setGeometry(QRect(20, 40, 191, 61))
        self.addScoreButton = QPushButton(self.centralwidget)
        self.addScoreButton.setObjectName(u"addScoreButton")
        self.addScoreButton.setGeometry(QRect(10, 20, 181, 26))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Window", None))
        self.scoreLabel.setText(QCoreApplication.translate("MainWindow", u"Score: 0", None))
        self.addScoreButton.setText(QCoreApplication.translate("MainWindow", u"Click for +? Score", None))
    # retranslateUi

