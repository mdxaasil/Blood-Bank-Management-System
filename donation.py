

from os import close
from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector as mc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setMinimumSize(QtCore.QSize(1280, 720))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(580, 70, 231, 81))

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(400, 50, 101, 71))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("logo.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("logo")

        font = QtGui.QFont()
        font.setFamily("Nirmala UI Semilight")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.volume = QtWidgets.QLineEdit(self.centralwidget)
        self.volume.setGeometry(QtCore.QRect(880, 320, 191, 31))
        self.volume.setObjectName("volume")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(880, 530, 101, 31))
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
        self.checkBox.setGeometry(QtCore.QRect(880, 480, 261, 51))
        self.checkBox.setObjectName("checkBox")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(540, 20, 271, 81))
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.bg = QtWidgets.QLineEdit(self.centralwidget)
        self.bg.setGeometry(QtCore.QRect(880, 270, 191, 31))
        self.bg.setText("")
        self.bg.setObjectName("bg")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(210, 260, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(500, 190, 381, 31))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.hname = QtWidgets.QLineEdit(self.centralwidget)
        self.hname.setGeometry(QtCore.QRect(490, 270, 191, 31))
        self.hname.setObjectName("hname")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(320, 310, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(15)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(720, 260, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(15)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.dname = QtWidgets.QLineEdit(self.centralwidget)
        self.dname.setGeometry(QtCore.QRect(490, 320, 191, 31))
        self.dname.setObjectName("dname")
        self.ph = QtWidgets.QLineEdit(self.centralwidget)
        self.ph.setGeometry(QtCore.QRect(490, 420, 191, 31))
        self.ph.setObjectName("ph")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(310, 410, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(15)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(360, 460, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(15)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.email = QtWidgets.QLineEdit(self.centralwidget)
        self.email.setGeometry(QtCore.QRect(490, 470, 191, 31))
        self.email.setText("")
        self.email.setObjectName("email")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(740, 310, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(15)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(700, 360, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(15)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.dob = QtWidgets.QLineEdit(self.centralwidget)
        self.dob.setGeometry(QtCore.QRect(490, 370, 191, 31))
        self.dob.setObjectName("dob")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(390, 360, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(15)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(700, 410, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(15)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(880, 420, 191, 31))
        self.comboBox.setObjectName("source")
        self.comboBox.addItem("Hospital")
        self.comboBox.addItem("Camp")

        self.dod = QtWidgets.QLineEdit(self.centralwidget)
        self.dod.setGeometry(QtCore.QRect(880, 370, 191, 31))
        self.dod.setObjectName("dod")
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
        print("clicked")

        hname1=self.hname.text()
        dname1=self.dname.text()
        dob1=self.dob.text()
        ph1=self.ph.text()
        email1=self.email.text()
        bg1=self.bg.text()
        vol=self.volume.text()
        dod1=self.dod.text()

        source1=self.comboBox.currentText()

        print(hname1,dname1,dob1,ph1,email1,bg1,vol,dod1,source1)
        
        con=mc.connect(host="localhost",user="root",password="aasil",database="bloodbank")
        cur=con.cursor()
                
        cur.execute("select * from history")
        his=cur.fetchall()
        print(his)

        con.commit()
        con.close()
         
        cup=0

        for i in his:
            
            if i[0]==dname1 or i[4]==email1:
                                
                print("Updating")
                cone=mc.connect(host="localhost",user="root",password="aasil",database="bloodbank")
                curs=cone.cursor()
                curs.execute(" update history set volume={},source='{}',donation_date='{}',frequency=frequency+1 where name='{}'".format(int(vol),source1,dod1,dname1))
                cone.commit()
                cone.close()
                cup=1
            
            
        if cup==0:    
        
            print("Creating new")
            con=mc.connect(host="localhost",user="root",password="aasil",database="bloodbank")
            cur=con.cursor()
            cur.execute("insert into history values('{}','{}',{},{},'{}','{}','{}',1,'{}')".format(dname1,bg1,int(vol),ph1,email1,source1,dod1,dob1))
            con.commit()
            con.close()
        
        vol1=int(vol)/1000
        print(vol1)
        con=mc.connect(host="localhost",user="root",password="aasil",database="bloodbank")
        cur=con.cursor()
        cur.execute("update stock set volume=volume+{} where blood_group='{}'".format(vol1,bg1))
        con.commit()
        con.close()        
        self.show_popup()


                




        
    def show_popup(self):
        print("Popup")
        msg=QtWidgets.QMessageBox()
        msg.setWindowTitle("GD Blood Bank")
        msg.setText("You just saved a life. 💖")
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setWindowIcon(QtGui.QIcon('blood.png'))

        x=msg.exec_() 


           

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Donation Portal"))
        self.volume.setPlaceholderText(_translate("MainWindow", "in ml"))
        self.pushButton.setText(_translate("MainWindow", "Submit"))
        self.checkBox.setText(_translate("MainWindow", "I hereby confirm the data given above."))
        self.label.setText(_translate("MainWindow", "GD Blood Bank🩸"))
        self.bg.setPlaceholderText(_translate("MainWindow", "A-/A+/B+/B-/O+/O-/AB+/AB-"))
        self.label_4.setText(_translate("MainWindow", "Hospital name/Camp name:"))
        self.label_7.setText(_translate("MainWindow", "All the details are mandatory."))
        self.label_5.setText(_translate("MainWindow", "Donor\'s name:"))
        self.label_6.setText(_translate("MainWindow", "Blood group:"))
        self.ph.setPlaceholderText(_translate("MainWindow", "Phone / Landline"))
        self.label_8.setText(_translate("MainWindow", "Contact number:"))
        self.label_9.setText(_translate("MainWindow", "Email:"))
        self.label_10.setText(_translate("MainWindow", "Volume:"))
        self.label_11.setText(_translate("MainWindow", "Date of Donation:"))
        self.dob.setPlaceholderText(_translate("MainWindow", "YYYY-MM-DD"))
        self.label_12.setText(_translate("MainWindow", "DOB:"))
        self.label_13.setText(_translate("MainWindow", "Hospital / Camp:"))
        self.dod.setPlaceholderText(_translate("MainWindow", "YYYY-MM-DD"))
        MainWindow.setWindowIcon(QtGui.QIcon('blood.png'))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.showMaximized()
    sys.exit(app.exec_())
