from PySide6.QtWidgets import (QVBoxLayout, QWidget, QLabel,
                               QMainWindow, QTableWidget, QTableWidgetItem,
                               QPushButton, QVBoxLayout, QWidget, QFileDialog, QMessageBox)
from PySide6.QtCore import QDate, Qt
from PySide6.QtGui import QColor, QBrush, QPen, QFont
from note import Ui_widget
from PySide6 import QtWidgets, QtCore
import json
import datetime


class Window(QtWidgets.QWidget,Ui_widget):

    def initUi(self) -> None:
        self.pushButton_4 = QPushButton('Добавить строку')
        self.pushButton = QPushButton('Записать в JSON')
        self.pushButton_5 = QPushButton('Загрузить из JSON')
        self.pushButton_3 = QPushButton('Установить в таблицу')
        self.pushButton_Del = QPushButton('Удалить строку')

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setupUi(self)
        self.initSignals()
        self.Current_Date()    # Устанавливаем календарь на текущую дату

    def Current_Date(self): # Устанавливаем календарь на текущую дату
        self.dateEdit.setDate(QDate.currentDate())
        self.calendarWidget.setSelectedDate(QDate.currentDate())


    def initSignals(self):
        self.pushButton.clicked.connect(self.onPushButtonClicked)
        self.calendarWidget.clicked.connect(self.onCalendar)
        self.dateEdit.dateChanged.connect(self.on_dateEdit_Change)
        self.pushButton_2.clicked.connect(self.onPushButton_2Clicked)
        self.pushButton_4.clicked.connect(self.onPushButton_4Clicked)
        self.pushButton_5.clicked.connect(self.onPushButton_5Clicked)
        self.pushButton_3.clicked.connect(self.onPushButton_3Clicked)
        self.pushButton_Del.clicked.connect(self.onPushButton_DelClicked)

    def onCalendar(self): # Делаем чтобы выбранная дата в листе календаря появлялась в числовом показометре слева
        global start_date, calc_date
        self.dateEdit.setDate(self.calendarWidget.selectedDate())
        start_date = QDate.currentDate()
        calc_date = self.calendarWidget.selectedDate()

    def on_dateEdit_Change(self):# Наоборот - чтобы выбранная дата в показометре появлялась в листике календарика
        global delta_days

        self.calendarWidget.setSelectedDate(self.dateEdit.date())
        start_date = QDate.currentDate()
        calc_date = self.dateEdit.date()
        delta_days = start_date.daysTo(calc_date)

        if delta_days < 0:
            self.label.setText("Время исполнения прошло \n%s дней назад" % abs(delta_days))
        else:
            self.label.setText("До времени выполнения осталось \n%s дней" % delta_days)

    # def onPushButtonClicked(self):
        # print(QDate.currentDate().toString('dd-MM-yyyy'))
        # print(self.calendarWidget.selectedDate().toString('dd-MM-yyyy'))


    def onPushButton_4Clicked(self): # Добавляем строки
        row_position = self.tableWidget.rowCount()
        self.tableWidget.insertRow(row_position)

        # self.pushButton_4.clicked.connect(self.add_row)

    def onPushButton_3Clicked(self):  # Нажимаем для переноса дат в таблицу

        self.calendarWidget.setSelectedDate(self.dateEdit.date())
        start_date = QDate.currentDate()
        calc_date = self.dateEdit.date()
        delta_days = start_date.daysTo(calc_date)


        table = self.tableWidget  # ваш QTableWidget

        if table.rowCount() <= 0:
            QMessageBox.warning(self, 'Ошибка',
                                'Добавьте новые строки с помощью кнопки "Добавить новую строку".')

        selected_rows = set(index.row() for index in self.tableWidget.selectedIndexes())
        if not selected_rows:
            QMessageBox.warning(self, 'Ошибка', 'Не выбрана ни одна строка')
            return

        # Добавляем дату в последний столбец выбранных строк
        for row in selected_rows:
            # Проверяем, что строка существует в таблице
            if row < self.tableWidget.rowCount():
                self.tableWidget.setItem(row, 1, QTableWidgetItem(QDate.currentDate().toString('dd-MM-yyyy')))
                self.tableWidget.setItem(row, 2, QTableWidgetItem(self.calendarWidget.selectedDate().toString('dd-MM-yyyy')))
                self.tableWidget.setItem(row, 3, QTableWidgetItem(str(delta_days)))


        # print(QDate.currentDate().toString('dd-MM-yyyy'))
        # print(self.calendarWidget.selectedDate().toString('dd-MM-yyyy'))
        # print(delta_days)

    def onPushButtonClicked(self): # Сохраняем в файл
        data = []
        # Собираем данные из таблицы
        for row in range(self.tableWidget.rowCount()):
            row_data = {
                'list': self.tableWidget.item(row, 0).text(),
                'BornDay': self.tableWidget.item(row, 1).text(),
                'FinalDay': self.tableWidget.item(row, 2).text(),
                'DeadLine': self.tableWidget.item(row, 3).text()
            }
            data.append(row_data)

        # Запрашиваем путь для сохранения
        file_path, _ = QFileDialog.getSaveFileName(
            self, 'Сохранить файл', '', 'JSON Files (*.json)')

        if file_path: # Сохраняем в файл
            try:

                with open(file_path, 'w', encoding='utf-8') as f:
                    json.dump(data, f, ensure_ascii=False, indent=4)
                QMessageBox.information(self, "Успех", "Данные успешно сохранены")
            except Exception as e:
                QMessageBox.critical(self, "Ошибка", f"Не удалось сохранить файл: {str(e)}")

        # self.pushButton.clicked.connect(self.save_to_json)

    def onPushButton_5Clicked(self): # Загружаем файл

        # self.pushButton_5.clicked.connect(self.load_from_json)
        file_path, _ = QFileDialog.getOpenFileName(
            self, 'Открыть файл', '', 'JSON Files (*.json)')

        if file_path:
            # Очищаем таблицу
            self.tableWidget.setRowCount(0)

            # Загружаем данные из файла
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)

                # Заполняем таблицу
                for row_data in data:
                    row_position = self.tableWidget.rowCount()
                    self.tableWidget.insertRow(row_position)

                    self.tableWidget.setItem(row_position, 0, QTableWidgetItem(row_data.get('list', '')))
                    self.tableWidget.setItem(row_position, 1, QTableWidgetItem(str(row_data.get('BornDay', ''))))
                    self.tableWidget.setItem(row_position, 2, QTableWidgetItem(str(row_data.get('FinalDay', ''))))
                    delta = (datetime.datetime.strptime(row_data.get('FinalDay'), "%d-%m-%Y") - datetime.datetime.now()).days
                    self.tableWidget.setItem(row_position, 3, QTableWidgetItem(str(delta + 1)))

    def onPushButton_2Clicked(self):  # Обнуляем дату на текущую
        self.Current_Date()

    def onPushButton_DelClicked(self): # Удаляем выбранную строку
        current_row = self.tableWidget.currentRow()

        if current_row >= 0:
            self.tableWidget.removeRow(current_row)
        else:
            QMessageBox.warning(self, "Предупреждение", "Пожалуйста, выберите строку для удаления")


if __name__ == '__main__':
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
