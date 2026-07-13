import sys
import jdatetime
from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMenu
from PyQt5.QtGui import QIcon, QPixmap, QPainter, QFont
from PyQt5.QtCore import QTimer

def create_icon(day):
    pixmap = QPixmap(64, 64)
    pixmap.fill()

    painter = QPainter(pixmap)
    painter.setFont(QFont("Sans", 30))
    painter.drawText(pixmap.rect(), 0x84, str(day))
    painter.end()

    return QIcon(pixmap)

def update_tray():
    global current_day
    today = jdatetime.date.today()

    if today.day != current_day:
        current_day = today.day
        tray.setIcon(create_icon(current_day))

        full_date = f"{today.day} {today.strftime('%B')} {today.year}"
        menu.clear()
        menu.addAction(full_date)
        menu.addSeparator()
        menu.addAction("Exit", app.quit)

app = QApplication(sys.argv)

today = jdatetime.date.today()
current_day = today.day

tray = QSystemTrayIcon()
tray.setIcon(create_icon(current_day))

menu = QMenu()
menu.addAction(f"{today.day} {today.strftime('%B')} {today.year}")
menu.addSeparator()
menu.addAction("Exit", app.quit)

tray.setContextMenu(menu)
tray.show()

# هر 60 ثانیه چک کن
timer = QTimer()
timer.timeout.connect(update_tray)
timer.start(60000)

sys.exit(app.exec_())
