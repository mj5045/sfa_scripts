import maya.OpenMayaUI as omui
from PySide2 import QtWidgets
from shiboken2 import wrapInstance


def maya_main_window():

    main_windows = omui.MQtUtil.mainWindow()
    return wrapInstance(long(main_windows), QtWidgets.QWidget)

class SimpleUI(QtWidgets.QDialog):

    def __init__(self):
        """super is parent for simpleui which is qdialog"""
        super(SimpleUI, self).__init__(parent=maya_main_window())
        self.setWindowTitle("A Simple Ui")
