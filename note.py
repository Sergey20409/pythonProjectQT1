# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'note.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
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
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QDateEdit, QGridLayout,
    QLabel, QPlainTextEdit, QPushButton, QSizePolicy,
    QWidget)

class Ui_widget(object):
    def setupUi(self, widget):
        if not widget.objectName():
            widget.setObjectName(u"widget")
        widget.resize(608, 347)
        self.layoutWidget = QWidget(widget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(26, 13, 520, 293))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.plainTextEdit = QPlainTextEdit(self.layoutWidget)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.gridLayout.addWidget(self.plainTextEdit, 1, 0, 1, 3)

        self.calendarWidget = QCalendarWidget(self.layoutWidget)
        self.calendarWidget.setObjectName(u"calendarWidget")

        self.gridLayout.addWidget(self.calendarWidget, 1, 3, 1, 2)

        self.pushButton_2 = QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(75, 71))
        font = QFont()
        font.setBold(True)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet(u"color: rgb(255, 0, 0);\n"
"")

        self.gridLayout.addWidget(self.pushButton_2, 2, 0, 2, 1)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 1, 1, 1)

        self.dateEdit = QDateEdit(self.layoutWidget)
        self.dateEdit.setObjectName(u"dateEdit")

        self.gridLayout.addWidget(self.dateEdit, 2, 2, 1, 2)

        self.pushButton = QPushButton(self.layoutWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 2, 4, 1, 1)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        font1 = QFont()
        font1.setPointSize(14)
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.gridLayout.addWidget(self.label_3, 3, 1, 1, 4)


        self.retranslateUi(widget)

        QMetaObject.connectSlotsByName(widget)
    # setupUi

    def retranslateUi(self, widget):
        widget.setWindowTitle(QCoreApplication.translate("widget", u"\u0417\u0430\u043c\u0435\u0442\u043a\u0438", None))
        self.label.setText(QCoreApplication.translate("widget", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0442\u0435\u043a\u0441\u0442 \u0437\u0430\u043c\u0435\u0442\u043a\u0438", None))
        self.pushButton_2.setText(QCoreApplication.translate("widget", u"\u0421\u0442\u0435\u0440\u0435\u0442\u044c", None))
        self.label_2.setText(QCoreApplication.translate("widget", u"\u0414\u0430\u0442\u0430 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f", None))
        self.pushButton.setText(QCoreApplication.translate("widget", u"\u0417\u0430\u043f\u0438\u0441\u0430\u0442\u044c", None))
        self.label_3.setText(QCoreApplication.translate("widget", u"\u0414\u043e \u0432\u0440\u0435\u043c\u0435\u043d\u0438 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f \u043e\u0441\u0442\u0430\u043b\u043e\u0441\u044c \u0425 \u0434\u043d\u0435\u0439", None))
    # retranslateUi

