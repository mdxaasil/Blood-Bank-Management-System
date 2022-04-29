
from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector as mc


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setMinimumSize(QtCore.QSize(1280, 720))

        

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(435, 25, 101, 71))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("logo.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(570, 0, 271, 81))
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(22)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(610, 40, 181, 81))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI Semilight")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(480, 290, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(15)
        
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(460, 240, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(530, 360, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(15)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        self.hname = QtWidgets.QLineEdit(self.centralwidget)
        self.hname.setGeometry(QtCore.QRect(630, 250, 191, 31))
        self.hname.setObjectName("hname")

        self.bg = QtWidgets.QLineEdit(self.centralwidget)
        self.bg.setGeometry(QtCore.QRect(630, 300, 191, 31))
        self.bg.setText("")
        self.bg.setObjectName("bg")

        self.volume = QtWidgets.QLineEdit(self.centralwidget)
        self.volume.setGeometry(QtCore.QRect(630, 360, 191, 31))
        self.volume.setObjectName("volume")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(670, 540, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.click)


        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(620, 490, 261, 51))
        self.checkBox.setObjectName("checkBox")

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(520, 410, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(15)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(530, 180, 381, 31))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(630, 420, 191, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("Yes")
        self.comboBox.addItem("No")
        self.comboBox.setCurrentIndex(1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def click(self):
        print("Clicked")
        hname1=self.hname.text()
        bg1 = self.bg.text()
        vol=self.volume.text()

        
        urg=self.comboBox.currentText()
        print(hname1,bg1,vol,urg)

        con=mc.connect(host="localhost",user="root",password="aasil",database="bloodbank")
        cur=con.cursor()
        cur.execute("insert into requests values('{}','{}',{},'{}')".format(hname1,bg1,int(vol),urg))
        con.commit()
        con.close()

        self.show_popup1()

        
        
        
    
    def show_popup1(self):
        msg=QtWidgets.QMessageBox()
        msg.setWindowTitle("Request")
        msg.setText("Request submitted successfully.")
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setWindowIcon(QtGui.QIcon('blood.png'))

        x=msg.exec_() 

    def show_popup2(self):
        msg=QtWidgets.QMessageBox()
        msg.setWindowTitle("Request")
        msg.setText("Request submitted successfully.")
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setWindowIcon(QtGui.QIcon('blood.png'))

        x=msg.exec_() 
        






    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "GD Blood Bank 🩸"))
        self.label_2.setText(_translate("MainWindow", "Request Portal"))
        self.label_3.setText(_translate("MainWindow", "Blood group:"))
        self.label_4.setText(_translate("MainWindow", "Hospital name:"))
        self.label_5.setText(_translate("MainWindow", "Volume:"))
        self.bg.setPlaceholderText(_translate("MainWindow", "A-/A+/B+/B-/O+/O-/AB+/AB-"))
        self.volume.setPlaceholderText(_translate("MainWindow", "in ml"))
        self.pushButton.setText(_translate("MainWindow", "Submit"))
        self.checkBox.setText(_translate("MainWindow", "I hereby confirm the details given above."))
        self.label_6.setText(_translate("MainWindow", "Urgency:"))
        self.label_7.setText(_translate("MainWindow", "Please enter the required details."))

        self.comboBox.setItemText(0, _translate("MainWindow", "Yes"))
        self.comboBox.setItemText(1, _translate("MainWindow", "No"))

        MainWindow.setWindowIcon(QtGui.QIcon("blood.png")) 



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.showMaximized()
    sys.exit(app.exec_())
