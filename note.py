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
    QHeaderView, QLabel, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_widget(object):
    def setupUi(self, widget):
        if not widget.objectName():
            widget.setObjectName(u"widget")
        widget.resize(706, 456)
        self.verticalLayout = QVBoxLayout(widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.calendarWidget = QCalendarWidget(widget)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setSelectedDate(QDate(2025, 6, 25))

        self.gridLayout.addWidget(self.calendarWidget, 0, 0, 3, 2)

        self.label_2 = QLabel(widget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)

        self.dateEdit = QDateEdit(widget)
        self.dateEdit.setObjectName(u"dateEdit")

        self.gridLayout.addWidget(self.dateEdit, 0, 3, 1, 2)

        self.label = QLabel(widget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.label.setTextFormat(Qt.TextFormat.PlainText)

        self.gridLayout.addWidget(self.label, 1, 2, 1, 3)

        self.pushButton_3 = QPushButton(widget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setEnabled(True)
        self.pushButton_3.setMinimumSize(QSize(75, 50))
        font = QFont()
        font.setBold(True)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet(u"color: rgb(255, 0, 0);\n"
"")

        self.gridLayout.addWidget(self.pushButton_3, 2, 2, 1, 2)

        self.pushButton_2 = QPushButton(widget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setEnabled(True)
        self.pushButton_2.setMinimumSize(QSize(75, 50))
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet(u"color: rgb(255, 0, 0);\n"
"")

        self.gridLayout.addWidget(self.pushButton_2, 2, 4, 1, 1)

        self.tableWidget = QTableWidget(widget)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setStretchLastSection(False)

        self.gridLayout.addWidget(self.tableWidget, 3, 0, 1, 5)

        self.pushButton_4 = QPushButton(widget)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.gridLayout.addWidget(self.pushButton_4, 4, 0, 1, 1)

        self.pushButton = QPushButton(widget)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 4, 1, 1, 1)

        self.pushButton_5 = QPushButton(widget)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.gridLayout.addWidget(self.pushButton_5, 4, 2, 1, 1)

        self.pushButton_Del = QPushButton(widget)
        self.pushButton_Del.setObjectName(u"pushButton_Del")

        self.gridLayout.addWidget(self.pushButton_Del, 4, 3, 1, 2)


        self.verticalLayout.addLayout(self.gridLayout)


        self.retranslateUi(widget)

        QMetaObject.connectSlotsByName(widget)
    # setupUi

    def retranslateUi(self, widget):
        widget.setWindowTitle(QCoreApplication.translate("widget", u"\u0417\u0430\u043c\u0435\u0442\u043a\u0438", None))
        self.label_2.setText(QCoreApplication.translate("widget", u"\u0414\u0430\u0442\u0430 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f", None))
        self.label.setText(QCoreApplication.translate("widget", u"\u0414\u043e \u0432\u0440\u0435\u043c\u0435\u043d\u0438 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f \u043e\u0441\u0442\u0430\u043b\u043e\u0441\u044c \n"
" \u0425 \u0434\u043d\u0435\u0439", None))
        self.pushButton_3.setText(QCoreApplication.translate("widget", u"\u0423\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u044c \u0432\u044b\u0431\u0440\u0430\u043d\u043d\u044b\u0435\n"
"\u0434\u0430\u0442\u044b \u0432 \u0442\u0430\u0431\u043b\u0438\u0446\u0443", None))
        self.pushButton_2.setText(QCoreApplication.translate("widget", u"\u0421\u0431\u0440\u043e\u0441\u0438\u0442\u044c", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("widget", u"\u0417\u0430\u043c\u0435\u0442\u043a\u0430", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("widget", u"\u0414\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("widget", u"\u0414\u0430\u0442\u0430 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("widget", u"\u041e\u0441\u0442\u0430\u043b\u043e\u0441\u044c \u0434\u043d\u0435\u0439", None));
        self.pushButton_4.setText(QCoreApplication.translate("widget", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0441\u0442\u0440\u043e\u043a\u0443", None))
        self.pushButton.setText(QCoreApplication.translate("widget", u"\u0417\u0430\u043f\u0438\u0441\u0430\u0442\u044c \u0432 JSON", None))
        self.pushButton_5.setText(QCoreApplication.translate("widget", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0438\u0437 JSON", None))
        self.pushButton_Del.setText(QCoreApplication.translate("widget", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0441\u0442\u0440\u043e\u043a\u0443", None))
    # retranslateUi

