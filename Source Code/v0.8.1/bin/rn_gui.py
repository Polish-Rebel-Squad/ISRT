# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\source_files\rn_gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_rn_window(object):
    def setupUi(self, rn_window):
        rn_window.setObjectName("rn_window")
        rn_window.resize(640, 720)
        rn_window.setMinimumSize(QtCore.QSize(640, 720))
        rn_window.setMaximumSize(QtCore.QSize(640, 723))
        font = QtGui.QFont()
        font.setPointSize(10)
        rn_window.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/img/isrt.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        rn_window.setWindowIcon(icon)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(rn_window)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.rn_top_layer = QtWidgets.QLabel(rn_window)
        self.rn_top_layer.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.rn_top_layer.setObjectName("rn_top_layer")
        self.verticalLayout.addWidget(self.rn_top_layer)
        spacerItem1 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.rn_middle_layer = QtWidgets.QLabel(rn_window)
        self.rn_middle_layer.setMinimumSize(QtCore.QSize(566, 580))
        self.rn_middle_layer.setMaximumSize(QtCore.QSize(566, 580))
        self.rn_middle_layer.setFrameShape(QtWidgets.QFrame.Box)
        self.rn_middle_layer.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.rn_middle_layer.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.rn_middle_layer.setWordWrap(True)
        self.rn_middle_layer.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.rn_middle_layer.setObjectName("rn_middle_layer")
        self.horizontalLayout_2.addWidget(self.rn_middle_layer)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.chkbx_show_rn = QtWidgets.QCheckBox(rn_window)
        self.chkbx_show_rn.setMaximumSize(QtCore.QSize(180, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.chkbx_show_rn.setFont(font)
        self.chkbx_show_rn.setObjectName("chkbx_show_rn")
        self.horizontalLayout.addWidget(self.chkbx_show_rn)
        self.btn_rn_close = QtWidgets.QPushButton(rn_window)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_rn_close.sizePolicy().hasHeightForWidth())
        self.btn_rn_close.setSizePolicy(sizePolicy)
        self.btn_rn_close.setMinimumSize(QtCore.QSize(150, 0))
        self.btn_rn_close.setMaximumSize(QtCore.QSize(150, 16777215))
        self.btn_rn_close.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_rn_close.setStyleSheet("background-color:rgb(228, 228, 228)\n"
"")
        self.btn_rn_close.setObjectName("btn_rn_close")
        self.horizontalLayout.addWidget(self.btn_rn_close)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(rn_window)
        QtCore.QMetaObject.connectSlotsByName(rn_window)

    def retranslateUi(self, rn_window):
        _translate = QtCore.QCoreApplication.translate
        rn_window.setWindowTitle(_translate("rn_window", "Release Notes ISRT"))
        self.rn_top_layer.setText(_translate("rn_window", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">ISRT {version} Release Notes</span></p></body></html>"))
        self.rn_middle_layer.setText(_translate("rn_window", "<html><head/><body><p>For this version I had to do a lot of work behind the scenes adding the map manager and all new maps from the mapping contest - that was a load. I hope you enjoy this release! I would love to hear from you via my Discord (=TCT= Madman#2803), my Steam Account (=TCT= Madman) or via e-mail (madman@isrt.info).</p><p align=\"center\">Report bugs or errors here: <a href=\"https://www.isrt.info/?page_id=661\"><span style=\" text-decoration: underline; color:#0000ff;\">Support Ticket System</span></a></p><p align=\"center\"><br/></p><p><span style=\" font-size:11pt; font-weight:600;\">What\'s new?</span></p><p>- Implemented a <span style=\" font-weight:600;\">map manager</span> so users can add and modify maps and scenarios<br/>- Added <span style=\" font-weight:600;\">65 new maps</span>, especially from the mapping contest<br/>- Changed the <span style=\" font-weight:600;\">ISRT Server monitor to auto-refresh</span> all 30 seconds<br/>- No GUI freeze anymore due to proper threading<br/>- Redesigned the help center<br/>- Added <span style=\" font-weight:600;\">Frenzy mode</span> switch to map changer<br/>- Commands within Command historiy can now be copied with a double click<br/>- Cleaned up the code and fixed a couple of bugs - as always ;-)<br/></p><p><br/></p><p><span style=\" font-size:11pt; font-weight:600;\">Known bug </span><span style=\" font-size:11pt;\">(red = not possible to fix - NWI Server Bug):</span></p><p><span style=\" color:#aa0000;\">- When chosing random map change, the map is not updated correctly (NWI Server Bug reported; I unfortunately can\'t change false reporting on server side...)</span><br/></p><p align=\"center\"><span style=\" font-family:\'Consolas\',\'Courier New\',\'monospace\'; font-size:8pt; font-weight:600; color:#00557f;\">Thanks to Helsing, Stuermer and Mamba for the pre-release testing!</span></p><p align=\"center\"><span style=\" font-family:\'Consolas\',\'Courier New\',\'monospace\'; font-size:8pt; font-weight:600; color:#00557f;\">I appreciate that very much!</span><br/></p><p><br/></p></body></html>"))
        self.chkbx_show_rn.setText(_translate("rn_window", "Do not show this window again"))
        self.btn_rn_close.setToolTip(_translate("rn_window", "Close Release Notes"))
        self.btn_rn_close.setStatusTip(_translate("rn_window", "Close Release Notes"))
        self.btn_rn_close.setText(_translate("rn_window", "Close"))
import res_rc
