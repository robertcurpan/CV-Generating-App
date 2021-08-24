import os
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QFont, QTextDocument
from PyQt5.QtPrintSupport import QPrinter
from PyQt5.QtWidgets import QApplication



############################### CLASSES ##########################################

class Ui_dialog1(object):
    def setupUi(self, dialog1):
        dialog1.setObjectName("dialog1")
        dialog1.resize(800, 640)
        dialog1.setBaseSize(QtCore.QSize(0, 0))
        #self.photo_label = QtWidgets.QLabel(dialog1)
        #self.photo_label.setGeometry(QtCore.QRect(420, 110, 300, 400))
        #self.photo_label.setText("")
        #self.photo_label.setScaledContents(True)
        #self.photo_label.setObjectName("photo_label")
        self.frame = QtWidgets.QFrame(dialog1)
        self.frame.setGeometry(QtCore.QRect(20, 100, 311, 461))
        font = QtGui.QFont()
        font.setPointSize(12)
        font1 = QtGui.QFont()
        font1.setPointSize(10)
        self.frame.setFont(font)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.firstName_label = QtWidgets.QLabel(self.frame)
        self.firstName_label.setGeometry(QtCore.QRect(20, 20, 121, 21))
        self.firstName_label.setObjectName("firstName_label")
        self.firstName_lineEdit = QtWidgets.QLineEdit(self.frame)
        self.firstName_lineEdit.setFont(font1)
        self.firstName_lineEdit.setGeometry(QtCore.QRect(20, 50, 281, 41))
        self.firstName_lineEdit.setObjectName("firstName_lineEdit")
        self.lastName_label = QtWidgets.QLabel(self.frame)
        self.lastName_label.setGeometry(QtCore.QRect(20, 100, 121, 21))
        self.lastName_label.setObjectName("lastName_label")
        self.lastName_lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lastName_lineEdit.setFont(font1)
        self.lastName_lineEdit.setGeometry(QtCore.QRect(20, 130, 281, 41))
        self.lastName_lineEdit.setObjectName("lastName_lineEdit")
        self.email_label = QtWidgets.QLabel(self.frame)
        self.email_label.setGeometry(QtCore.QRect(20, 190, 111, 21))
        self.email_label.setObjectName("email_label")
        self.email_lineEdit = QtWidgets.QLineEdit(self.frame)
        self.email_lineEdit.setFont(font1)
        self.email_lineEdit.setGeometry(QtCore.QRect(20, 220, 281, 41))
        self.email_lineEdit.setObjectName("email_lineEdit")
        self.phone_label = QtWidgets.QLabel(self.frame)
        self.phone_label.setGeometry(QtCore.QRect(20, 280, 101, 21))
        self.phone_label.setObjectName("phone_label")
        self.phone_lineEdit = QtWidgets.QLineEdit(self.frame)
        self.phone_lineEdit.setFont(font1)
        self.phone_lineEdit.setGeometry(QtCore.QRect(20, 310, 281, 41))
        self.phone_lineEdit.setObjectName("phone_lineEdit")
        self.date_label = QtWidgets.QLabel(self.frame)
        self.date_label.setGeometry(QtCore.QRect(20, 370, 151, 21))
        self.date_label.setObjectName("date_label")
        self.date_lineEdit = QtWidgets.QLineEdit(self.frame)
        self.date_lineEdit.setFont(font1)
        self.date_lineEdit.setGeometry(QtCore.QRect(20, 400, 281, 41))
        self.date_lineEdit.setObjectName("date_lineEdit")
        self.gotoProfileScreen_button = QtWidgets.QPushButton(dialog1)
        self.gotoProfileScreen_button.setGeometry(QtCore.QRect(600, 570, 161, 61))
        self.gotoProfileScreen_button.setObjectName("gotoProfileScreen_button")
        self.gotoProfileScreen_button.setFont(font)
        self.title1_label = QtWidgets.QLabel(dialog1)
        self.title1_label.setGeometry(QtCore.QRect(270, 30, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.title1_label.setFont(font)
        self.title1_label.setAlignment(QtCore.Qt.AlignCenter)
        self.title1_label.setObjectName("title1_label")
        #self.choosePhoto_button = QtWidgets.QPushButton(dialog1)
        #self.choosePhoto_button.setGeometry(QtCore.QRect(360, 530, 141, 30))
        #self.choosePhoto_button.setObjectName("choosePhoto_button")

        # Set default "Insert Image" photo
        #myImg = QImage()
        #myImg.loadFromData(requests.get("https://www.lynchmere-pc.gov.uk/wp-content/uploads/2015/12/insert-picture-here.jpg").content)
        #self.photo_label.setPixmap(QtGui.QPixmap(myImg))

        # Connect "Choose Photo" button to handler
        #self.choosePhoto_button.clicked.connect(self.browseImage)

        # Connect "Next" button to the Profile Screen
        self.gotoProfileScreen_button.clicked.connect(self.gotoProfile)

        self.retranslateUi(dialog1)
        QtCore.QMetaObject.connectSlotsByName(dialog1)

    def retranslateUi(self, dialog1):
        _translate = QtCore.QCoreApplication.translate
        dialog1.setWindowTitle(_translate("dialog1", "CV Generator - Personal Information"))
        self.firstName_label.setText(_translate("dialog1", "First Name"))
        self.lastName_label.setText(_translate("dialog1", "Last Name"))
        self.email_label.setText(_translate("dialog1", "Email"))
        self.phone_label.setText(_translate("dialog1", "Phone"))
        self.date_label.setText(_translate("dialog1", "Date of birth"))
        self.gotoProfileScreen_button.setText(_translate("dialog1", "Next"))
        self.title1_label.setText(_translate("dialog1", "Personal Information"))
        #self.choosePhoto_button.setText(_translate("dialog1", "Choose Photo"))

    '''
    def browseImage(self):
        fname = QFileDialog.getOpenFileName(options=QtWidgets.QFileDialog.DontUseNativeDialog)
        self.imagePath = fname[0]
        self.photo_label.setPixmap(QtGui.QPixmap(self.imagePath))
        print(self.imagePath)
    '''

    def gotoProfile(self):
        localHtml = "<html><head><title>CV " + self.firstName_lineEdit.text() + " " + self.lastName_lineEdit.text() + "</title></head>"
        localHtml += "<body>" + "<h2 style=\"text-align: center;\">CV " + self.firstName_lineEdit.text() + " " + self.lastName_lineEdit.text() + "</h2><p>&nbsp;</p><p>&nbsp;</p><p style=\"text-align: left;\"><strong>PERSONAL INFORMATION</strong></p><hr /><p>Name:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;" + self.lastName_lineEdit.text() + " " + self.firstName_lineEdit.text() +"<br>Date of birth:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;" + self.date_lineEdit.text() + "<br>Email:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;" + self.email_lineEdit.text() +"<br>Phone:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;" + self.phone_lineEdit.text() +"</p>"

        globalQueue.append(localHtml)

        widget.setCurrentIndex(widget.currentIndex() + 1)

class Ui_dialog2(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(800, 640)
        self.title2_label = QtWidgets.QLabel(Dialog)
        self.title2_label.setGeometry(QtCore.QRect(330, 20, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.title2_label.setFont(font)
        self.title2_label.setAlignment(QtCore.Qt.AlignCenter)
        self.title2_label.setObjectName("title2_label")
        self.profile_textEdit = QtWidgets.QTextEdit(Dialog)
        self.profile_textEdit.setGeometry(QtCore.QRect(40, 100, 711, 321))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.profile_textEdit.setFont(font)
        self.profile_textEdit.setObjectName("profile_textEdit")
        self.backToPersonalInformationScreen_button = QtWidgets.QPushButton(Dialog)
        self.backToPersonalInformationScreen_button.setGeometry(QtCore.QRect(30, 570, 151, 61))
        self.backToPersonalInformationScreen_button.setFont(font)
        self.backToPersonalInformationScreen_button.setObjectName("backToPersonalInformationScreen_button")
        self.gotoWorkExperienceScreen_button = QtWidgets.QPushButton(Dialog)
        self.gotoWorkExperienceScreen_button.setGeometry(QtCore.QRect(600, 570, 161, 61))
        self.gotoWorkExperienceScreen_button.setFont(font)
        self.gotoWorkExperienceScreen_button.setObjectName("gotoWorkExperienceScreen_button")

        # Connect "Back" button to the Personal Information Screen
        self.backToPersonalInformationScreen_button.clicked.connect(self.backToPersonalInformation)
        # Connect "Next" button to the Work Experience Screen
        self.gotoWorkExperienceScreen_button.clicked.connect(self.gotoWorkExperience)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.title2_label.setText(_translate("Dialog", "Profile"))
        self.profile_textEdit.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.profile_textEdit.setPlaceholderText(_translate("Dialog", "Describe yourself in a few paragraphs ..."))
        self.backToPersonalInformationScreen_button.setText(_translate("Dialog", "Back"))
        self.gotoWorkExperienceScreen_button.setText(_translate("Dialog", "Next"))

    def backToPersonalInformation(self):
        if len(globalQueue) > 0:
            globalQueue.pop(-1)
        widget.setCurrentIndex(widget.currentIndex() - 1)

    def gotoWorkExperience(self):
        if len(self.profile_textEdit.toPlainText()) > 1:
            localHtml = "<p>&nbsp;</p><p style=\"text-align: left;\"><strong>PROFILE</strong></p><hr /><p>" + self.profile_textEdit.toPlainText() + "</p>"

            globalQueue.append(localHtml)

        widget.setCurrentIndex(widget.currentIndex() + 1)

class Ui_dialog3(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(800, 640)
        self.title3_label = QtWidgets.QLabel(Dialog)
        self.title3_label.setGeometry(QtCore.QRect(260, 20, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.title3_label.setFont(font)
        self.title3_label.setAlignment(QtCore.Qt.AlignCenter)
        self.title3_label.setObjectName("title3_label")
        font.setPointSize(8)
        font.setBold(False)
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(460, 110, 321, 441))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.previewWorkExperience_label = QtWidgets.QLabel(self.frame)
        self.previewWorkExperience_label.setGeometry(QtCore.QRect(10, 0, 301, 431))
        self.previewWorkExperience_label.setFont(QFont('Ubuntu', 8))
        self.previewWorkExperience_label.setWordWrap(True)
        self.previewWorkExperience_label.setText("")
        self.previewWorkExperience_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.previewWorkExperience_label.setObjectName("previewWorkExperience_label")
        font.setPointSize(12)
        self.gotoEducationScreen_button = QtWidgets.QPushButton(Dialog)
        self.gotoEducationScreen_button.setGeometry(QtCore.QRect(600, 570, 161, 61))
        self.gotoEducationScreen_button.setFont(font)
        self.gotoEducationScreen_button.setObjectName("gotoEducationScreen_button")
        self.backToProfileScreen_button = QtWidgets.QPushButton(Dialog)
        self.backToProfileScreen_button.setGeometry(QtCore.QRect(30, 570, 151, 61))
        self.backToProfileScreen_button.setFont(font)
        self.backToProfileScreen_button.setObjectName("backToProfileScreen_button")
        font.setPointSize(10)
        self.inputPreview_label = QtWidgets.QLabel(Dialog)
        self.inputPreview_label.setGeometry(QtCore.QRect(560, 80, 121, 21))
        self.inputPreview_label.setFont(font)
        self.inputPreview_label.setObjectName("inputPreview_label")
        self.submit_button = QtWidgets.QPushButton(Dialog)
        self.submit_button.setGeometry(QtCore.QRect(340, 520, 101, 30))
        self.submit_button.setFont(font)
        self.submit_button.setObjectName("submit_button")
        self.undo_button = QtWidgets.QPushButton(Dialog)
        self.undo_button.setGeometry(QtCore.QRect(30, 520, 101, 30))
        self.undo_button.setFont(font)
        self.undo_button.setObjectName("undo_button")
        self.timePeriod_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.timePeriod_lineEdit.setGeometry(QtCore.QRect(30, 230, 411, 29))
        self.timePeriod_lineEdit.setFont(font)
        self.timePeriod_lineEdit.setText("")
        self.timePeriod_lineEdit.setObjectName("timePeriod_lineEdit")
        self.company_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.company_lineEdit.setGeometry(QtCore.QRect(30, 300, 411, 29))
        self.company_lineEdit.setFont(font)
        self.company_lineEdit.setObjectName("company_lineEdit")
        self.jobPosition_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.jobPosition_lineEdit.setGeometry(QtCore.QRect(30, 370, 411, 29))
        self.jobPosition_lineEdit.setFont(font)
        self.jobPosition_lineEdit.setObjectName("jobPosition_lineEdit")
        self.label11 = QtWidgets.QLabel(Dialog)
        self.label11.setGeometry(QtCore.QRect(30, 200, 131, 21))
        self.label11.setFont(font)
        self.label11.setObjectName("label11")
        self.label12 = QtWidgets.QLabel(Dialog)
        self.label12.setGeometry(QtCore.QRect(30, 270, 191, 21))
        self.label12.setFont(font)
        self.label12.setObjectName("label12")
        self.label13 = QtWidgets.QLabel(Dialog)
        self.label13.setGeometry(QtCore.QRect(30, 340, 201, 21))
        self.label13.setFont(font)
        self.label13.setObjectName("label13")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 80, 391, 21))
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 110, 381, 21))
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 140, 391, 21))
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(30, 170, 401, 21))
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(30, 410, 401, 21))
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.workProjects_textEdit = QtWidgets.QTextEdit(Dialog)
        self.workProjects_textEdit.setGeometry(QtCore.QRect(30, 440, 411, 71))
        self.workProjects_textEdit.setFont(font)
        self.workProjects_textEdit.setObjectName("workProjects_textEdit")

        # Declare the local queue
        self.localQueue = []
        # Declare the list of fields
        self.listOfFields = []

        # Connect the "Back" button to the Profile Screen
        self.backToProfileScreen_button.clicked.connect(self.backToProfile)
        # Connect the "Next" button to the Education Screen
        self.gotoEducationScreen_button.clicked.connect(self.gotoEducation)
        # Connect "Submit" button to handler
        self.submit_button.clicked.connect(self.submitLine)
        # Connect "Undo" button to handler
        self.undo_button.clicked.connect(self.undoLine)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.title3_label.setText(_translate("Dialog", "Work Experience"))
        self.gotoEducationScreen_button.setText(_translate("Dialog", "Next"))
        self.backToProfileScreen_button.setText(_translate("Dialog", "Back"))
        self.inputPreview_label.setText(_translate("Dialog", "Input preview"))
        self.submit_button.setText(_translate("Dialog", "Submit"))
        self.undo_button.setText(_translate("Dialog", "Undo"))
        self.timePeriod_lineEdit.setPlaceholderText(_translate("Dialog", "Ex: 2012 - 2015"))
        self.company_lineEdit.setPlaceholderText(_translate("Dialog", "Ex: Amazon"))
        self.jobPosition_lineEdit.setPlaceholderText(_translate("Dialog", "Ex: Software Engineer"))
        self.label11.setText(_translate("Dialog", "Time period"))
        self.label12.setText(_translate("Dialog", "Company/Institution"))
        self.label13.setText(_translate("Dialog", "Job position"))
        self.label.setText(_translate("Dialog", "Complete the blank spaces and press submit in"))
        self.label_2.setText(_translate("Dialog", "order to commit one line of input. Repeat the "))
        self.label_3.setText(_translate("Dialog", "process until you have submitted all your work"))
        self.label_4.setText(_translate("Dialog", "experience. Press Undo to remove the last input."))
        self.label_5.setText(_translate("Dialog", "Projects you have worked on during your stay"))
        self.workProjects_textEdit.setPlaceholderText(_translate("Dialog", "Ex: Worked at the development of the X app (You can write multiple lines here)"))

    def backToProfile(self):
        if len(globalQueue) > 0:
            globalQueue.pop(-1)
        widget.setCurrentIndex(widget.currentIndex() - 1)

    def gotoEducation(self):
        if len(self.listOfFields) > 0:
            localHtml = "<p>&nbsp;</p><p style=\"text-align: left;\"><strong>WORK EXPERIENCE</strong></p><hr />"
            for elem in self.listOfFields:
                spatiere = ""
                for i in range(32):
                    spatiere += "&nbsp;"

                if elem[0] != "$":
                    localHtml += "<p>" + elem[0] + "<br>"
                else:
                    localHtml += "<p>Unknown time period<br>"

                if elem[1] != "$":
                    localHtml += spatiere + "<span style=\"color: #3366ff;\">" + elem[1] + "</span><br />"
                else:
                    localHtml += spatiere + "Unknown job position<br />"

                if elem[2] != "$":
                    localHtml += spatiere + "<em>-&gt; " + elem[2] + "</em>"
                else:
                    localHtml += spatiere + "<em>-&gt; " + "Unknown company" + "</em>"

                if elem[3] != "$":
                    for i in elem[3]:
                        localHtml += "<br>" + spatiere + "&nbsp;&nbsp;&nbsp;* " + i
                localHtml += "</p>"

            globalQueue.append(localHtml)

        widget.setCurrentIndex(widget.currentIndex() + 1)

    def submitLine(self):
        auxList = []
        lineOfInfo = " ** "

        if len(self.timePeriod_lineEdit.text()) > 0:
            lineOfInfo += self.timePeriod_lineEdit.text() + " : "
            auxList.append(self.timePeriod_lineEdit.text())
        else:
            lineOfInfo += "Unknown time period" + " : "
            auxList.append("$")

        if len(self.jobPosition_lineEdit.text()) > 0:
            lineOfInfo += self.jobPosition_lineEdit.text() + "\n\t-> "
            auxList.append(self.jobPosition_lineEdit.text())
        else:
            lineOfInfo += "Unknown job position" + "\n\t-> "
            auxList.append("$")

        if len(self.company_lineEdit.text()) > 0:
            lineOfInfo += self.company_lineEdit.text() + "\n"
            auxList.append(self.company_lineEdit.text())
        else:
            lineOfInfo += "Unknown company" + "\n"
            auxList.append("$")

        if len(self.workProjects_textEdit.toPlainText()) > 0:
            workProjectList = self.workProjects_textEdit.toPlainText().split("\n")
            for line in workProjectList:
                lineOfInfo += "\t- " + line + "\n"
            auxList.append(workProjectList)
        else:
            auxList.append("$")

        self.localQueue.append(lineOfInfo)
        self.displayQueueOnPreview()

        self.listOfFields.append(auxList)

        self.timePeriod_lineEdit.setText("")
        self.company_lineEdit.setText("")
        self.jobPosition_lineEdit.setText("")
        self.workProjects_textEdit.setText("")

    def undoLine(self):
        if len(self.localQueue) > 0:
            self.localQueue.pop(-1)
            self.listOfFields.pop(-1)
        self.displayQueueOnPreview()

    def displayQueueOnPreview(self):
        previewText = ""
        for line in self.localQueue:
            previewText += line
        self.previewWorkExperience_label.setText(previewText)

