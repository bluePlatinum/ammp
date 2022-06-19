import sys
from ammp.ui.mainWidget import MainWidget
from ammp.ui.greetDialog import GreetDialog
from PyQt5.QtWidgets import QApplication


def main():
    app = QApplication(sys.argv)
    mainWidget = MainWidget()
    dialog = GreetDialog(parent=mainWidget)
    mainWidget.focusWidget = dialog
    dialog.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
