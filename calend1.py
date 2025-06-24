from PySide6.QtWidgets import QCalendarWidget
from PySide6.QtGui import QColor, QBrush, QPen, QFont
from PySide6.QtCore import QDate, Qt


class CustomCalendar(QCalendarWidget):
    def paintCell(self, painter, rect, date):
        is_current = date == QDate.currentDate()
        is_selected = date == self.selectedDate()

        painter.save()

        if is_current and is_selected:
            # Дата является и текущей, и выбранной
            painter.setBrush(QBrush(QColor(76, 175, 80)))  # зеленый
            painter.setPen(QPen(QColor(255, 255, 255)))  # белый
            font = QFont()
            font.setBold(True)
            painter.setFont(font)
        elif is_current:
            # Только текущая дата
            painter.setBrush(QBrush(QColor(230, 243, 255)))  # голубой
            painter.setPen(QPen(QColor(0, 102, 204)))  # синий
            font = QFont()
            font.setBold(True)
            painter.setFont(font)
        elif is_selected:
            # Только выбранная дата
            painter.setBrush(QBrush(QColor(255, 87, 34)))  # оранжевый
            painter.setPen(QPen(QColor(255, 255, 255)))  # белый
        else:
            # Обычная дата
            painter.setBrush(QBrush(QColor(255, 255, 255)))  # белый
            painter.setPen(QPen(QColor(0, 0, 0)))  # черный

        painter.drawRect(rect)
        painter.drawText(rect, Qt.AlignmentFlag.AlignCenter, str(date.day()))

        painter.restore()


# Использование
from PySide6.QtWidgets import QApplication

app = QApplication([])
calendar = CustomCalendar()
calendar.show()
app.exec()