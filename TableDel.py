import sys
import json
from PySide6.QtWidgets import (QApplication, QMainWindow, QTableWidget,
                             QTableWidgetItem, QVBoxLayout, QWidget,
                             QPushButton, QFileDialog, QMessageBox)
from PySide6.QtCore import Qt


class TableWidgetDemo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QTableWidget с JSON")
        self.setGeometry(100, 100, 600, 400)

        # Создаем центральный виджет и layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Создаем таблицу
        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["Имя", "Возраст", "Email"])
        self.table.setRowCount(0)

        # Кнопки для управления
        self.add_button = QPushButton("Добавить строку")
        self.add_button.clicked.connect(self.add_row)

        self.delete_button = QPushButton("Удалить выбранную строку")
        self.delete_button.clicked.connect(self.delete_row)

        self.save_button = QPushButton("Сохранить в JSON")
        self.save_button.clicked.connect(self.save_to_json)

        self.load_button = QPushButton("Загрузить из JSON")
        self.load_button.clicked.connect(self.load_from_json)

        # Добавляем виджеты в layout
        layout.addWidget(self.table)
        layout.addWidget(self.add_button)
        layout.addWidget(self.delete_button)
        layout.addWidget(self.save_button)
        layout.addWidget(self.load_button)

        # Инициализируем данные
        self.data = []

    def add_row(self):
        """Добавляет новую строку в таблицу"""
        row_position = self.table.rowCount()
        self.table.insertRow(row_position)

        # Устанавливаем значения по умолчанию
        self.table.setItem(row_position, 0, QTableWidgetItem("Новое имя"))
        self.table.setItem(row_position, 1, QTableWidgetItem("0"))
        self.table.setItem(row_position, 2, QTableWidgetItem("example@mail.com"))

    def delete_row(self):
        """Удаляет выбранную строку из таблицы"""
        current_row = self.table.currentRow()
        if current_row >= 0:
            self.table.removeRow(current_row)
        else:
            QMessageBox.warning(self, "Предупреждение", "Пожалуйста, выберите строку для удаления")

    def save_to_json(self):
        """Сохраняет данные таблицы в JSON-файл"""
        # Собираем данные из таблицы
        data = []
        for row in range(self.table.rowCount()):
            row_data = {
                "name": self.table.item(row, 0).text(),
                "age": self.table.item(row, 1).text(),
                "email": self.table.item(row, 2).text()
            }
            data.append(row_data)

        # Открываем диалог сохранения файла
        file_name, _ = QFileDialog.getSaveFileName(
            self, "Сохранить файл", "", "JSON Files (*.json)")

        if file_name:
            try:
                with open(file_name, 'w', encoding='utf-8') as f:
                    json.dump(data, f, ensure_ascii=False, indent=4)
                QMessageBox.information(self, "Успех", "Данные успешно сохранены")
            except Exception as e:
                QMessageBox.critical(self, "Ошибка", f"Не удалось сохранить файл: {str(e)}")

    def load_from_json(self):
        """Загружает данные из JSON-файла в таблицу"""
        # Открываем диалог выбора файла
        file_name, _ = QFileDialog.getOpenFileName(
            self, "Открыть файл", "", "JSON Files (*.json)")

        if file_name:
            try:
                with open(file_name, 'r', encoding='utf-8') as f:
                    data = json.load(f)

                # Очищаем таблицу перед загрузкой новых данных
                self.table.setRowCount(0)

                # Заполняем таблицу данными из JSON
                for row_data in data:
                    row_position = self.table.rowCount()
                    self.table.insertRow(row_position)

                    self.table.setItem(row_position, 0, QTableWidgetItem(row_data.get("name", "")))
                    self.table.setItem(row_position, 1, QTableWidgetItem(str(row_data.get("age", ""))))
                    self.table.setItem(row_position, 2, QTableWidgetItem(row_data.get("email", "")))

                QMessageBox.information(self, "Успех", "Данные успешно загружены")
            except Exception as e:
                QMessageBox.critical(self, "Ошибка", f"Не удалось загрузить файл: {str(e)}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TableWidgetDemo()
    window.show()
    sys.exit(app.exec_())