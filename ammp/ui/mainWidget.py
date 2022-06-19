from PyQt5.QtWidgets import QWidget


class MainWidget(QWidget):
    """
    This class is used as the main widget. It is primarily used to switch
    between different widgets, which the user perceives to be the main
    (focused) widgets. For this the MainWidget class has the currentFocus
    property which holds the widget with the current focus.

    As an example this is used in main.py to act as a parent for all
    subsequent widgets. So at startup the greetDialog widget is created and
    set as the currentFocus for the main MainWidget. Then the dialog can create
    new windows and assign them to currentFocus while hiding itself.
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.currentFocus = None
