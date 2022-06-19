from ammp.ui.systemViewer import SystemViewer
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout


class GreetDialog(QDialog):
    """
    This is the dialog that appears when starting the application (for now).
    In that sense this is the entrypoint to the application and displays
    buttons to use different types of the Applications functionality.

    :param parent: The parent widget. This will be passed onto the QDialog
        constructor as the parent.
    """
    def __init__(self, parent=None):
        """
        Constructor method
        """
        super().__init__(parent)

        self.setWindowTitle('ammp')
        self.setFixedSize(235, 235)
        self.setContentsMargins(20, 50, 20, 50)
        layout = QVBoxLayout()

        # First button (currently just named 1, will change with function)
        systemViewerButton = QPushButton('System Viewer')
        layout.addWidget(systemViewerButton)
        systemViewerButton.clicked.connect(self.openSystemViewer)

        # Second button (currently just named 2, will change with function)
        btn_2 = QPushButton('Test 2')
        layout.addWidget(btn_2)

        # Exit button
        exitBtn = QPushButton('Exit')
        layout.addWidget(exitBtn)
        exitBtn.clicked.connect(self.close)

        self.setLayout(layout)

    def openSystemViewer(self):
        """
        Opens the System viewer Widget, and closes the greeting dialog.

        :return: None
        """
        self.hide()
        systemViewer = SystemViewer()
        self.parent().focusWidget = systemViewer
        systemViewer.show()
