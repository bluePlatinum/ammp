from ammp.ui.mainWidget import MainWidget

import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget


class TestMainWidget:
    """
    Tests for the MainWidget Class
    """
    def test_constructor(self):
        """
        Tests the constructor of MainWidget
        """
        app = QApplication(sys.argv)
        parent = QWidget()
        focus = QWidget()
        widget = MainWidget(parent=parent)
        widget.currentFocus = focus

        assert widget.parent() == parent
        assert widget.currentFocus == focus

        app.exit()
