from PyQt5 import uic
from PyQt5.QtWidgets import QWidget


class Reports(QWidget):
    # Class name is important as its imported
    # to __main__ as it is

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi('ui/reports.ui', self)
