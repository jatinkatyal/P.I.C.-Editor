# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
            return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setFunc(self):
        self.actionOpen.triggered.connect(self.fileOpen)
        self.actionSave.triggered.connect(self.fileSave)
        self.actionExit.triggered.connect(self.closeApp)
        self.buttonBox.clicked.connect(self.filterFunc)
        self.buttonBox.accepted.connect(self.acceptChanges)
        self.buttonBox_2.clicked.connect(self.transformFunc)
        self.buttonBox_2.accepted.connect(self.acceptChanges)
    def fileOpen(self):
        file = QtGui.QFileDialog.getOpenFileName(None,"Open file")
        import Image as i
        self.pic = i.Image(file)
        from scipy.misc import imsave
        imsave("Resources/test.jpg",self.pic.get_img())
        self.imageUpdate()
    def imageUpdate(self,img='Resources/test.jpg'):
        self.scene = QtGui.QGraphicsScene()
        self.scene.addPixmap(QtGui.QPixmap(img)) 
        self.graphicsView.setScene(self.scene)
        self.graphicsView.show()
    def fileSave(self):
        file = QtGui.QFileDialog.getSaveFileName(None,"Save File")
        from scipy.misc import imsave
        imsave(file,self.pic.get_img())
    def filterFunc(self):
        import Image as i, Filter
        self.pic = i.Image("Resources/test.jpg")
        if(self.radioButton_0.isChecked()):
            self.pic = i.Image("Resources/test.jpg")
        if(self.radioButton_1.isChecked()):
            self.pic.set_img(Filter.mars(self.pic.get_img()))
        if(self.radioButton_2.isChecked()):
            self.pic.set_img(Filter.night_vision(self.pic.get_img()))
        if(self.radioButton_3.isChecked()):
            self.pic.set_img(Filter.night(self.pic.get_img()))
        if(self.radioButton_4.isChecked()):
            self.pic.set_img(Filter.aquamarine(self.pic.get_img()))
        if(self.radioButton_5.isChecked()):
            self.pic.set_img(Filter.magenta(self.pic.get_img()))
        if(self.radioButton_6.isChecked()):
            self.pic.set_img(Filter.pale(self.pic.get_img()))
        if(self.radioButton_7.isChecked()):
            self.pic.set_img(Filter.wnb(self.pic.get_img()))
        if(self.radioButton_8.isChecked()):
            self.pic.set_img(Filter.bnw(self.pic.get_img()))
        from scipy.misc import imsave
        imsave("Resources/test2.jpg",self.pic.get_img())
        self.imageUpdate("Resources/test2.jpg")
    def transformFunc(self):
        import Image as i, Transform
        self.pic = i.Image("Resources/test.jpg")
        if(self.radioButton.isChecked()):
            self.pic.set_img(Transform.crop(self.pic.get_img(),self.spinBox_2.value(),self.spinBox_3.value()))
        if(self.radioButton_9.isChecked()):
            self.pic.set_img(Transform.rotate(self.pic.get_img(),self.spinBox.value()))
        if(self.radioButton_10.isChecked()):
            if(self.checkBox.isChecked()):
                self.pic.set_img(Transform.flip(self.pic.get_img(),1))
            if(self.checkBox_2.isChecked()):
                self.pic.set_img(Transform.flip(self.pic.get_img(),2))
        from scipy.misc import imsave
        imsave("Resources/test2.jpg",self.pic.get_img())
        self.imageUpdate("Resources/test2.jpg")
    def acceptChanges(self):
        from scipy.misc import imsave
        imsave("Resources/test.jpg",self.pic.get_img())
    def closeApp(self):
        import sys
        ch = QtGui.QMessageBox.question(None,'Exit>',
                                    "Exit PIC Editor?",
                                    QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.No)
        if(ch== QtGui.QMessageBox.Yes):
            import sys
            sys.exit()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(684, 373)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.graphicsView = QtGui.QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.gridLayout_2.addWidget(self.graphicsView, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 684, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuFilters = QtGui.QMenu(self.menubar)
        self.menuFilters.setObjectName(_fromUtf8("menuFilters"))
        self.menuBlack_and_White = QtGui.QMenu(self.menuFilters)
        self.menuBlack_and_White.setObjectName(_fromUtf8("menuBlack_and_White"))
        self.menuTransforms = QtGui.QMenu(self.menubar)
        self.menuTransforms.setObjectName(_fromUtf8("menuTransforms"))
        self.menuFlip = QtGui.QMenu(self.menuTransforms)
        self.menuFlip.setObjectName(_fromUtf8("menuFlip"))
        self.menuView = QtGui.QMenu(self.menubar)
        self.menuView.setObjectName(_fromUtf8("menuView"))
        self.menuTool = QtGui.QMenu(self.menuView)
        self.menuTool.setObjectName(_fromUtf8("menuTool"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.filter = QtGui.QDockWidget(MainWindow)
        self.filter.setObjectName(_fromUtf8("filter"))
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label = QtGui.QLabel(self.dockWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_3.addWidget(self.label)
        self.radioButton_0 = QtGui.QRadioButton(self.dockWidgetContents)
        self.radioButton_0.setObjectName(_fromUtf8("radioButton_0"))
        self.verticalLayout_3.addWidget(self.radioButton_0)
        self.radioButton_1 = QtGui.QRadioButton(self.dockWidgetContents)
        self.radioButton_1.setObjectName(_fromUtf8("radioButton_1"))
        self.verticalLayout_3.addWidget(self.radioButton_1)
        self.radioButton_2 = QtGui.QRadioButton(self.dockWidgetContents)
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.verticalLayout_3.addWidget(self.radioButton_2)
        self.radioButton_3 = QtGui.QRadioButton(self.dockWidgetContents)
        self.radioButton_3.setObjectName(_fromUtf8("radioButton_3"))
        self.verticalLayout_3.addWidget(self.radioButton_3)
        self.radioButton_4 = QtGui.QRadioButton(self.dockWidgetContents)
        self.radioButton_4.setObjectName(_fromUtf8("radioButton_4"))
        self.verticalLayout_3.addWidget(self.radioButton_4)
        self.radioButton_5 = QtGui.QRadioButton(self.dockWidgetContents)
        self.radioButton_5.setObjectName(_fromUtf8("radioButton_5"))
        self.verticalLayout_3.addWidget(self.radioButton_5)
        self.radioButton_6 = QtGui.QRadioButton(self.dockWidgetContents)
        self.radioButton_6.setObjectName(_fromUtf8("radioButton_6"))
        self.verticalLayout_3.addWidget(self.radioButton_6)
        self.radioButton_7 = QtGui.QRadioButton(self.dockWidgetContents)
        self.radioButton_7.setObjectName(_fromUtf8("radioButton_7"))
        self.verticalLayout_3.addWidget(self.radioButton_7)
        self.radioButton_8 = QtGui.QRadioButton(self.dockWidgetContents)
        self.radioButton_8.setObjectName(_fromUtf8("radioButton_8"))
        self.verticalLayout_3.addWidget(self.radioButton_8)
        self.buttonBox = QtGui.QDialogButtonBox(self.dockWidgetContents)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Apply|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout_3.addWidget(self.buttonBox)
        self.filter.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.filter)
        self.transform = QtGui.QDockWidget(MainWindow)
        self.transform.setObjectName(_fromUtf8("transform"))
        self.dockWidgetContents_2 = QtGui.QWidget()
        self.dockWidgetContents_2.setObjectName(_fromUtf8("dockWidgetContents_2"))
        self.gridLayout = QtGui.QGridLayout(self.dockWidgetContents_2)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.radioButton_9 = QtGui.QRadioButton(self.dockWidgetContents_2)
        self.radioButton_9.setObjectName(_fromUtf8("radioButton_9"))
        self.gridLayout.addWidget(self.radioButton_9, 7, 0, 1, 2)
        self.label_3 = QtGui.QLabel(self.dockWidgetContents_2)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 1, 1, 1)
        self.spinBox = QtGui.QSpinBox(self.dockWidgetContents_2)
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.gridLayout.addWidget(self.spinBox, 7, 2, 1, 2)
        self.radioButton = QtGui.QRadioButton(self.dockWidgetContents_2)
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.gridLayout.addWidget(self.radioButton, 1, 0, 1, 1)
        self.radioButton_10 = QtGui.QRadioButton(self.dockWidgetContents_2)
        self.radioButton_10.setObjectName(_fromUtf8("radioButton_10"))
        self.gridLayout.addWidget(self.radioButton_10, 4, 0, 2, 1)
        self.checkBox = QtGui.QCheckBox(self.dockWidgetContents_2)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.gridLayout.addWidget(self.checkBox, 5, 1, 1, 3)
        self.label_2 = QtGui.QLabel(self.dockWidgetContents_2)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 3)
        self.spinBox_2 = QtGui.QSpinBox(self.dockWidgetContents_2)
        self.spinBox_2.setObjectName(_fromUtf8("spinBox_2"))
        self.gridLayout.addWidget(self.spinBox_2, 1, 2, 1, 2)
        self.checkBox_2 = QtGui.QCheckBox(self.dockWidgetContents_2)
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.gridLayout.addWidget(self.checkBox_2, 4, 1, 1, 3)
        self.label_4 = QtGui.QLabel(self.dockWidgetContents_2)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 1, 1, 1, 1)
        self.buttonBox_2 = QtGui.QDialogButtonBox(self.dockWidgetContents_2)
        self.buttonBox_2.setStandardButtons(QtGui.QDialogButtonBox.Apply|QtGui.QDialogButtonBox.Ok)
        self.buttonBox_2.setObjectName(_fromUtf8("buttonBox_2"))
        self.gridLayout.addWidget(self.buttonBox_2, 8, 0, 1, 4)
        self.spinBox_3 = QtGui.QSpinBox(self.dockWidgetContents_2)
        self.spinBox_3.setObjectName(_fromUtf8("spinBox_3"))
        self.gridLayout.addWidget(self.spinBox_3, 2, 2, 1, 2)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 3, 0, 1, 4)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 6, 0, 1, 4)
        self.transform.setWidget(self.dockWidgetContents_2)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.transform)
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionMars = QtGui.QAction(MainWindow)
        self.actionMars.setObjectName(_fromUtf8("actionMars"))
        self.actionNight_Vision = QtGui.QAction(MainWindow)
        self.actionNight_Vision.setObjectName(_fromUtf8("actionNight_Vision"))
        self.actionNoght = QtGui.QAction(MainWindow)
        self.actionNoght.setObjectName(_fromUtf8("actionNoght"))
        self.actionAquamarine = QtGui.QAction(MainWindow)
        self.actionAquamarine.setObjectName(_fromUtf8("actionAquamarine"))
        self.actionMgenta = QtGui.QAction(MainWindow)
        self.actionMgenta.setObjectName(_fromUtf8("actionMgenta"))
        self.actionPale = QtGui.QAction(MainWindow)
        self.actionPale.setObjectName(_fromUtf8("actionPale"))
        self.actionBlack_and_White_2 = QtGui.QAction(MainWindow)
        self.actionBlack_and_White_2.setObjectName(_fromUtf8("actionBlack_and_White_2"))
        self.actionDarker = QtGui.QAction(MainWindow)
        self.actionDarker.setObjectName(_fromUtf8("actionDarker"))
        self.actionNormal = QtGui.QAction(MainWindow)
        self.actionNormal.setObjectName(_fromUtf8("actionNormal"))
        self.actionCrop = QtGui.QAction(MainWindow)
        self.actionCrop.setObjectName(_fromUtf8("actionCrop"))
        self.actionUpside_down = QtGui.QAction(MainWindow)
        self.actionUpside_down.setObjectName(_fromUtf8("actionUpside_down"))
        self.actionHorizontal = QtGui.QAction(MainWindow)
        self.actionHorizontal.setObjectName(_fromUtf8("actionHorizontal"))
        self.actionRotate = QtGui.QAction(MainWindow)
        self.actionRotate.setObjectName(_fromUtf8("actionRotate"))
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionFilters = QtGui.QAction(MainWindow)
        self.actionFilters.setObjectName(_fromUtf8("actionFilters"))
        self.actionTransforms = QtGui.QAction(MainWindow)
        self.actionTransforms.setObjectName(_fromUtf8("actionTransforms"))
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuBlack_and_White.addAction(self.actionDarker)
        self.menuBlack_and_White.addAction(self.actionNormal)
        self.menuFilters.addAction(self.actionMars)
        self.menuFilters.addAction(self.actionNight_Vision)
        self.menuFilters.addAction(self.actionNoght)
        self.menuFilters.addAction(self.actionAquamarine)
        self.menuFilters.addAction(self.actionMgenta)
        self.menuFilters.addAction(self.actionPale)
        self.menuFilters.addAction(self.menuBlack_and_White.menuAction())
        self.menuFlip.addAction(self.actionUpside_down)
        self.menuFlip.addAction(self.actionHorizontal)
        self.menuTransforms.addAction(self.actionCrop)
        self.menuTransforms.addAction(self.menuFlip.menuAction())
        self.menuTransforms.addAction(self.actionRotate)
        self.menuTool.addAction(self.actionFilters)
        self.menuTool.addAction(self.actionTransforms)
        self.menuView.addAction(self.menuTool.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuFilters.menuAction())
        self.menubar.addAction(self.menuTransforms.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.setFunc()
        self.fileOpen()
        
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "P.I.C.E.", None))
        MainWindow.setWindowIcon(QtGui.QIcon("Icon.jpg"))
        self.filter.setWindowTitle("Filters")
        self.filter.setWindowIcon(QtGui.QIcon("Icon.jpg"))
        self.transform.setWindowTitle("Transformss")
        self.transform.setWindowIcon(QtGui.QIcon("Resources/Icon.jpg"))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuFilters.setTitle(_translate("MainWindow", "Filters", None))
        self.menuBlack_and_White.setTitle(_translate("MainWindow", "Black and White", None))
        self.menuTransforms.setTitle(_translate("MainWindow", "Transforms", None))
        self.menuFlip.setTitle(_translate("MainWindow", "Flip", None))
        self.menuView.setTitle(_translate("MainWindow", "View", None))
        self.menuTool.setTitle(_translate("MainWindow", "Tool", None))
        self.label.setText(_translate("MainWindow", "Filters", None))
        self.radioButton_0.setText(_translate("MainWindow", "Original Image", None))
        self.radioButton_1.setText(_translate("MainWindow", " Mars Mode", None))
        self.radioButton_2.setText(_translate("MainWindow", "Night Vision", None))
        self.radioButton_3.setText(_translate("MainWindow", "Night mode", None))
        self.radioButton_4.setText(_translate("MainWindow", "Aquamarine Mode", None))
        self.radioButton_5.setText(_translate("MainWindow", "Magenta mode", None))
        self.radioButton_6.setText(_translate("MainWindow", "Pale mode", None))
        self.radioButton_7.setText(_translate("MainWindow", "Black and white", None))
        self.radioButton_8.setText(_translate("MainWindow", "Black and White(dark)", None))
        self.radioButton_9.setText(_translate("MainWindow", "Rotate", None))
        self.label_3.setText(_translate("MainWindow", "Y:", None))
        self.radioButton.setText(_translate("MainWindow", "Crop", None))
        self.radioButton_10.setText(_translate("MainWindow", "Flip", None))
        self.checkBox.setText(_translate("MainWindow", "Upside down", None))
        self.label_2.setText(_translate("MainWindow", "Transforms", None))
        self.checkBox_2.setText(_translate("MainWindow", "leftside right", None))
        self.label_4.setText(_translate("MainWindow", "X:", None))
        self.actionOpen.setText(_translate("MainWindow", "Open", None))
        self.actionSave.setText(_translate("MainWindow", "Save", None))
        self.actionMars.setText(_translate("MainWindow", "Mars", None))
        self.actionNight_Vision.setText(_translate("MainWindow", "Night Vision", None))
        self.actionNoght.setText(_translate("MainWindow", "Night", None))
        self.actionAquamarine.setText(_translate("MainWindow", "Aquamarine", None))
        self.actionMgenta.setText(_translate("MainWindow", "Magenta", None))
        self.actionPale.setText(_translate("MainWindow", "Pale", None))
        self.actionBlack_and_White_2.setText(_translate("MainWindow", "Black and White", None))
        self.actionDarker.setText(_translate("MainWindow", "Darker", None))
        self.actionNormal.setText(_translate("MainWindow", "Normal", None))
        self.actionCrop.setText(_translate("MainWindow", "Crop", None))
        self.actionUpside_down.setText(_translate("MainWindow", "Vertical", None))
        self.actionHorizontal.setText(_translate("MainWindow", "Horizontal", None))
        self.actionRotate.setText(_translate("MainWindow", "Rotate", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.actionFilters.setText(_translate("MainWindow", "Filters", None))
        self.actionTransforms.setText(_translate("MainWindow", "Transforms", None))
        self.spinBox.setMaximum (360)
        self.spinBox.setMinimum(0)
        self.spinBox_2.setMaximum (1000)
        self.spinBox_2.setMinimum(1)
        self.spinBox_3.setMaximum (1000)
        self.spinBox_3.setMinimum(1)

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

