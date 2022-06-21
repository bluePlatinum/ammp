from ammp.ui.systemViewer import SystemViewer

import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget


class TestSystemViewer:
    """
    Tests for the SystemViewer class
    """
    def test_constructor(self):
        """
        Test the constructor method
        """
        app = QApplication(sys.argv)
        parent = QWidget()
        systemViewer = SystemViewer(parent=parent)

        assert systemViewer.parent() == parent

        app.exit()
