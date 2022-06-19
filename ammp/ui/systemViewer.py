from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QLabel


class SystemViewer(QMainWindow):
    """
    This class will allow to view a system of objects in space. This will
    mainly aide in development, but will also be used in final to view the
    system.

    :param parent: the parent widget
    """
    def __init__(self, parent=None):
        """
        Constructor method
        """
        super().__init__(parent)
        self.setWindowTitle('System Viewer')
        self.setCentralWidget(QLabel('PLACEHOLDER'))
        self._createMenu()

    def _createMenu(self):
        """
        Creates the menu for the SystemViewer QMainWindow
        :return: None
        """
        self.menu = self.menuBar().addMenu('&Menu')
        self.menu.addAction('&Exit', self.close)
