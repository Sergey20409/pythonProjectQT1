from PySide6.QtWidgets import (QVBoxLayout, QWidget, QLabel,
                               QMainWindow, QTableWidget, QTableWidgetItem,
                               QPushButton, QVBoxLayout, QWidget, QFileDialog, QMessageBox)
from PySide6.QtCore import QDate, Qt
from PySide6.QtGui import QColor, QBrush, QPen, QFont
from note import Ui_widget
from PySide6 import QtWidgets, QtCore
import json

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
            self.label.setText("Время исполнения прошло %s дней назад" % abs(delta_days))
        else:
            self.label.setText("До времени выполнения осталось %s дней" % delta_days)

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
                self.tableWidget.setItem(row, 3, delta_days)


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
                    self.tableWidget.setItem(row_position, 3, QTableWidgetItem(str(row_data.get('DeadLine', ''))))

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




#
# class TableWidgetExample(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#         self.Window = Window
#
#     def initUI(self):
#         self.setWindowTitle('Заметка и даты')
#         self.setGeometry(100, 100, 600, 400)
#
#         # Создаем таблицу
#         self.table = QTableWidget()
#         self.table.setColumnCount(3)
#         self.table.setHorizontalHeaderLabels(['Заметка', 'Дата создания', 'Дата выполнения'])
#
#         # Кнопки для управления
#         self.add_btn = QPushButton('Добавить строку')
#         self.add_btn.clicked.connect(self.add_row)
#
#         self.save_btn = QPushButton('Сохранить в JSON')
#         self.save_btn.clicked.connect(self.save_to_json)
#
#         self.load_btn = QPushButton('Загрузить из JSON')
#         self.load_btn.clicked.connect(self.load_from_json)
#
#         # Размещаем элементы
#         layout = QVBoxLayout()
#         layout.addWidget(self.table)
#         layout.addWidget(self.add_btn)
#         layout.addWidget(self.save_btn)
#         layout.addWidget(self.load_btn)
#
#         container = QWidget()
#         container.setLayout(layout)
#         self.setCentralWidget(container)
#
#
#     def add_row(self):
#         """Добавляет новую строку в таблицу"""
#         row_position = self.table.rowCount()
#         self.table.insertRow(row_position)



        # Устанавливаем значения по умолчанию
        # self.table.setItem(row_position, 0, QTableWidgetItem("Новая заметка"))
        # self.table.setItem(row_position, 1, QTableWidgetItem("Дата создания"))
        # self.table.setItem(row_position, 2, QTableWidgetItem("Дата выполнения"))
    #
    # def save_to_json(self):
    #     """Сохраняет данные таблицы в JSON файл"""
    #     data = []
    #
    #     # Собираем данные из таблицы
    #     for row in range(self.table.rowCount()):
    #         row_data = {
    #             'list': self.table.item(row, 0).text(),
    #             'BornDay': self.Window.QDate.currentDate().toString('dd-MM-yyyy').table.item(row, 1),
    #             'FinalDay': self.Window.calendarWidget.selectedDate().toString('dd-MM-yyyy')
    #         }
    #         data.append(row_data)
    #
    #     # Запрашиваем путь для сохранения
    #     file_path, _ = QFileDialog.getSaveFileName(
    #         self, 'Сохранить файл', '', 'JSON Files (*.json)')
    #
    #     if file_path:
    #         # Сохраняем в файл
    #         with open(file_path, 'w', encoding='utf-8') as f:
    #             json.dump(data, f, ensure_ascii=False, indent=4)
    #
    # def load_from_json(self):
    #     """Загружает данные из JSON файла в таблицу"""
    #     # Запрашиваем путь к файлу
    #     file_path, _ = QFileDialog.getOpenFileName(
    #         self, 'Открыть файл', '', 'JSON Files (*.json)')
    #
    #     if file_path:
    #         # Очищаем таблицу
    #         self.table.setRowCount(0)
    #
    #         # Загружаем данные из файла
    #         with open(file_path, 'r', encoding='utf-8') as f:
    #             data = json.load(f)
    #
    #             # Заполняем таблицу
    #             for row_data in data:
    #                 row_position = self.table.rowCount()
    #                 self.table.insertRow(row_position)
    #
    #                 self.table.setItem(row_position, 0,
    #                                    QTableWidgetItem(row_data.get('list', '')))
    #                 self.table.setItem(row_position, 1,
    #                                    QTableWidgetItem(str(row_data.get('bornday', ''))))
    #                 self.table.setItem(row_position, 2,
    #                                    QTableWidgetItem(row_data.get('finalday', '')))







    # print (self.plainTextEdit.toPlainText())
    # print(self.dateEdit.dateTime().toString('dd-MM-yyyy'))
    # print(self.calendarWidget.selectedDate().toString('dd-MM-yyyy'))
    # date = QDate(2022, 9, 17)
    # self.calendarWidget.setSelectedDate(date)


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



