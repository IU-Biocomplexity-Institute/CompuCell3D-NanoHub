# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'configurationdlg.ui'
#
# Created: Mon Dec  9 21:26:54 2013
#      by: PyQt4 UI code generator 4.10.3
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

class Ui_ConfigurationDlg(object):
    def setupUi(self, ConfigurationDlg):
        ConfigurationDlg.setObjectName(_fromUtf8("ConfigurationDlg"))
        ConfigurationDlg.resize(530, 446)
        self.verticalLayout_3 = QtGui.QVBoxLayout(ConfigurationDlg)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.tabWidget = QtGui.QTabWidget(ConfigurationDlg)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.editingTab = QtGui.QWidget()
        self.editingTab.setObjectName(_fromUtf8("editingTab"))
        self.gridLayout_2 = QtGui.QGridLayout(self.editingTab)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tabSpacesCheckBox = QtGui.QCheckBox(self.editingTab)
        self.tabSpacesCheckBox.setChecked(True)
        self.tabSpacesCheckBox.setObjectName(_fromUtf8("tabSpacesCheckBox"))
        self.gridLayout.addWidget(self.tabSpacesCheckBox, 0, 0, 1, 3)
        self.tabWidthLabel = QtGui.QLabel(self.editingTab)
        self.tabWidthLabel.setObjectName(_fromUtf8("tabWidthLabel"))
        self.gridLayout.addWidget(self.tabWidthLabel, 1, 0, 1, 1)
        self.spacesSpinBox = QtGui.QSpinBox(self.editingTab)
        self.spacesSpinBox.setEnabled(True)
        self.spacesSpinBox.setMinimum(1)
        self.spacesSpinBox.setProperty("value", 4)
        self.spacesSpinBox.setObjectName(_fromUtf8("spacesSpinBox"))
        self.gridLayout.addWidget(self.spacesSpinBox, 1, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 2, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.lineNumberCheckBox = QtGui.QCheckBox(self.editingTab)
        self.lineNumberCheckBox.setChecked(True)
        self.lineNumberCheckBox.setObjectName(_fromUtf8("lineNumberCheckBox"))
        self.verticalLayout.addWidget(self.lineNumberCheckBox)
        self.foldTextCheckBox = QtGui.QCheckBox(self.editingTab)
        self.foldTextCheckBox.setChecked(True)
        self.foldTextCheckBox.setObjectName(_fromUtf8("foldTextCheckBox"))
        self.verticalLayout.addWidget(self.foldTextCheckBox)
        self.tabGuidelinesCheckBox = QtGui.QCheckBox(self.editingTab)
        self.tabGuidelinesCheckBox.setChecked(True)
        self.tabGuidelinesCheckBox.setObjectName(_fromUtf8("tabGuidelinesCheckBox"))
        self.verticalLayout.addWidget(self.tabGuidelinesCheckBox)
        self.whiteSpaceCheckBox = QtGui.QCheckBox(self.editingTab)
        self.whiteSpaceCheckBox.setObjectName(_fromUtf8("whiteSpaceCheckBox"))
        self.verticalLayout.addWidget(self.whiteSpaceCheckBox)
        self.eolCheckBox = QtGui.QCheckBox(self.editingTab)
        self.eolCheckBox.setObjectName(_fromUtf8("eolCheckBox"))
        self.verticalLayout.addWidget(self.eolCheckBox)
        self.restoreTabsCheckBox = QtGui.QCheckBox(self.editingTab)
        self.restoreTabsCheckBox.setChecked(True)
        self.restoreTabsCheckBox.setObjectName(_fromUtf8("restoreTabsCheckBox"))
        self.verticalLayout.addWidget(self.restoreTabsCheckBox)
        self.wrapLinesCheckBox = QtGui.QCheckBox(self.editingTab)
        self.wrapLinesCheckBox.setObjectName(_fromUtf8("wrapLinesCheckBox"))
        self.verticalLayout.addWidget(self.wrapLinesCheckBox)
        self.showWrapSymbolCheckBox = QtGui.QCheckBox(self.editingTab)
        self.showWrapSymbolCheckBox.setObjectName(_fromUtf8("showWrapSymbolCheckBox"))
        self.verticalLayout.addWidget(self.showWrapSymbolCheckBox)
        self.autocompletionCheckBox = QtGui.QCheckBox(self.editingTab)
        self.autocompletionCheckBox.setChecked(True)
        self.autocompletionCheckBox.setObjectName(_fromUtf8("autocompletionCheckBox"))
        self.verticalLayout.addWidget(self.autocompletionCheckBox)
        self.quickTextDecodingCB = QtGui.QCheckBox(self.editingTab)
        self.quickTextDecodingCB.setChecked(True)
        self.quickTextDecodingCB.setObjectName(_fromUtf8("quickTextDecodingCB"))
        self.verticalLayout.addWidget(self.quickTextDecodingCB)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.autocompletionLabel = QtGui.QLabel(self.editingTab)
        self.autocompletionLabel.setObjectName(_fromUtf8("autocompletionLabel"))
        self.horizontalLayout_3.addWidget(self.autocompletionLabel)
        self.autocompletionSpinBox = QtGui.QSpinBox(self.editingTab)
        self.autocompletionSpinBox.setMinimum(1)
        self.autocompletionSpinBox.setProperty("value", 2)
        self.autocompletionSpinBox.setObjectName(_fromUtf8("autocompletionSpinBox"))
        self.horizontalLayout_3.addWidget(self.autocompletionSpinBox)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(204, 291, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 1, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(177, 10, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem2, 1, 0, 1, 1)
        self.tabWidget.addTab(self.editingTab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.verticalLayout_9 = QtGui.QVBoxLayout(self.tab_2)
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.verticalLayout_8 = QtGui.QVBoxLayout()
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.groupBox = QtGui.QGroupBox(self.tab_2)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.themeCB = QtGui.QComboBox(self.groupBox)
        self.themeCB.setObjectName(_fromUtf8("themeCB"))
        self.verticalLayout_5.addWidget(self.themeCB)
        self.verticalLayout_8.addWidget(self.groupBox)
        self.fontGroupBox = QtGui.QGroupBox(self.tab_2)
        self.fontGroupBox.setObjectName(_fromUtf8("fontGroupBox"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.fontGroupBox)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.fontLabel = QtGui.QLabel(self.fontGroupBox)
        self.fontLabel.setObjectName(_fromUtf8("fontLabel"))
        self.horizontalLayout_4.addWidget(self.fontLabel)
        self.fontComboBox = QtGui.QFontComboBox(self.fontGroupBox)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Courier New"))
        font.setPointSize(10)
        self.fontComboBox.setCurrentFont(font)
        self.fontComboBox.setObjectName(_fromUtf8("fontComboBox"))
        self.horizontalLayout_4.addWidget(self.fontComboBox)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.fontSizeLabel = QtGui.QLabel(self.fontGroupBox)
        self.fontSizeLabel.setObjectName(_fromUtf8("fontSizeLabel"))
        self.horizontalLayout_5.addWidget(self.fontSizeLabel)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.fontSizeComboBox = QtGui.QComboBox(self.fontGroupBox)
        self.fontSizeComboBox.setObjectName(_fromUtf8("fontSizeComboBox"))
        self.fontSizeComboBox.addItem(_fromUtf8(""))
        self.fontSizeComboBox.addItem(_fromUtf8(""))
        self.fontSizeComboBox.addItem(_fromUtf8(""))
        self.fontSizeComboBox.addItem(_fromUtf8(""))
        self.fontSizeComboBox.addItem(_fromUtf8(""))
        self.fontSizeComboBox.addItem(_fromUtf8(""))
        self.fontSizeComboBox.addItem(_fromUtf8(""))
        self.fontSizeComboBox.addItem(_fromUtf8(""))
        self.fontSizeComboBox.addItem(_fromUtf8(""))
        self.fontSizeComboBox.addItem(_fromUtf8(""))
        self.fontSizeComboBox.addItem(_fromUtf8(""))
        self.fontSizeComboBox.addItem(_fromUtf8(""))
        self.fontSizeComboBox.addItem(_fromUtf8(""))
        self.horizontalLayout_5.addWidget(self.fontSizeComboBox)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.verticalLayout_7.addLayout(self.verticalLayout_4)
        self.verticalLayout_8.addWidget(self.fontGroupBox)
        self.horizontalLayout_8.addLayout(self.verticalLayout_8)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem4)
        self.verticalLayout_9.addLayout(self.horizontalLayout_8)
        spacerItem5 = QtGui.QSpacerItem(17, 165, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem5)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.verticalLayout_10 = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.pluginsLW = QtGui.QListWidget(self.tab)
        self.pluginsLW.setObjectName(_fromUtf8("pluginsLW"))
        self.horizontalLayout_7.addWidget(self.pluginsLW)
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.pluginsTE = QtGui.QTextEdit(self.tab)
        self.pluginsTE.setReadOnly(True)
        self.pluginsTE.setObjectName(_fromUtf8("pluginsTE"))
        self.verticalLayout_6.addWidget(self.pluginsTE)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.loadPB = QtGui.QPushButton(self.tab)
        self.loadPB.setObjectName(_fromUtf8("loadPB"))
        self.horizontalLayout_6.addWidget(self.loadPB)
        self.unloadPB = QtGui.QPushButton(self.tab)
        self.unloadPB.setObjectName(_fromUtf8("unloadPB"))
        self.horizontalLayout_6.addWidget(self.unloadPB)
        self.loadOnStartupCHB = QtGui.QCheckBox(self.tab)
        self.loadOnStartupCHB.setObjectName(_fromUtf8("loadOnStartupCHB"))
        self.horizontalLayout_6.addWidget(self.loadOnStartupCHB)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem6)
        self.verticalLayout_6.addLayout(self.horizontalLayout_6)
        spacerItem7 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem7)
        self.horizontalLayout_7.addLayout(self.verticalLayout_6)
        self.verticalLayout_10.addLayout(self.horizontalLayout_7)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.verticalLayout_3.addWidget(self.tabWidget)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem8 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem8)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.okButton = QtGui.QPushButton(ConfigurationDlg)
        self.okButton.setObjectName(_fromUtf8("okButton"))
        self.horizontalLayout.addWidget(self.okButton)
        self.cancelButton = QtGui.QPushButton(ConfigurationDlg)
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.horizontalLayout.addWidget(self.cancelButton)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.retranslateUi(ConfigurationDlg)
        self.tabWidget.setCurrentIndex(0)
        self.fontSizeComboBox.setCurrentIndex(2)
        QtCore.QObject.connect(self.tabSpacesCheckBox, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.spacesSpinBox.setEnabled)
        QtCore.QObject.connect(self.cancelButton, QtCore.SIGNAL(_fromUtf8("clicked()")), ConfigurationDlg.reject)
        QtCore.QObject.connect(self.okButton, QtCore.SIGNAL(_fromUtf8("clicked()")), ConfigurationDlg.accept)
        QtCore.QObject.connect(self.wrapLinesCheckBox, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.showWrapSymbolCheckBox.setEnabled)
        QtCore.QObject.connect(self.autocompletionCheckBox, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.autocompletionSpinBox.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(ConfigurationDlg)

    def retranslateUi(self, ConfigurationDlg):
        ConfigurationDlg.setWindowTitle(_translate("ConfigurationDlg", "Configuration", None))
        self.tabSpacesCheckBox.setToolTip(_translate("ConfigurationDlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Set this option if you want to  use multiple spaces when Tab key is pressed instead of </span><span style=\" font-size:8pt; font-weight:600;\">&quot;\\t&quot;</span><span style=\" font-size:8pt;\"> character.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">This is highly recommended when editing Python scripts (unwritten standard is 4 spaces per tab)</span></p></body></html>", None))
        self.tabSpacesCheckBox.setText(_translate("ConfigurationDlg", "Use spaces instead of tabs", None))
        self.tabWidthLabel.setText(_translate("ConfigurationDlg", "Tab width", None))
        self.lineNumberCheckBox.setText(_translate("ConfigurationDlg", "Display Line Number", None))
        self.foldTextCheckBox.setText(_translate("ConfigurationDlg", "Enable Text Folding", None))
        self.tabGuidelinesCheckBox.setToolTip(_translate("ConfigurationDlg", "Display/hide vertical marks that help visualize indentation", None))
        self.tabGuidelinesCheckBox.setText(_translate("ConfigurationDlg", "Enable Tab Guidelines", None))
        self.whiteSpaceCheckBox.setToolTip(_translate("ConfigurationDlg", "Display/hide normally invisible white spaces", None))
        self.whiteSpaceCheckBox.setText(_translate("ConfigurationDlg", "Display whitespaces", None))
        self.eolCheckBox.setText(_translate("ConfigurationDlg", "Display End of Line", None))
        self.restoreTabsCheckBox.setText(_translate("ConfigurationDlg", "Restore tabs on startup", None))
        self.wrapLinesCheckBox.setText(_translate("ConfigurationDlg", "Wrap Lines", None))
        self.showWrapSymbolCheckBox.setText(_translate("ConfigurationDlg", "Show Wrap Symbol", None))
        self.autocompletionCheckBox.setText(_translate("ConfigurationDlg", "Enable Autocompletion", None))
        self.quickTextDecodingCB.setToolTip(_translate("ConfigurationDlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Enales text decoding to be based on first 1000 characters. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">It can be less acurate then full text scanning but documents open faster </span></p></body></html>", None))
        self.quickTextDecodingCB.setText(_translate("ConfigurationDlg", "Enable Quick Text Decoding", None))
        self.autocompletionLabel.setToolTip(_translate("ConfigurationDlg", "Determines minimum number of characters after which autocompletion options will be displayed", None))
        self.autocompletionLabel.setText(_translate("ConfigurationDlg", "Autocompletion threshold", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.editingTab), _translate("ConfigurationDlg", "Editing", None))
        self.groupBox.setTitle(_translate("ConfigurationDlg", "Editor Theme", None))
        self.fontGroupBox.setTitle(_translate("ConfigurationDlg", "Fonts", None))
        self.fontLabel.setText(_translate("ConfigurationDlg", "Font", None))
        self.fontSizeLabel.setText(_translate("ConfigurationDlg", "Size", None))
        self.fontSizeComboBox.setItemText(0, _translate("ConfigurationDlg", "8", None))
        self.fontSizeComboBox.setItemText(1, _translate("ConfigurationDlg", "9", None))
        self.fontSizeComboBox.setItemText(2, _translate("ConfigurationDlg", "10", None))
        self.fontSizeComboBox.setItemText(3, _translate("ConfigurationDlg", "11", None))
        self.fontSizeComboBox.setItemText(4, _translate("ConfigurationDlg", "12", None))
        self.fontSizeComboBox.setItemText(5, _translate("ConfigurationDlg", "14", None))
        self.fontSizeComboBox.setItemText(6, _translate("ConfigurationDlg", "16", None))
        self.fontSizeComboBox.setItemText(7, _translate("ConfigurationDlg", "18", None))
        self.fontSizeComboBox.setItemText(8, _translate("ConfigurationDlg", "20", None))
        self.fontSizeComboBox.setItemText(9, _translate("ConfigurationDlg", "22", None))
        self.fontSizeComboBox.setItemText(10, _translate("ConfigurationDlg", "24", None))
        self.fontSizeComboBox.setItemText(11, _translate("ConfigurationDlg", "26", None))
        self.fontSizeComboBox.setItemText(12, _translate("ConfigurationDlg", "28", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("ConfigurationDlg", "Style Config", None))
        self.loadPB.setText(_translate("ConfigurationDlg", "Load", None))
        self.unloadPB.setText(_translate("ConfigurationDlg", "Unload", None))
        self.loadOnStartupCHB.setText(_translate("ConfigurationDlg", "Load on startup", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("ConfigurationDlg", "Plugins", None))
        self.okButton.setText(_translate("ConfigurationDlg", "OK", None))
        self.cancelButton.setText(_translate("ConfigurationDlg", "Cancel", None))

