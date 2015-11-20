from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QAction
from PyQt5.QtGui import QIcon
import sys, os

current_path = os.path.abspath(os.path.dirname(sys.argv[0])) + "/"

class tray_icon(QSystemTrayIcon):
    enabled_icon = "caffeine-cup-full.svg"
    disabled_icon = "caffeine-cup-empty.svg"
    script_name = "script.sh"
    is_enabled = False

    def __init__(self, parent=None):
        QSystemTrayIcon.__init__(self, parent=None)

        # Initial state
        self.set_disabled()

        # Right Click
        right_menu = RightClicked()
        self.setContextMenu(right_menu)

        # left click
        self.activated.connect(self.toggle)

    def set_enabled(self):
        icon = QIcon(current_path + self.enabled_icon)
        self.setIcon(icon)

    def set_disabled(self):
        icon = QIcon(current_path + self.disabled_icon)
        self.setIcon(icon)

    def toggle(self, reason):
        # if left clicked
        if(reason == QSystemTrayIcon.Trigger):
            if(self.is_enabled):
                self.set_disabled()
                self.is_enabled = False
                os.system(current_path + self.script_name + " " + "disable")

            else:
                self.set_enabled()
                self.is_enabled = True
                os.system(current_path + self.script_name + " " + "enable")

class RightClicked(QMenu):
    def __init__(self, parent=None):
        QMenu.__init__(self, parent=None)

        action = QAction("Exit", self)
        action.triggered.connect(lambda : QApplication.exit(0))
        self.addAction(action)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    tray = tray_icon(app)
    tray.show()

    sys.exit(app.exec_())
