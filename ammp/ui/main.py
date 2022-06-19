import sys
from ammp.ui.mainWidget import MainWidget
from ammp.ui.greetDialog import GreetDialog
from PyQt5.QtWidgets import QApplication


def default():
    """
    The default entry point for the UI. This opens up a greeting Dialog with
    options on how to proceed.

    :return: None
    """
    app = QApplication(sys.argv)
    mainWidget = MainWidget()
    dialog = GreetDialog(parent=mainWidget)
    mainWidget.focusWidget = dialog
    dialog.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    default()
