# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Note.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
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
        widget.resize(637, 412)
        self.widget1 = QWidget(widget)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(27, 14, 574, 355))
        self.gridLayout = QGridLayout(self.widget1)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget1)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.plainTextEdit = QPlainTextEdit(self.widget1)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.gridLayout.addWidget(self.plainTextEdit, 1, 0, 1, 3)

        self.calendarWidget = QCalendarWidget(self.widget1)
        self.calendarWidget.setObjectName(u"calendarWidget")

        self.gridLayout.addWidget(self.calendarWidget, 1, 3, 1, 1)

        self.pushButton_2 = QPushButton(self.widget1)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(75, 71))
        font = QFont()
        font.setBold(True)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet(u"color: rgb(255, 0, 0);\n"
"")

        self.gridLayout.addWidget(self.pushButton_2, 2, 0, 2, 1)

        self.label_2 = QLabel(self.widget1)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 1, 1, 1)

        self.dateEdit = QDateEdit(self.widget1)
        self.dateEdit.setObjectName(u"dateEdit")

        self.gridLayout.addWidget(self.dateEdit, 2, 2, 1, 1)

        self.pushButton = QPushButton(self.widget1)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 2, 3, 1, 1)

        self.label_3 = QLabel(self.widget1)
        self.label_3.setObjectName(u"label_3")
        font1 = QFont()
        font1.setPointSize(14)
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.gridLayout.addWidget(self.label_3, 3, 1, 1, 3)

        self.pushButton_3 = QPushButton(self.widget1)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout.addWidget(self.pushButton_3, 4, 0, 1, 1)


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
        self.pushButton_3.setText(QCoreApplication.translate("widget", u"\u0412\u044b\u0437\u0432\u0430\u0442\u044c\n"
"\u043f\u043e\u0441\u043b\u0435\u0434\u043d\u0438\u0439\n"
"\u0441\u043e\u0445\u0440\u0430\u043d\u0435\u043d\u043d\u044b\u0439", None))
    # retranslateUi

