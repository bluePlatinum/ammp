import sys
from ammp.ui.greet_dialog import GreetDialog
from PyQt5.QtWidgets import QApplication


def main():
    app = QApplication(sys.argv)
    dialog = GreetDialog()
    dialog.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