class Ui_dialog4(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(800, 640)
        self.title4_label = QtWidgets.QLabel(Dialog)
        self.title4_label.setGeometry(QtCore.QRect(260, 20, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.title4_label.setFont(font)
        self.title4_label.setAlignment(QtCore.Qt.AlignCenter)
        self.title4_label.setObjectName("title4_label")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(460, 110, 321, 441))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.previewEducation_label = QtWidgets.QLabel(self.frame)
        self.previewEducation_label.setGeometry(QtCore.QRect(10, 0, 301, 431))
        self.previewEducation_label.setFont(QFont('Ubuntu', 8))
        self.previewEducation_label.setWordWrap(True)
        self.previewEducation_label.setText("")
        self.previewEducation_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.previewEducation_label.setObjectName("previewEducation_label")
        font.setPointSize(12)
        font.setBold(False)
        self.gotoSkillsScreen_button = QtWidgets.QPushButton(Dialog)
        self.gotoSkillsScreen_button.setGeometry(QtCore.QRect(600, 570, 161, 61))
        self.gotoSkillsScreen_button.setFont(font)
        self.gotoSkillsScreen_button.setObjectName("gotoSkillsScreen_button")
        self.backToWorkExperienceScreen_button = QtWidgets.QPushButton(Dialog)
        self.backToWorkExperienceScreen_button.setGeometry(QtCore.QRect(30, 570, 151, 61))
        self.backToWorkExperienceScreen_button.setFont(font)
        self.backToWorkExperienceScreen_button.setObjectName("backToWorkExperienceScreen_button")
        font.setPointSize(10)
        self.inputPreview_label = QtWidgets.QLabel(Dialog)
        self.inputPreview_label.setGeometry(QtCore.QRect(560, 80, 121, 21))
        self.inputPreview_label.setFont(font)
        self.inputPreview_label.setObjectName("inputPreview_label")
        self.submit_button = QtWidgets.QPushButton(Dialog)
        self.submit_button.setGeometry(QtCore.QRect(340, 520, 101, 30))
        self.submit_button.setFont(font)
        self.submit_button.setObjectName("submit_button")
        self.undo_button = QtWidgets.QPushButton(Dialog)
        self.undo_button.setGeometry(QtCore.QRect(30, 520, 101, 30))
        self.undo_button.setFont(font)
        self.undo_button.setObjectName("undo_button")
        self.timePeriod_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.timePeriod_lineEdit.setGeometry(QtCore.QRect(30, 250, 411, 29))
        self.timePeriod_lineEdit.setFont(font)
        self.timePeriod_lineEdit.setText("")
        self.timePeriod_lineEdit.setObjectName("timePeriod_lineEdit")
        self.university_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.university_lineEdit.setGeometry(QtCore.QRect(30, 320, 411, 29))
        self.university_lineEdit.setFont(font)
        self.university_lineEdit.setText("")
        self.university_lineEdit.setObjectName("university_lineEdit")
        self.label11 = QtWidgets.QLabel(Dialog)
        self.label11.setGeometry(QtCore.QRect(30, 220, 131, 21))
        self.label11.setFont(font)
        self.label11.setObjectName("label11")
        self.label12 = QtWidgets.QLabel(Dialog)
        self.label12.setGeometry(QtCore.QRect(30, 290, 151, 21))
        self.label12.setFont(font)
        self.label12.setObjectName("label12")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 70, 391, 21))
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 100, 381, 21))
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 130, 411, 21))
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(30, 160, 401, 21))
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(30, 190, 141, 21))
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.major_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.major_lineEdit.setGeometry(QtCore.QRect(30, 390, 411, 29))
        self.major_lineEdit.setFont(font)
        self.major_lineEdit.setText("")
        self.major_lineEdit.setObjectName("major_lineEdit")
        self.label12_2 = QtWidgets.QLabel(Dialog)
        self.label12_2.setGeometry(QtCore.QRect(30, 360, 111, 21))
        self.label12_2.setFont(font)
        self.label12_2.setObjectName("label12_2")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(30, 430, 411, 21))
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.relevantEducationInfo_textEdit = QtWidgets.QTextEdit(Dialog)
        self.relevantEducationInfo_textEdit.setGeometry(QtCore.QRect(30, 460, 411, 51))
        self.relevantEducationInfo_textEdit.setFont(font)
        self.relevantEducationInfo_textEdit.setObjectName("relevantEducationInfo_textEdit")

        # Declare the local queue
        self.localQueue = []
        # Declare the list of fields
        self.listOfFields = []

        # Connect the "Back" button to the Work Experience Screen
        self.backToWorkExperienceScreen_button.clicked.connect(self.backToWorkExperience)
        # Connect the "Next" button to the Skills Screen
        self.gotoSkillsScreen_button.clicked.connect(self.gotoSkills)
        # Connect "Submit" button to handler
        self.submit_button.clicked.connect(self.submitLine)
        # Connect "Undo" button to handler
        self.undo_button.clicked.connect(self.undoLine)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.title4_label.setText(_translate("Dialog", "Education"))
        self.gotoSkillsScreen_button.setText(_translate("Dialog", "Next"))
        self.backToWorkExperienceScreen_button.setText(_translate("Dialog", "Back"))
        self.inputPreview_label.setText(_translate("Dialog", "Input preview"))
        self.submit_button.setText(_translate("Dialog", "Submit"))
        self.undo_button.setText(_translate("Dialog", "Undo"))
        self.timePeriod_lineEdit.setPlaceholderText(_translate("Dialog", "Ex: 2012 - 2015"))
        self.university_lineEdit.setPlaceholderText(_translate("Dialog", "Ex: MIT / National Highschool"))
        self.label11.setText(_translate("Dialog", "Time period"))
        self.label12.setText(_translate("Dialog", "University/School"))
        self.label.setText(_translate("Dialog", "Complete the blank spaces and press submit in"))
        self.label_2.setText(_translate("Dialog", "order to commit one line of input. Repeat the "))
        self.label_3.setText(_translate("Dialog", "process until you have submitted all the education"))
        self.label_4.setText(_translate("Dialog", "cycles you attended. Press Undo to remove the"))
        self.label_5.setText(_translate("Dialog", "last line of input."))
        self.major_lineEdit.setPlaceholderText(_translate("Dialog", "Ex: Computer Science / Maths & Informatics"))
        self.label12_2.setText(_translate("Dialog", "Major/Profile"))
        self.label_6.setText(_translate("Dialog", "Relevant information about this cycle"))
        self.relevantEducationInfo_textEdit.setPlaceholderText(_translate("Dialog", "Ex: Silver Medal at the International Mathematics Olympiad (You can write multiple lines here)"))

    def backToWorkExperience(self):
        if len(globalQueue) > 0:
            globalQueue.pop(-1)
        widget.setCurrentIndex(widget.currentIndex() - 1)

    def gotoSkills(self):
        if len(self.listOfFields) > 0:
            localHtml = "<p>&nbsp;</p><p style=\"text-align: left;\"><strong>EDUCATION</strong></p><hr />"
            for elem in self.listOfFields:
                spatiere = ""
                for i in range(32):
                    spatiere += "&nbsp;"

                if elem[0] != "$":
                    localHtml += "<p>" + elem[0] + "<br>"
                else:
                    localHtml += "<p>Unknown time period<br>"

                if elem[1] != "$":
                    localHtml += spatiere + "<span style=\"color: #3366ff;\">" + elem[1] + "</span><br />"
                else:
                    localHtml += spatiere + "Unknown major/profile" + "<br />"

                if elem[2] != "$":
                    localHtml += spatiere + "<em>-&gt; " + elem[2] + "</em>"
                else:
                    localHtml += spatiere + "<em>-&gt; " + "Unknown university/school" + "</em>"

                if elem[3] != "$":
                    for i in elem[3]:
                        localHtml += "<br>" + spatiere + "&nbsp;&nbsp;&nbsp;* " + i
                localHtml += "</p>"

            globalQueue.append(localHtml)

        widget.setCurrentIndex(widget.currentIndex() + 1)

    def submitLine(self):
        auxList = []
        lineOfInfo = " ** "

        if len(self.timePeriod_lineEdit.text()) > 0:
            lineOfInfo += self.timePeriod_lineEdit.text() + " : "
            auxList.append(self.timePeriod_lineEdit.text())
        else:
            lineOfInfo += "Unknown time period : "
            auxList.append("$")

        if len(self.major_lineEdit.text()) > 0:
            lineOfInfo += self.major_lineEdit.text() + "\n\t-> "
            auxList.append(self.major_lineEdit.text())
        else:
            lineOfInfo += "Unknown major/profile" + "\n\t-> "
            auxList.append("$")

        if len(self.university_lineEdit.text()) > 0:
            lineOfInfo += self.university_lineEdit.text() + "\n"
            auxList.append(self.university_lineEdit.text())
        else:
            lineOfInfo += "Unknown university/school" + "\n"
            auxList.append("$")

        #lineOfInfo = " ** " + self.timePeriod_lineEdit.text() + " : " + self.major_lineEdit.text() + "\n\t-> " + self.university_lineEdit.text() + "\n"
        if len(self.relevantEducationInfo_textEdit.toPlainText()) > 0:
            relevantEducationInfoList = self.relevantEducationInfo_textEdit.toPlainText().split("\n")
            for line in relevantEducationInfoList:
                lineOfInfo += "\t- " + line + "\n"
            auxList.append(relevantEducationInfoList)
        else:
            auxList.append("$")

        self.localQueue.append(lineOfInfo)
        self.displayQueueOnPreview()

        self.listOfFields.append(auxList)

        self.timePeriod_lineEdit.setText("")
        self.university_lineEdit.setText("")
        self.major_lineEdit.setText("")
        self.relevantEducationInfo_textEdit.setText("")

    def undoLine(self):
        if len(self.localQueue) > 0:
            self.localQueue.pop(-1)
            self.listOfFields.pop(-1)
        self.displayQueueOnPreview()

    def displayQueueOnPreview(self):
        previewText = ""
        for line in self.localQueue:
            previewText += line
        self.previewEducation_label.setText(previewText)

