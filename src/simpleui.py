import QtWidgets as QtWidgets


class SimpleUI(QtWidgets.QDialog):

    def __init__(self):
        """super is parent for simpleui which is qdialog"""
        super(SimpleUI, self).__init__()
        self.setWindowTitle("A Simple Ui")
