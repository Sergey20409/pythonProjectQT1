from PySide6.QtCore import QDate
from note import Ui_widget
from PySide6 import QtWidgets, QtCore
import json

class Window(QtWidgets.QWidget,Ui_widget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setupUi(self)
        self.initSignals()
        self.Current_Date()    # Устанавливаем календарь на текущую дату
        self.label.setText("Заметка от %s" % QDate.currentDate().toString('dd-MM-yyyy')) # Заголовок заметки с текущей датой

    def Current_Date(self): # Устанавливаем календарь на текущую дату
        self.dateEdit.setDate(QDate.currentDate())
        self.calendarWidget.setSelectedDate(QDate.currentDate())
        # print(QDate.currentDate().toString('dd-MM-yyyy'))


    def initSignals(self):
        self.pushButton.clicked.connect(self.onPushButtonClicked)
        self.calendarWidget.clicked.connect(self.onCalendar)
        self.dateEdit.dateChanged.connect(self.on_dateEdit_Change)
        self.pushButton_2.clicked.connect(self.onPushButton_2Clicked)




    def onCalendar(self): # Делаем чтобы выбранная дата в листе календаря появлялась в числовом показометре слева
        global star_date, calc_date
        # print(self.calendarWidget.selectedDate().toString('dd-MM-yyyy'))
        self.dateEdit.setDate(self.calendarWidget.selectedDate())
        start_date = QDate.currentDate()
        # print(start_date)
        calc_date = self.calendarWidget.selectedDate()
        delta_days = start_date.daysTo(calc_date)

        # print(calc_date)
        # print(delta_days)

    def on_dateEdit_Change(self):# Наоборот - чтобы выбранная дата в показометре появлялась в листике календарика
        global star_date, calc_date

        # print(self.dateEdit.dateTime().toString('dd-MM-yyyy'))
        self.calendarWidget.setSelectedDate(self.dateEdit.date())
        start_date = QDate.currentDate()
        calc_date = self.dateEdit.date()
        delta_days = start_date.daysTo(calc_date)
        if delta_days < 0:
            self.label_3.setText("Время исполнения прошло %s дней назад" % abs(delta_days))
        else:
            self.label_3.setText("До времени выполнения осталось %s дней" % delta_days)

        # print(start_date)
        # print(calc_date)
        # print(delta_days)

    def onPushButtonClicked(self):

        with open("Record.json", "w", encoding="utf-8") as f:
            json.dump({"Заметка": self.plainTextEdit.toPlainText(),
                       "Дата создания": QDate.currentDate().toString('dd-MM-yyyy'),
                       "Дата выполнения": self.calendarWidget.selectedDate().toString('dd-MM-yyyy'),
                       }, f, ensure_ascii=False, indent=5)
        # print (self.plainTextEdit.toPlainText())
        # print(QDate.currentDate().toString('dd-MM-yyyy'))
        # print(self.calendarWidget.selectedDate().toString('dd-MM-yyyy'))


    def onPushButton_2Clicked(self): # Стираем текст в поле и обнуляем дату на текущую
        self.plainTextEdit.clear()
        self.Current_Date()


    # def save_textedit_content(textEdit):
    #     with open("widget_textedit.json", "w") as f:
    #         json.dump({"content": textEdit.toPlainText()}, f)

    # def load_textedit_content(textEdit):
    #     try:
    #         with open("widget_textedit.json", "r") as f:
    #             data = json.load(f)
    #             textEdit.setPlainText(data.get("content", ""))
    #     except FileNotFoundError:
    #         pass


if __name__ == '__main__':
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()



    # print (self.plainTextEdit.toPlainText())
    # print(self.dateEdit.dateTime().toString('dd-MM-yyyy'))
    # print(self.calendarWidget.selectedDate().toString('dd-MM-yyyy'))
    # date = QDate(2022, 9, 17)
    # self.calendarWidget.setSelectedDate(date)