class Ui_dialog5(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(800, 640)
        self.title5_label = QtWidgets.QLabel(Dialog)
        self.title5_label.setGeometry(QtCore.QRect(260, 20, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.title5_label.setFont(font)
        self.title5_label.setAlignment(QtCore.Qt.AlignCenter)
        self.title5_label.setObjectName("title5_label")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(460, 110, 321, 441))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.previewSkills_label = QtWidgets.QLabel(self.frame)
        self.previewSkills_label.setGeometry(QtCore.QRect(10, 0, 301, 431))
        self.previewSkills_label.setFont(QFont('Ubuntu', 8))
        self.previewSkills_label.setWordWrap(True)
        self.previewSkills_label.setText("")
        self.previewSkills_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.previewSkills_label.setObjectName("previewSkills_label")
        font.setBold(False)
        font.setPointSize(12)
        self.gotoAwardsScreen_button = QtWidgets.QPushButton(Dialog)
        self.gotoAwardsScreen_button.setGeometry(QtCore.QRect(600, 570, 161, 61))
        self.gotoAwardsScreen_button.setFont(font)
        self.gotoAwardsScreen_button.setObjectName("gotoAwardsScreen_button")
        self.backToEducationScreen_button = QtWidgets.QPushButton(Dialog)
        self.backToEducationScreen_button.setGeometry(QtCore.QRect(30, 570, 151, 61))
        self.backToEducationScreen_button.setFont(font)
        self.backToEducationScreen_button.setObjectName("backToEducationScreen_button")
        font.setPointSize(10)
        self.inputPreview_label = QtWidgets.QLabel(Dialog)
        self.inputPreview_label.setGeometry(QtCore.QRect(560, 80, 121, 21))
        self.inputPreview_label.setFont(font)
        self.inputPreview_label.setObjectName("inputPreview_label")
        self.submit_button = QtWidgets.QPushButton(Dialog)
        self.submit_button.setGeometry(QtCore.QRect(340, 240, 101, 30))
        self.submit_button.setFont(font)
        self.submit_button.setObjectName("submit_button")
        self.undo_button = QtWidgets.QPushButton(Dialog)
        self.undo_button.setGeometry(QtCore.QRect(30, 240, 101, 30))
        self.undo_button.setFont(font)
        self.undo_button.setObjectName("undo_button")
        self.skill_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.skill_lineEdit.setGeometry(QtCore.QRect(30, 190, 411, 29))
        self.skill_lineEdit.setFont(font)
        self.skill_lineEdit.setText("")
        self.skill_lineEdit.setObjectName("skill_lineEdit")
        self.label11 = QtWidgets.QLabel(Dialog)
        self.label11.setGeometry(QtCore.QRect(30, 160, 51, 21))
        self.label11.setFont(font)
        self.label11.setObjectName("label11")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 110, 391, 21))
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 350, 391, 21))
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 380, 431, 21))
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(30, 410, 331, 21))
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        # Declare the local queue
        self.localQueue = []
        # Declare the list of skills
        self.listOfSkills = []

        # Connect the "Back" button to the Education Screen
        self.backToEducationScreen_button.clicked.connect(self.backToEducation)
        # Connect the "Next" button to the Awards Screen
        self.gotoAwardsScreen_button.clicked.connect(self.gotoAwards)
        # Connect "Submit" button to handler
        self.submit_button.clicked.connect(self.submitLine)
        # Connect "Undo" button to handler
        self.undo_button.clicked.connect(self.undoLine)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.title5_label.setText(_translate("Dialog", "Skills"))
        self.gotoAwardsScreen_button.setText(_translate("Dialog", "Next"))
        self.backToEducationScreen_button.setText(_translate("Dialog", "Back"))
        self.inputPreview_label.setText(_translate("Dialog", "Input preview"))
        self.submit_button.setText(_translate("Dialog", "Submit"))
        self.undo_button.setText(_translate("Dialog", "Undo"))
        self.skill_lineEdit.setPlaceholderText(_translate("Dialog", "Ex: Teamwork / Programming in C++"))
        self.label11.setText(_translate("Dialog", "Skill"))
        self.label.setText(_translate("Dialog", "Write your skills in the blank space, one by one."))
        self.label_2.setText(_translate("Dialog", "Tip: Write the most relevant skills first. These "))
        self.label_3.setText(_translate("Dialog", "should be relevant to the job position you are"))
        self.label_4.setText(_translate("Dialog", "applying for."))

    def backToEducation(self):
        if len(globalQueue) > 0:
            globalQueue.pop(-1)
        widget.setCurrentIndex(widget.currentIndex() - 1)

    def gotoAwards(self):
        if len(self.listOfSkills) > 0:
            localHtml = "<p>&nbsp;</p><p style=\"text-align: left;\"><strong>SKILLS</strong></p><hr /><ul>"
            for elem in self.listOfSkills:
                localHtml += "<li>" + elem + "</li>"
            localHtml += "</ul>"

            globalQueue.append(localHtml)

        widget.setCurrentIndex(widget.currentIndex() + 1)

    def submitLine(self):
        lineOfInfo = " - " + self.skill_lineEdit.text() + "\n"
        self.localQueue.append(lineOfInfo)
        self.listOfSkills.append(self.skill_lineEdit.text())
        self.displayQueueOnPreview()
        self.skill_lineEdit.setText("")

    def undoLine(self):
        if len(self.localQueue) > 0:
            self.localQueue.pop(-1)
            self.listOfSkills.pop(-1)
        self.displayQueueOnPreview()

    def displayQueueOnPreview(self):
        previewText = ""
        for line in self.localQueue:
            previewText += line
        self.previewSkills_label.setText(previewText)

