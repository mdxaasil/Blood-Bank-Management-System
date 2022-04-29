from weakref import WeakKeyDictionary
import pywhatkit
import smtplib
from datetime import datetime
from PyQt5.QtWidgets import * 
from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector as mc
from withdraw import Ui_Withdraw
import tweepy
import string

import random


class Ui_Form(object):

    def openWindow(self):
        self.window= QtWidgets.QMainWindow()
        self.ui = Ui_Withdraw()
        self.ui.setupUi (self.window)
        self.window.show()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1280, 720)
        Form.setStyleSheet("background-color: beige ;border: 1px solid black;")

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setFont(QtGui.QFont('Sitka Small', 15))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
    
      

        self.lineEditDb = QtWidgets.QLineEdit(placeholderText="A-/A+/B+/B-/O+/O-/AB+/AB-")
        self.lineEditDb.setObjectName("lineEditDb")
        f = self.lineEditDb.font()
        f.setPointSize(15)
        self.lineEditDb.setFont(f)

        self.horizontalLayout.addWidget(self.lineEditDb)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.label_2.setFont(QtGui.QFont('Sitka Small', 15))

        self.horizontalLayout_2.addWidget(self.label_2)
        
        self.lineEditTable = QtWidgets.QLineEdit(placeholderText="history/stock/withdrawal/requests")
        self.lineEditTable.setObjectName("lineEditTable")
        f = self.lineEditTable.font()
        f.setPointSize(15)
        self.lineEditTable.setFont(f)
      

        self.horizontalLayout_2.addWidget(self.lineEditTable)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget = QtWidgets.QTableWidget(Form)


        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMinimumSize(QtCore.QSize(0, 0))
        #self.tableWidget.setRowCount(8)
        #self.tableWidget.setColumnCount(10)
        self.tableWidget.setObjectName("tableWidget")
        self.verticalLayout.addWidget(self.tableWidget)

        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet("background-color: rgb(0,85,255);")
        self.pushButton.setFont(QtGui.QFont('Bookman Old Style', 20))


        
        #we have connected clicked signal of button with the selec_data method
        self.pushButton.clicked.connect(self.click)
        self.verticalLayout.addWidget(self.pushButton)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form) 
        
        
    #this is the method for selecting data
    def click(self):
        try:
            need=self.lineEditDb.text()

            
            if need!="":
                print(need)

                if need == 'A+':
                    request=['A+','A-','O+','O-']
                    self.wd(req=request)
                 
                elif need == 'A-':
                    request=['A-','O-']
                    self.wd(req=request)

                elif need == 'B+':
                    request=['A-','O-','O+','O-']
                    self.wd(req=request)

                elif need == 'B-':
                    request=['B-','O-']
                    self.wd(req=request)

                elif need == 'AB+':
                    request=['A+','A-','O-','O+','AB-','AB+','B+','B-']
                    self.wd(req=request)
                
                elif need == 'AB-':
                    request=['A-','O-','AB-','B-']
                    self.wd(req=request)
                    
                elif need == 'O+':
                    request=['O+','O-']
                    self.wd(req=request)
                
                elif need == 'O-':
                    request=['O-']
                    self.wd(req=request)
                


            dbname = "bloodbank"
            tablename = self.lineEditTable.text()
            mydb = mc.connect(

                host="localhost",
                user="root",
                password="aasil",
                database=dbname
            )

            mycursor = mydb.cursor()

            mycursor.execute("SELECT * FROM {} ".format(tablename))

          
            result = mycursor.fetchall()
            
            
            
            if tablename=="stock":
                self.tableWidget.setColumnCount(2)
                print(tablename )
                self.tableWidget.setHorizontalHeaderLabels(['Stock', 'Volume'])


            elif tablename=="withdrawal":
                self.show_popup3()
                self.tableWidget.setColumnCount(3)
                header = self.tableWidget.horizontalHeader()       
                header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
                header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
                header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
                self.tableWidget.setHorizontalHeaderLabels(['Name', 'Blood group','Volume'])

                print(tablename)
            
            elif tablename=="requests":
               
                self.tableWidget.setColumnCount(4)
                header = self.tableWidget.horizontalHeader()       
                header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
                header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
                header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
                self.tableWidget.setHorizontalHeaderLabels(['Hospital Name', 'Blood group', 'Volume', 'Urgency'])


                print(tablename)

            elif tablename=="history":
                self.tableWidget.setColumnCount(9)
                
                header = self.tableWidget.horizontalHeader()       
                header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
                header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
                header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
                self.tableWidget.setHorizontalHeaderLabels(['Name', 'Blood group', 'Volume', 'Phone','Email','Latest donation','Date of donation','Frequency','DOB'])

                print(tablename)
            

            self.tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(result):
                print(row_number)
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    #print(column_number)
                    self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))



        except mc.Error as e:
            print("_____________________________________________________________")
            


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "GD Blood Bank"))
        Form.setWindowIcon(QtGui.QIcon("blood.png")) 

        self.label.setText(_translate("Form", "Enter the required blood:"))
        self.label_2.setText(_translate("Form", "Enter the field:"))
        self.pushButton.setText(_translate("Form", "Show Data"))
        
    def show_popup1(self):
        msg=QMessageBox()
        msg.setWindowTitle("Stock over")
        msg.setText("Mail sent to the donors donated before.")
        msg.setIcon(QMessageBox.Information)
        msg.setWindowIcon(QtGui.QIcon('blood.png'))

        x=msg.exec_() 

     

    def show_popup3(self):
        msg=QMessageBox()
        msg.setWindowTitle("Withdraw")
        msg.setText("Do you want to withdraw?")
        msg.setIcon(QMessageBox.Question)
        msg.setWindowIcon(QtGui.QIcon('blood.png'))
        msg.setStandardButtons(QMessageBox.Yes|QMessageBox.No)
        msg.setDefaultButton(QMessageBox.No)
        msg.buttonClicked.connect(self.wselect)
        
        x=msg.exec_() 
    
    def wselect(self,i):
        print(i.text())
        if i.text()=="&Yes":
            print('withdrawing')
            self.openWindow()
            
        elif i.text()=="&No":
            pass

    def wd(self,req):
        con=mc.connect(host="localhost",user="root",password="aasil",database="bloodbank")
        cur=con.cursor()
        cur.execute("select * from history")
        h=cur.fetchall()
        con.close()
        con=mc.connect(host="localhost",user="root",password="aasil",database="bloodbank")
        cur=con.cursor()
        cur.execute("select * from stock")
        s=cur.fetchall()
        con.close()
        print(h)
        print("\n")
        print(s)
        tem=0 
        instock=[]
        for i in s:
            if i[0] in req:
                if i[1]>=2:
                    tem=1
                    instock.append(i[0])
                    
                
        print(instock)
        print(tem)

        if tem==1:
            pr=""
            for i in instock:
                pr=pr+i+','
            
            pr=pr[:-1]
            print(pr)

            msg=QMessageBox()
            msg.setWindowTitle("Blood available")
            msg.setText("Blood available and can be withdrawed.")
            msg.setIcon(QMessageBox.Information)
            msg.setWindowIcon(QtGui.QIcon('blood.png'))
            msg.setInformativeText('Matching blood groups: '+pr)
            x=msg.exec_()

        elif tem==0:            
            
            print("Sending mail requesting blood to the previous donours.")
            
            consumer_key='VU0N0HvlafOUmCLSQX6xRzy0D'
            consumer_secret='bO4Om9Qp9lGc7em4CsYi1iBl7y2pBrinOkavd0S51AGVpVX341'
            access_token='1343258269628788736-dD4L6c1MaiJLjPDl9GclTcgWfXnyxf'
            access_token_secret='1cYO9LvCY4iTUy2X7sReYHiwsK9kyJdGdwakoexd95oXF'
            auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
            auth.set_access_token(access_token,access_token_secret)
            oauth=auth
            api=tweepy.API(oauth)

            random.seed(2)
            #r=str(random.random())
            letters = string.ascii_lowercase
            r=( ''.join(random.choice(letters) for i in range(18)) )

            bgs=""
            for i in req:
                bgs=bgs+str(i)+" "

            cont=""" We need """+bgs+""" group blood for an 
emergency case at GD Hospital, . If you are willing to be a donor, please reply to this message as
soon as possible.

Contact Details: 9823815628

Kind regards,
GD Blood bank technician.


"""+r

            api.update_status(cont)
            print(cont)

            print("Tweet sent")
            
            
            for q in h:
                
                if q[1] in req:
                    before=q[6]                 
                    now=datetime.today().strftime('%Y-%m-%d')
                    date_format = "%Y-%m-%d"
                    a = datetime.strptime(str(before), date_format)
                    b = datetime.strptime(str(now), date_format)
                    delta = b - a
                    diff=delta.days
                    
                    if diff>56:
                        print(before,'---',now)
                        print(q[0])
                        print(diff)
                        print(q[1])
                        print("Eligible")

                        m=q[4]
                        con="""Dear """+str(q[0])+""", 
This is a message from GD Blood bank. We need """+str(q[1])+""" group blood for an 
emergency case. If you are willing to be a donor, please reply to this message as
soon as possible.

Contact Details: 9823815628

Kind regards,
GD Blood bank technician.  """

                    
                        message = 'Subject: {}\n\n{}'.format("Wanted Blood Donor", con)

                        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                        server.login('sendermail2020@gmail.com', 'imsending')
                        print(m)
                        server.sendmail('sendermail2020@gmail.com',m,message)
                        server.quit()
                        print("mail sent successfully")   

                        P='+91'+str(q[3])
                        print(P)
                        T=datetime.now().strftime("%#H:%#M:%#S")
                        x =T.split(":")
                        H=x[0]
                        M=int(x[1])+1
                        S=x[2]

                        
                        pywhatkit.sendwhatmsg(P,con,int(H),M)
                    else:
                        continue
                        
            msg=QMessageBox()
            msg.setWindowTitle("Stock over")
            msg.setText("Message sent to the previous donors.📞")
            msg.setIcon(QMessageBox.Information)
            msg.setWindowIcon(QtGui.QIcon('blood.png'))

            x=msg.exec_() 



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.showMaximized()
    
    sys.exit(app.exec_())

