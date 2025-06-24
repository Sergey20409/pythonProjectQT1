import json
from PySide6.QtWidgets import (QApplication, QMainWindow, QTableWidget,
                             QTableWidgetItem, QPushButton, QVBoxLayout,
                             QWidget, QFileDialog)


class TableWidgetExample(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('TableWidget и JSON')
        self.setGeometry(100, 100, 600, 400)

        # Создаем таблицу
        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(['Заметка', 'Дата создания', 'Дата выполнения'])

        # Кнопки для управления
        self.add_btn = QPushButton('Добавить строку')
        self.add_btn.clicked.connect(self.add_row)

        self.save_btn = QPushButton('Сохранить в JSON')
        self.save_btn.clicked.connect(self.save_to_json)

        self.load_btn = QPushButton('Загрузить из JSON')
        self.load_btn.clicked.connect(self.load_from_json)

        # Размещаем элементы
        layout = QVBoxLayout()
        layout.addWidget(self.table)
        layout.addWidget(self.add_btn)
        layout.addWidget(self.save_btn)
        layout.addWidget(self.load_btn)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def add_row(self):
        """Добавляет новую строку в таблицу"""
        row_position = self.table.rowCount()
        self.table.insertRow(row_position)

        # Устанавливаем значения по умолчанию
        self.table.setItem(row_position, 0, QTableWidgetItem("Новая заметка"))
        self.table.setItem(row_position, 1, QTableWidgetItem("Дата создания"))
        self.table.setItem(row_position, 2, QTableWidgetItem("Дата выполнения"))

    def save_to_json(self):
        """Сохраняет данные таблицы в JSON файл"""
        data = []

        # Собираем данные из таблицы
        for row in range(self.table.rowCount()):
            row_data = {
                'list': self.table.item(row, 0).text(),
                'BornDay': self.table.item(row, 1).text(),
                'FinalDay': self.table.item(row, 2).text()
            }
            data.append(row_data)

        # Запрашиваем путь для сохранения
        file_path, _ = QFileDialog.getSaveFileName(
            self, 'Сохранить файл', '', 'JSON Files (*.json)')

        if file_path:
            # Сохраняем в файл
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)

    def load_from_json(self):
        """Загружает данные из JSON файла в таблицу"""
        # Запрашиваем путь к файлу
        file_path, _ = QFileDialog.getOpenFileName(
            self, 'Открыть файл', '', 'JSON Files (*.json)')

        if file_path:
            # Очищаем таблицу
            self.table.setRowCount(0)

            # Загружаем данные из файла
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)

                # Заполняем таблицу
                for row_data in data:
                    row_position = self.table.rowCount()
                    self.table.insertRow(row_position)

                    self.table.setItem(row_position, 0,
                                       QTableWidgetItem(row_data.get('name', '')))
                    self.table.setItem(row_position, 1,
                                       QTableWidgetItem(str(row_data.get('age', ''))))
                    self.table.setItem(row_position, 2,
                                       QTableWidgetItem(row_data.get('city', '')))


if __name__ == '__main__':
    app = QApplication([])
    window = TableWidgetExample()
    window.show()
    app.exec_()