class Ui_dialog6(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(800, 640)
        self.title6_label = QtWidgets.QLabel(Dialog)
        self.title6_label.setGeometry(QtCore.QRect(240, 20, 341, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.title6_label.setFont(font)
        self.title6_label.setAlignment(QtCore.Qt.AlignCenter)
        self.title6_label.setObjectName("title6_label")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(460, 110, 321, 441))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.previewAwards_label = QtWidgets.QLabel(self.frame)
        self.previewAwards_label.setGeometry(QtCore.QRect(10, 0, 301, 431))
        self.previewAwards_label.setFont(QFont('Ubuntu', 8))
        self.previewAwards_label.setText("")
        self.previewAwards_label.setWordWrap(True)
        self.previewAwards_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.previewAwards_label.setObjectName("previewAwards_label")
        font.setBold(False)
        font.setPointSize(12)
        self.gotoPublicationsScreen_button = QtWidgets.QPushButton(Dialog)
        self.gotoPublicationsScreen_button.setGeometry(QtCore.QRect(600, 570, 161, 61))
        self.gotoPublicationsScreen_button.setFont(font)
        self.gotoPublicationsScreen_button.setObjectName("gotoPublicationsScreen_button")
        self.backToSkillsScreen_button = QtWidgets.QPushButton(Dialog)
        self.backToSkillsScreen_button.setGeometry(QtCore.QRect(30, 570, 151, 61))
        self.backToSkillsScreen_button.setFont(font)
        self.backToSkillsScreen_button.setObjectName("backToSkillsScreen_button")
        font.setPointSize(10)
        self.inputPreview_label = QtWidgets.QLabel(Dialog)
        self.inputPreview_label.setGeometry(QtCore.QRect(560, 80, 121, 21))
        self.inputPreview_label.setFont(font)
        self.inputPreview_label.setObjectName("inputPreview_label")
        self.submit_button = QtWidgets.QPushButton(Dialog)
        self.submit_button.setGeometry(QtCore.QRect(340, 400, 101, 30))
        self.submit_button.setFont(font)
        self.submit_button.setObjectName("submit_button")
        self.undo_button = QtWidgets.QPushButton(Dialog)
        self.undo_button.setGeometry(QtCore.QRect(30, 400, 101, 30))
        self.undo_button.setFont(font)
        self.undo_button.setObjectName("undo_button")
        self.when_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.when_lineEdit.setGeometry(QtCore.QRect(30, 220, 411, 29))
        self.when_lineEdit.setFont(font)
        self.when_lineEdit.setText("")
        self.when_lineEdit.setObjectName("when_lineEdit")
        self.label11 = QtWidgets.QLabel(Dialog)
        self.label11.setGeometry(QtCore.QRect(30, 190, 51, 21))
        self.label11.setFont(font)
        self.label11.setObjectName("label11")
        self.label12 = QtWidgets.QLabel(Dialog)
        self.label12.setGeometry(QtCore.QRect(30, 270, 171, 21))
        self.label12.setFont(font)
        self.label12.setObjectName("label12")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 110, 391, 21))
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 140, 381, 21))
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.award_textEdit = QtWidgets.QTextEdit(Dialog)
        self.award_textEdit.setGeometry(QtCore.QRect(30, 300, 411, 85))
        self.award_textEdit.setFont(font)
        self.award_textEdit.setObjectName("award_textEdit")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(40, 490, 321, 21))
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        # Declare the local queue
        self.localQueue = []
        # Declare the list of fields
        self.listOfFields = []

        # Connect the "Back" button to the Skills Screen
        self.backToSkillsScreen_button.clicked.connect(self.backToSkills)
        # Connect the "Next" button to the Publications Screen
        self.gotoPublicationsScreen_button.clicked.connect(self.gotoPublications)
        # Connect "Submit" button to handler
        self.submit_button.clicked.connect(self.submitLine)
        # Connect "Undo" button to handler
        self.undo_button.clicked.connect(self.undoLine)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.title6_label.setText(_translate("Dialog", "Awards & Certifications"))
        self.gotoPublicationsScreen_button.setText(_translate("Dialog", "Next"))
        self.backToSkillsScreen_button.setText(_translate("Dialog", "Back"))
        self.inputPreview_label.setText(_translate("Dialog", "Input preview"))
        self.submit_button.setText(_translate("Dialog", "Submit"))
        self.undo_button.setText(_translate("Dialog", "Undo"))
        self.when_lineEdit.setPlaceholderText(_translate("Dialog", "Ex: August 2015"))
        self.label11.setText(_translate("Dialog", "When"))
        self.label12.setText(_translate("Dialog", "Award/Certification"))
        self.label.setText(_translate("Dialog", "Insert your awards and/or certifications in the "))
        self.label_2.setText(_translate("Dialog", "blank space below, one by one."))
        self.award_textEdit.setPlaceholderText(_translate("Dialog", "Ex: Gold Medal at the International Mathematics Olympiad"))
        self.label_3.setText(_translate("Dialog", "Tip: Write the most relevant ones first."))

    def backToSkills(self):
        if len(globalQueue) > 0:
            globalQueue.pop(-1)
        widget.setCurrentIndex(widget.currentIndex() - 1)

    def gotoPublications(self):
        if len(self.listOfFields) > 0:
            localHtml = "<p>&nbsp;</p><p style=\"text-align: left;\"><strong>AWARDS & CERTIFICATIONS</strong></p><hr /><ul style=\"list-style-type:circle\">"
            for elem in self.listOfFields:
                localHtml += "<li>" + elem[0] + " - " + elem[1] + "</li>"
            localHtml += "</ul>"

            globalQueue.append(localHtml)

        widget.setCurrentIndex(widget.currentIndex() + 1)

    def submitLine(self):
        auxList = []
        lineOfInfo = " ** "
        if len(self.when_lineEdit.text()) > 0:
            lineOfInfo += self.when_lineEdit.text() + " : "
            auxList.append(self.when_lineEdit.text())
        else:
            lineOfInfo += "Unknown timestamp : "
            auxList.append("Unknown timestamp")

        if len(self.award_textEdit.toPlainText()) > 0:
            lineOfInfo += self.award_textEdit.toPlainText() + "\n"
            auxList.append(self.award_textEdit.toPlainText())
        else:
            lineOfInfo += "Unknown award/certification\n"
            auxList.append("Unknown award/certification")

        self.listOfFields.append(auxList)

        self.localQueue.append(lineOfInfo)
        self.displayQueueOnPreview()

        self.award_textEdit.setText("")
        self.when_lineEdit.setText("")

    def undoLine(self):
        if len(self.localQueue) > 0:
            self.localQueue.pop(-1)
            self.listOfFields.pop(-1)
        self.displayQueueOnPreview()

    def displayQueueOnPreview(self):
        previewText = ""
        for line in self.localQueue:
            previewText += line
        self.previewAwards_label.setText(previewText)

