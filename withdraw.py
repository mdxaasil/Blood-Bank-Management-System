

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import mysql.connector as mc


class Ui_Withdraw(object):
    def setupUi(self, Withdraw):
        Withdraw.setObjectName("Withdraw")
        Withdraw.resize(400, 200)
        Withdraw.setMaximumSize(QtCore.QSize(400, 200))
        self.pushButton = QtWidgets.QPushButton(Withdraw)
        self.pushButton.setGeometry(QtCore.QRect(180, 150, 100, 30))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setFont(QtGui.QFont('Times', 10))
        self.pushButton.clicked.connect(self.click)


        self.label = QtWidgets.QLabel(Withdraw)
        self.label.setGeometry(QtCore.QRect(70, 75, 100, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAutoFillBackground(True)
        self.label.setObjectName("label")
     
        self.label_2 = QtWidgets.QLabel(Withdraw)
        self.label_2.setGeometry(QtCore.QRect(100, 100, 51, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
       
        self.label_3 = QtWidgets.QLabel(Withdraw)
        self.label_3.setGeometry(QtCore.QRect(55, 50, 101, 20))
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        
        self.hn = QtWidgets.QLineEdit(Withdraw)
        self.hn.setGeometry(QtCore.QRect(160, 50, 161, 20))
        self.hn.setObjectName("hn")
        
        self.bg = QtWidgets.QLineEdit(Withdraw)
        self.bg.setGeometry(QtCore.QRect(160, 75, 161, 20))
        self.bg.setObjectName("bg")

        self.vol = QtWidgets.QLineEdit(Withdraw)
        self.vol.setGeometry(QtCore.QRect(160, 100, 161, 20))
        self.vol.setReadOnly(False)
        self.vol.setObjectName("vol")

        self.retranslateUi(Withdraw)
        QtCore.QMetaObject.connectSlotsByName(Withdraw)

    def click(self):
        print("clicked")
        bg1 = self.bg.text()
        vol1=self.vol.text()
        hn1=self.hn.text()
        print(hn1,bg1, vol1)
        
        vol2=int(vol1)/1000
        #print(vol2)
        
        con=mc.connect(host="localhost",user="root",password="aasil",database="bloodbank")
        cur=con.cursor()
        
        cur.execute("update stock set volume=volume-{} where blood_group='{}'".format(vol2,bg1))
        con.commit()
        con.close()
       
        con=mc.connect(host="localhost",user="root",password="aasil",database="bloodbank")
        cur=con.cursor()
        cur.execute("insert into withdrawal values('{}','{}',{})".format(hn1,bg1,int(vol1)))
        con.commit()
        con.close()

        con=mc.connect(host="localhost",user="root",password="aasil",database="bloodbank")
        cur=con.cursor()
        cur.execute("select * from requests")
        req=cur.fetchall()
        print(req)
        for i in req:
            if i[0]==hn1 and i[1]==bg1:
                cur.execute("delete from requests where hname='{}'".format(hn1))
                
        con.commit()
        con.close()
        



        self.show_popup1()
         

    
    def show_popup1(self):
        msg=QMessageBox()
        msg.setWindowTitle("Withdraw")
        msg.setText("Withdrawal Successful and database updated.")
        msg.setIcon(QMessageBox.Information)
        msg.setWindowIcon(QtGui.QIcon('blood.png'))

        x=msg.exec_() 
    






    def retranslateUi(self, Withdraw):
        _translate = QtCore.QCoreApplication.translate
        Withdraw.setWindowTitle(_translate("Withdraw", "Withdraw"))
        Withdraw.setWindowIcon(QtGui.QIcon("blood.png")) 

        self.pushButton.setText(_translate("Withdraw", "Withdraw"))
        self.label.setText(_translate("Withdraw", "Blood Group"))
        self.label_2.setText(_translate("Withdraw", "Volume "))
        self.label_3.setText(_translate("Withdraw", "Hospital Name"))
        
        self.bg.setPlaceholderText(_translate("Withdraw", "A-/A+/B+/B-/O+/O-/AB+/AB-"))
        self.vol.setPlaceholderText(_translate("Withdraw", "in ml"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    OtherWindow= QtWidgets.QMainWindow()
    Withdraw = QtWidgets.QWidget()
    ui = Ui_Withdraw()
    ui.setupUi(Withdraw)

    Withdraw.show()
    sys.exit(app.exec_())
