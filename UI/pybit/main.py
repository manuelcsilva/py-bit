import PySide6.QtCore
import PySide6.QtGui
import PySide6.QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(499, 378)
        self.centralwidget = PySide6.QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.checkBox = PySide6.QCheckBox(self.centralwidget)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(PySide6.QRect(40, 130, 76, 20))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = PySide6.QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(PySide6.QRect(0, 0, 499, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = PySide6.QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        PySide6.QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(PySide6.QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.checkBox.setText(PySide6.QCoreApplication.translate("MainWindow", u"CheckBox", None))
    # retranslateUi