# class NewWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#
#         self.setWindowTitle("Новое окно")
#         self.setGeometry(200, 200, 300, 200)
#
#         # Добавляем какой-нибудь виджет в новое окно
#         label = QLabel("Это новое окно!")
#         layout = QVBoxLayout()
#         layout.addWidget(label)
#         self.setLayout(layout)

    # def open_new_window(self):
    #     # Создаем и показываем новое окно
    #     self.new_window = TableWidgetExample()
    #     self.new_window.show()


        # Создаем layout и добавляем кнопку
        # layout = QVBoxLayout()
        # layout.addWidget(self.pushButton)
# self.pushButton.clicked.connect(self.open_new_window)
# with open("Record.json", "w", encoding="utf-8") as f:
#     json.dump({"Заметка": self.plainTextEdit.toPlainText(),
#                "Дата создания": QDate.currentDate().toString('dd-MM-yyyy'),
#                "Дата выполнения": self.calendarWidget.selectedDate().toString('dd-MM-yyyy'),
#                }, f, ensure_ascii=False, indent=5)


    # def add_row(self):
    #     """Добавляет новую строку в таблицу"""
    #     row_position = self.tableWidget.rowCount()
    #     self.tableWidget.insertRow(row_position)



        # Устанавливаем значения по умолчанию
        # self.tableWidget.setItem(row_position, 0, QTableWidgetItem("Новая заметка"))
        # self.tableWidget.setItem(row_position, 1, QTableWidgetItem("Дата создания"))
        # self.tableWidget.setItem(row_position, 2, QTableWidgetItem("Дата выполнения"))
    #
    # def save_to_json(self):
    #     """Сохраняет данные таблицы в JSON файл"""
    #     data = []
    #
    #     # Собираем данные из таблицы
    #     for row in range(self.tableWidget.rowCount()):
    #         row_data = {
    #             'list': self.tableWidget.item(row, 0).text(),
    #             'BornDay': self.tableWidget.item(row, 1).text(),
    #             'FinalDay': self.tableWidget.item(row, 2).text()
    #         }
    #         data.append(row_data)
    #
    #     # Запрашиваем путь для сохранения
    #     file_path, _ = QFileDialog.getSaveFileName(
    #         self, 'Сохранить файл', '', 'JSON Files (*.json)')
    #
    #     if file_path:
    #         # Сохраняем в файл
    #         with open(file_path, 'w', encoding='utf-8') as f:
    #             json.dump(data, f, ensure_ascii=False, indent=4)

    # def load_from_json(self):
    #     """Загружает данные из JSON файла в таблицу"""
    #     # Запрашиваем путь к файлу
    #     file_path, _ = QFileDialog.getOpenFileName(
    #         self, 'Открыть файл', '', 'JSON Files (*.json)')
    #
    #     if file_path:
    #         # Очищаем таблицу
    #         self.tableWidget.setRowCount(0)
    #
    #         # Загружаем данные из файла
    #         with open(file_path, 'r', encoding='utf-8') as f:
    #             data = json.load(f)
    #
    #             # Заполняем таблицу
    #             for row_data in data:
    #                 row_position = self.tableWidget.rowCount()
    #                 self.tableWidget.insertRow(row_position)
    #
    #                 self.tableWidget.setItem(row_position, 0,
    #                                    QTableWidgetItem(row_data.get('list', '')))
    #                 self.tableWidget.setItem(row_position, 1,
    #                                    QTableWidgetItem(str(row_data.get('bornday', ''))))
    #                 self.tableWidget.setItem(row_position, 2,
    #                                    QTableWidgetItem(row_data.get('finalday', '')))