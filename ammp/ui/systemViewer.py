from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from PyQt5.QtWidgets import QMainWindow


class SystemViewerGraphic(FigureCanvasQTAgg):
    """
    This widget contains the matplotlib plot which will represent the objects
    in the system.

    :param parent: the Parent of the Widget
    :type parent: QWidget
    :param width: the width of the matplotlib plot
    :type width: float
    :param height: the height of the matplotlib plot
    :type width: float
    :param dpi: dots per inch
    :type dpi: float
    """
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        """
        Constructor method
        """
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111, projection='3d')
        self.__parent = parent
        super(SystemViewerGraphic, self).__init__(fig)

    def parent(self):
        """
        Returns the parent.

        :return: the parent Qwidget
        :rtype: QWidget
        """
        return self.__parent


class SystemViewer(QMainWindow):
    """
    This class will allow to view a system of objects in space. This will
    mainly aide in development, but will also be used in final to view the
    system.

    :param parent: the parent widget
    :type parent: Qwidget
    :param system: the system to be displayed
    :type system: System
    """
    def __init__(self, parent=None, system=None):
        """
        Constructor method
        """
        super().__init__(parent)
        self.setWindowTitle('System Viewer')

        figure = SystemViewerGraphic(parent=self, width=5, height=4, dpi=100)

        try:
            system.draw_sv()
        except NotImplementedError:
            msg = ".draw_sv() method was not implemented."
            print(msg)
        except AttributeError:
            msg = ".draw_sv() method was not found in system. Something " \
                  "probably went wrong in assigning the system to the " \
                  "SystemViewer widget"
            print(msg)

        self.setCentralWidget(figure)
        self._createMenu()

    def _createMenu(self):
        """
        Creates the menu for the SystemViewer QMainWindow
        :return: None
        """
        self.menu = self.menuBar().addMenu('&Menu')
        self.menu.addAction('&Exit', self.close)