class Ui_dialog7(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(800, 640)
        self.title7_label = QtWidgets.QLabel(Dialog)
        self.title7_label.setGeometry(QtCore.QRect(180, 20, 461, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.title7_label.setFont(font)
        self.title7_label.setAlignment(QtCore.Qt.AlignCenter)
        self.title7_label.setObjectName("title7_label")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(460, 110, 321, 441))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.previewPublications_label = QtWidgets.QLabel(self.frame)
        self.previewPublications_label.setGeometry(QtCore.QRect(10, 0, 301, 431))
        self.previewPublications_label.setFont(QFont('Ubuntu', 8))
        self.previewPublications_label.setText("")
        self.previewPublications_label.setWordWrap(True)
        self.previewPublications_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.previewPublications_label.setObjectName("previewPublications_label")
        font.setBold(False)
        font.setPointSize(12)
        self.gotoFinalScreen_button = QtWidgets.QPushButton(Dialog)
        self.gotoFinalScreen_button.setGeometry(QtCore.QRect(600, 570, 161, 61))
        self.gotoFinalScreen_button.setFont(font)
        self.gotoFinalScreen_button.setObjectName("gotoFinalScreen_button")
        self.backToAwardsScreen_button = QtWidgets.QPushButton(Dialog)
        self.backToAwardsScreen_button.setGeometry(QtCore.QRect(30, 570, 151, 61))
        self.backToAwardsScreen_button.setFont(font)
        self.backToAwardsScreen_button.setObjectName("backToAwardsScreen_button")
        font.setPointSize(10)
        self.inputPreview_label = QtWidgets.QLabel(Dialog)
        self.inputPreview_label.setGeometry(QtCore.QRect(560, 80, 121, 21))
        self.inputPreview_label.setFont(font)
        self.inputPreview_label.setObjectName("inputPreview_label")
        self.submit_button = QtWidgets.QPushButton(Dialog)
        self.submit_button.setGeometry(QtCore.QRect(340, 520, 101, 30))
        self.submit_button.setFont(font)
        self.submit_button.setObjectName("submit_button")
        self.undo_button = QtWidgets.QPushButton(Dialog)
        self.undo_button.setGeometry(QtCore.QRect(30, 520, 101, 30))
        self.undo_button.setFont(font)
        self.undo_button.setObjectName("undo_button")
        self.when_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.when_lineEdit.setGeometry(QtCore.QRect(30, 210, 411, 29))
        self.when_lineEdit.setFont(font)
        self.when_lineEdit.setText("")
        self.when_lineEdit.setObjectName("when_lineEdit")
        self.label11 = QtWidgets.QLabel(Dialog)
        self.label11.setGeometry(QtCore.QRect(30, 180, 51, 21))
        self.label11.setFont(font)
        self.label11.setObjectName("label11")
        self.label12 = QtWidgets.QLabel(Dialog)
        self.label12.setGeometry(QtCore.QRect(30, 260, 251, 21))
        self.label12.setFont(font)
        self.label12.setObjectName("label12")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 110, 411, 21))
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 140, 381, 21))
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.publication_textEdit = QtWidgets.QTextEdit(Dialog)
        self.publication_textEdit.setGeometry(QtCore.QRect(30, 290, 411, 85))
        self.publication_textEdit.setFont(font)
        self.publication_textEdit.setObjectName("publication_textEdit")
        self.label12_2 = QtWidgets.QLabel(Dialog)
        self.label12_2.setGeometry(QtCore.QRect(30, 390, 251, 21))
        self.label12_2.setFont(font)
        self.label12_2.setObjectName("label12_2")
        self.link_textEdit = QtWidgets.QTextEdit(Dialog)
        self.link_textEdit.setGeometry(QtCore.QRect(30, 420, 411, 81))
        self.link_textEdit.setFont(font)
        self.link_textEdit.setPlaceholderText("")
        self.link_textEdit.setObjectName("link_textEdit")

        # Declare the local queue
        self.localQueue = []
        # Declare the list of fields
        self.listOfFields = []

        # Connect the "Back" button to the Awards Screen
        self.backToAwardsScreen_button.clicked.connect(self.backToAwards)
        # Connect the "Next" button to the Final Screen
        self.gotoFinalScreen_button.clicked.connect(self.gotoFinal)
        # Connect "Submit" button to handler
        self.submit_button.clicked.connect(self.submitLine)
        # Connect "Undo" button to handler
        self.undo_button.clicked.connect(self.undoLine)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.title7_label.setText(_translate("Dialog", "Publications & Personal Projects"))
        self.gotoFinalScreen_button.setText(_translate("Dialog", "Next"))
        self.backToAwardsScreen_button.setText(_translate("Dialog", "Back"))
        self.inputPreview_label.setText(_translate("Dialog", "Input preview"))
        self.submit_button.setText(_translate("Dialog", "Submit"))
        self.undo_button.setText(_translate("Dialog", "Undo"))
        self.when_lineEdit.setPlaceholderText(_translate("Dialog", "Ex: August 2015"))
        self.label11.setText(_translate("Dialog", "When"))
        self.label12.setText(_translate("Dialog", "Publication / Personal Project"))
        self.label.setText(_translate("Dialog", "Insert your publications and/or personal projects"))
        self.label_2.setText(_translate("Dialog", "in the blank spaces below, one by one."))
        self.publication_textEdit.setPlaceholderText(_translate("Dialog", "Ex: Bomberman Game - created using Java"))
        self.label12_2.setText(_translate("Dialog", "Link (optional)"))

    def backToAwards(self):
        if len(globalQueue) > 0:
            globalQueue.pop(-1)
        widget.setCurrentIndex(widget.currentIndex() - 1)

    def gotoFinal(self):
        if len(self.listOfFields) > 0:
            localHtml = "<p>&nbsp;</p><p style=\"text-align: left;\"><strong>PUBLICATIONS &amp; PERSONAL PROJECTS</strong></p><hr /><dl>"
            for elem in self.listOfFields:
                localHtml += "<dt>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;* <em>" + elem[1] + "</em></dt>"
                if elem[2] != "nolink":
                    localHtml += "<dd><span style=\"color: #800000;\">Link</span>: " + elem[2] + "</dd>"
                localHtml += "<dd style=\"text-align: right;\">- " + elem[0] + "</dd>"
            localHtml += "</dl>"

            globalQueue.append(localHtml)

        widget.setCurrentIndex(widget.currentIndex() + 1)

    def submitLine(self):
        auxList = []
        lineOfInfo = " ** "
        if len(self.when_lineEdit.text()) > 0:
            lineOfInfo += self.when_lineEdit.text() + " : "
            auxList.append(self.when_lineEdit.text())
        else:
            lineOfInfo += "Unknown timestamp : "
            auxList.append("Unknown timestamp")

        if len(self.publication_textEdit.toPlainText()) > 0:
            lineOfInfo += self.publication_textEdit.toPlainText() + "\n"
            auxList.append(self.publication_textEdit.toPlainText())
        else:
            lineOfInfo += "Unknown publication/project\n"
            auxList.append("Unknown publication/project")

        if len(self.link_textEdit.toPlainText()) > 0:
            lineOfInfo += "->" + self.link_textEdit.toPlainText() + "\n"
            auxList.append(self.link_textEdit.toPlainText())
        else:
            auxList.append("nolink")

        self.localQueue.append(lineOfInfo)
        self.displayQueueOnPreview()

        self.listOfFields.append(auxList)

        self.publication_textEdit.setText("")
        self.when_lineEdit.setText("")
        self.link_textEdit.setText("")

    def undoLine(self):
        if len(self.localQueue) > 0:
            self.localQueue.pop(-1)
            self.listOfFields.pop(-1)
        self.displayQueueOnPreview()

    def displayQueueOnPreview(self):
        previewText = ""
        for line in self.localQueue:
            previewText += line
        self.previewPublications_label.setText(previewText)

class Ui_dialog8(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(800, 640)
        self.title8_label = QtWidgets.QLabel(Dialog)
        self.title8_label.setGeometry(QtCore.QRect(180, 20, 461, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.title8_label.setFont(font)
        self.title8_label.setAlignment(QtCore.Qt.AlignCenter)
        self.title8_label.setObjectName("title8_label")
        self.generateCV_button = QtWidgets.QPushButton(Dialog)
        self.generateCV_button.setGeometry(QtCore.QRect(500, 510, 261, 121))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.generateCV_button.setFont(font)
        self.generateCV_button.setObjectName("generateCV_button")
        font.setPointSize(12)
        self.backToPublicationsScreen_button = QtWidgets.QPushButton(Dialog)
        self.backToPublicationsScreen_button.setGeometry(QtCore.QRect(30, 570, 151, 61))
        self.backToPublicationsScreen_button.setFont(font)
        self.backToPublicationsScreen_button.setObjectName("backToPublicationsScreen_button")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 110, 771, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 150, 741, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 370, 751, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(0, 420, 791, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(20, 200, 751, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        # Connect the "Back" button to the Publications Screen
        self.backToPublicationsScreen_button.clicked.connect(self.backToPublications)
        # Connect the "Generate CV" button to handler
        self.generateCV_button.clicked.connect(self.generateCV)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.title8_label.setText(_translate("Dialog", "One more step ..."))
        self.generateCV_button.setText(_translate("Dialog", "Generate CV"))
        self.backToPublicationsScreen_button.setText(_translate("Dialog", "Back"))
        self.label.setText(_translate("Dialog", "That would be all. If you are sure that the information provided is correct, you can"))
        self.label_2.setText(_translate("Dialog", "proceed to getting your CV."))
        self.label_3.setText(_translate("Dialog", "Press the \"Generate CV\" button to receive your document!"))
        self.label_4.setText(_translate("Dialog", "Thank you!"))
        self.label_5.setText(_translate("Dialog", "P.S. : It is alright if you left one or more sections blank."))

    def backToPublications(self):
        if len(globalQueue) > 0:
            globalQueue.pop(-1)
        widget.setCurrentIndex(widget.currentIndex() - 1)

    def generateCV(self):
        widget.setCurrentIndex(widget.currentIndex() + 1)

        textFinalHtml = ""
        for i in globalQueue:
            textFinalHtml += i
        textFinalHtml += "</body></html>"

        location = os.path.expanduser("~/Downloads")

        with open(os.path.join(location, "outputFile.html"), "w") as myFile:
            myFile.write(textFinalHtml)

        doc = QTextDocument()
        html = open(os.path.join(location, "outputFile.html")).read()
        doc.setHtml(html)

        printer = QPrinter()
        printer.setOutputFileName(os.path.join(location, "yourCV.pdf"))
        printer.setOutputFormat(QPrinter.PdfFormat)
        printer.setPageSize(QPrinter.A4)
        printer.setPageMargins(10, 12, 12, 10, QPrinter.Millimeter)

        doc.print_(printer)

        os.remove(os.path.join(location, "outputFile.html"))

class Ui_dialog9(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(800, 640)
        self.title9_label = QtWidgets.QLabel(Dialog)
        self.title9_label.setGeometry(QtCore.QRect(180, 40, 461, 71))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.title9_label.setFont(font)
        self.title9_label.setAlignment(QtCore.Qt.AlignCenter)
        self.title9_label.setObjectName("title9_label")
        self.close_button = QtWidgets.QPushButton(Dialog)
        self.close_button.setGeometry(QtCore.QRect(600, 570, 161, 61))
        # 600, 550, 151, 61
        font = QtGui.QFont()
        font.setPointSize(14)
        self.close_button.setFont(font)
        self.close_button.setObjectName("close_button")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 200, 751, 101))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(0, 260, 791, 81))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")

        # Connect the "Close" button to handler
        self.close_button.clicked.connect(QCoreApplication.instance().quit)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.title9_label.setText(_translate("Dialog", "Thank you!"))
        self.close_button.setText(_translate("Dialog", "Close"))
        self.label_3.setText(_translate("Dialog", "You will find your pdf document in the \"Downloads\" folder."))
        self.label_4.setText(_translate("Dialog", "Its name is \"yourCV.pdf\"."))


##################################################################################


if __name__ == "__main__":
    # Create the application
    app = QApplication(sys.argv)

    # The global queue
    globalQueue = []

    # First screen - Personal Information
    dialog1 = QtWidgets.QDialog()
    persInfo = Ui_dialog1()
    persInfo.setupUi(dialog1)
    # Second screen - Profile
    dialog2 = QtWidgets.QDialog()
    profile = Ui_dialog2()
    profile.setupUi(dialog2)
    # Third screen - Work Experience
    dialog3 = QtWidgets.QDialog()
    workExp = Ui_dialog3()
    workExp.setupUi(dialog3)
    # Fourth screen - Education
    dialog4 = QtWidgets.QDialog()
    education = Ui_dialog4()
    education.setupUi(dialog4)
    # Fifth screen - Skills
    dialog5 = QtWidgets.QDialog()
    skills = Ui_dialog5()
    skills.setupUi(dialog5)
    # Sixth screen - Awards
    dialog6 = QtWidgets.QDialog()
    awards = Ui_dialog6()
    awards.setupUi(dialog6)
    # Seventh screen - Publications
    dialog7 = QtWidgets.QDialog()
    publications = Ui_dialog7()
    publications.setupUi(dialog7)
    # Eighth screen - Final
    dialog8 = QtWidgets.QDialog()
    final = Ui_dialog8()
    final.setupUi(dialog8)
    # Nineth screen - Thank You
    dialog9 = QtWidgets.QDialog()
    thankyou = Ui_dialog9()
    thankyou.setupUi(dialog9)

    # Window stack (all screens will be put in this QStackedWidget() - a list of windows)
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(dialog1)
    widget.addWidget(dialog2)
    widget.addWidget(dialog3)
    widget.addWidget(dialog4)
    widget.addWidget(dialog5)
    widget.addWidget(dialog6)
    widget.addWidget(dialog7)
    widget.addWidget(dialog8)
    widget.addWidget(dialog9)

    widget.setFixedWidth(800)
    widget.setFixedHeight(640)
    widget.show()

    # Execute application
    sys.exit(app.exec_())
