from PyQt5 import QtGui
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow,self).__init__()
        self.setWindowTitle('Percentiles Demonstration')
        self.resize(1000, 700)
        self.initUI()
    
    def initUI(self):
        self.center()
        self.centralwidget = QWidget(self)

        # Add Top Name and Label
        self.label1 = QLabel(self)
        self.pixmap1 = QPixmap('Kings Design(rev).png')
        self.label1.setPixmap(self.pixmap1)
        self.label1.resize(self.pixmap1.width(),
                          self.pixmap1.height())
        br = self.frameGeometry()
        self.label1.move(300, 25)

###<-------------------------------------------------------------------------------------------
#QLINE EDIT
        #Input
        self.textbox = QLineEdit(self)
        self.textbox.move(405, 220)
        self.textbox.setAlignment(Qt.AlignCenter)
        self.textbox.setText('100')
        self.textbox.setValidator(QDoubleValidator(-9999999.99, 9999999.99, 2))
        self.textbox.setFont(QFont('Arial',18))
        self.textbox.resize(200, 40)
        self.textbox.textChanged.connect(self.textchanged)

###<-------------------------------------------------------------------------------------------
#QLABELS

        #Add Percentage Label to slider
        self.slider_label = QLabel(self)
        self.percentage = 0
        self.slider_label.setText(str(self.percentage) + '%')
        self.slider_label.move(485, 500)
        self.slider_label.setFont(QtGui.QFont('Arial', 18, QtGui.QFont.Black))

        #Add 'or' label
        self.or_label = QLabel(self)
        self.or_label.setText('or')
        self.or_label.move(485, 545)
        self.or_label.setFont(QtGui.QFont('Calibri', 16))

        #Add Decimal Label to slider
        self.decimal_label = QLabel(self)
        self.decimal = 0.0
        self.decimal_label.setText(str(self.decimal))
        self.decimal_label.move(485, 590)
        self.decimal_label.setFont(QtGui.QFont('Arial', 18, QtGui.QFont.Black))
    #<-------------------------------------------------------------------------------------
        #Add Max Value Label
        self.maxvalue_label = QLabel(self)
        self.maxvalue_label.setText('100%')
        self.maxvalue_label.setFont(QFont('Times', 14))
        self.maxvalue_label.move(730, 360)

        #Add 75% Value Label
        self.value_label75 = QLabel(self)
        self.value_label75.setText('75%')
        self.value_label75.setFont(QFont('Times', 14))
        self.value_label75.move(577, 325)

        #Add 50% Value Label
        self.value_label50 = QLabel(self)
        self.value_label50.setText('50%')
        self.value_label50.setFont(QFont('Times', 14))
        self.value_label50.move(490, 310)

        #Add 25% Value Label
        self.value_label25 = QLabel(self)
        self.value_label25.setText('25%')
        self.value_label25.setFont(QFont('Times', 14))
        self.value_label25.move(403, 325)
    #<---------------------------------------------------------------------------------------
        #Add Current 100%
        self.display100 = QLabel(self)
        self.display100.setText(str(self.textbox.text()))
        self.display100.setFont(QFont('Arial', 20, QFont.Black))
        self.display100.setAlignment(Qt.AlignCenter)
        self.display100.move(700, 415)

        #Add Current 75%
        self.display75 = QLabel(self)
        self.display75.setText(str(float(self.textbox.text())*0.75))
        self.display75.setFont(QFont('Arial', 16, QFont.Black))
        self.display75.setAlignment(Qt.AlignCenter)
        self.display75.move(543, 355)

        #Add Current 50%
        self.display50 = QLabel(self)
        self.display50.setText(str(float(self.textbox.text())*0.50))
        self.display50.setFont(QFont('Arial', 16, QFont.Black))
        self.display50.setAlignment(Qt.AlignCenter)
        self.display50.move(455, 340)

        #Add Current 25%
        self.display25 = QLabel(self)
        self.display25.setText(str(float(self.textbox.text())*0.25))
        self.display25.setFont(QFont('Arial', 16, QFont.Black))
        self.display25.setAlignment(Qt.AlignCenter)
        self.display25.move(367, 355)

    #<---------------------------------------------------------------------------------------

        #Add Top Slider_Cacl Label
        self.slider_calc_label = QLabel(self)
        self.slider_calc_label.setText('Slider Calculations')
        self.slider_calc_label.setFont(QFont('Arial', 16))
        self.slider_calc_label.setAlignment(Qt.AlignCenter)
        self.slider_calc_label.move(60, 74)
        self.slider_calc_label.adjustSize()

        #Add Current 100% for calc
        self.current100_label = QLabel(self)
        self.current100_label.setText(f'Current 100%: {str(self.textbox.text())}')
        self.current100_label.setFont(QFont('Arial', 11))
        self.current100_label.move(60, 115)
        self.current100_label.adjustSize()

        #Add Current Percent for calc
        self.currentpercent_label = QLabel(self)
        self.currentpercent_label.setText('Current Percentage: 0%')
        self.currentpercent_label.setFont(QFont('Arial', 11))
        self.currentpercent_label.move(60, 140)
        self.currentpercent_label.adjustSize()

        #Add Equation for calc
        self.equation_label = QLabel(self)
        self.equation_label.setText(f'Equation: {str(self.textbox.text())} * 0.0')
        self.equation_label.setFont(QFont('Arial', 11))
        self.equation_label.move(60, 165)
        self.equation_label.adjustSize()

        #Create, but not display EQ answer
        self.equation_answer = QLabel(self)
        self.equation_answer.setFont(QFont('Arial',16, QFont.Black))
        self.equation_answer.setAlignment(Qt.AlignCenter)
        self.equation_answer.move(82, 270)

###<-------------------------------------------------------------------------------------------

        #Bottom Percentage Lines 
        for i in range(9):
            self.line = QFrame(self.centralwidget)
            x = (i+1) * 35
            if i == 4:
                self.line.setGeometry(QRect(325 + x, 460, 2, 15))
            else:
                self.line.setGeometry(QRect(325 + x, 460, 2, 10))
            self.line.setLineWidth(5)
            self.line.setMidLineWidth(5)
            self.line.setFrameShape(QFrame.VLine)
        
        #Top Percetage Lines
        for i in range(3):
            self.line = QFrame(self.centralwidget)
            x = int((i+1) * 87.5)
            if i == 1:
                self.line.setGeometry(QRect(325 + x, 385, 2, 15))
            else:
                self.line.setGeometry(QRect(325 + x, 390, 2, 10))
            self.line.setLineWidth(5)
            self.line.setMidLineWidth(5)
            self.line.setFrameShape(QFrame.VLine)
        
        #100% Underline
        self.underline100 = QFrame(self.centralwidget)
        self.underline100.setGeometry(QRect(690, 390, 118, 3))
        self.underline100.setFrameShape(QFrame.HLine)

        #75% Underline
        self.underline75 = QFrame(self.centralwidget)
        self.underline75.setGeometry(QRect(570, 355, 40, 3))
        self.underline75.setFrameShape(QFrame.HLine)

        #50% Underline
        self.underline50 = QFrame(self.centralwidget)
        self.underline50.setGeometry(QRect(482, 340, 40, 3))
        self.underline50.setFrameShape(QFrame.HLine)

        #25% Underline
        self.underline25 = QFrame(self.centralwidget)
        self.underline25.setGeometry(QRect(395, 355, 40, 3))
        self.underline25.setFrameShape(QFrame.HLine)

        #Slider Calculations Underscore Line
        self.sliderline = QFrame(self.centralwidget)
        self.sliderline.setGeometry(QRect(55, 100, 180, 3))
        self.sliderline.setFrameShape(QFrame.HLine)

####<-------------------------------------------------------------------------------------------

        #Slider Time!
        self.slider = QSlider(self.centralwidget)
        self.slider.setGeometry(QRect(315, 400, 360, 60))
        self.slider.setMaximum(100)
        self.slider.setOrientation(Qt.Horizontal)
        self.slider.setTickPosition(QSlider.TicksAbove)
        self.slider.setTickInterval(10)
        self.setCentralWidget(self.centralwidget)
        self.slider.valueChanged.connect(self.valuechange)
        self.slider.setStyleSheet(u"QSlider::groove:horizontal {\n"
        "    background: red;\n"
        "    position: absolute; /* absolutely position 4px from the left and right of the widget. setting margins on the widget should work too... */\n"
        "    left: 4px; right: 4px;\n"
        "}\n"
        "\n"
        "QSlider::handle:horizontal  {\n"
        "    height: 10px;\n"
        "    width:  13px;\n"
        "    background: green;\n"
        "    margin: 0 -4px; /* expand outside the groove */\n"
        "}\n"
        "\n"
        "QSlider::add-page:horizontal  {\n"
        "    background: white;\n"
        "}\n"
        "\n"
        "QSlider::sub-page:horizontal  {\n"
        "    background: green;\n"
        "}")
        
        
#<-------------------------------------------------------------------------------------------
#Button

        self.reveal_button = QPushButton(self)
        self.reveal_button.setText('Click to reveal\nequation answer')
        self.reveal_button.setFont(QFont('Arial', 10))
        self.reveal_button.move(65, 200)
        self.reveal_button.resize(130, 60)
        self.reveal_button.clicked.connect(self.button_clicked)

        self.show()
#<-------------------------------------------------------------------------------------------
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    
    def button_clicked(self):
        try:
            self.equation_answer.setText(str(round(self.decimal * float(self.textbox.text()), 4)))
        except Exception as e:
            self.equation_answer.setText('???')
            print(e)

    def valuechange(self):
        """ Updates Values as soon as slider changes"""

        #Update Values under Slider
        self.percentage = self.slider.value()
        self.decimal = (self.slider.value())/100
        self.slider_label.setText(str(self.percentage) + '%')
        self.decimal_label.setText(str(self.decimal))

        #Update Values Under Calculations
        self.currentpercent_label.setText(f'Current Percentage: {str(self.percentage)}%')
        self.currentpercent_label.adjustSize()

        # Update Equation as Slider Adjusts
        try:
            self.equation_label.setText(f'Equation: {str(self.textbox.text())} * {str(self.decimal)}')
            self.equation_label.adjustSize()
        except:
            self.equation_label.setText(f'Equation: ??? * {str(self.decimal)}')

    def textchanged(self):
        """ Updates Values as Text Box Changes"""

        self.display100.setText(str(self.textbox.text()))
        try:
            #Display dynamic percent values above slider
            self.float_value = float(self.textbox.text())
            self.display75.setText(str(round(self.float_value*0.75, 5)))
            self.display50.setText(str(round(self.float_value*0.50, 5)))
            self.display25.setText(str(round(self.float_value*0.25, 5)))

            #Display dynamic 100% under calculations
            self.current100_label.setText(f'Current 100%: {str(self.textbox.text())}')
            self.current100_label.adjustSize()

            #Update Equation as textbox updates
            self.equation_label.setText(f'Equation: {str(self.textbox.text())} * {str(self.decimal)}')

        except Exception as e:
            self.display100.setText('???')
            self.display75.setText('???')
            self.display50.setText('???')
            self.display25.setText('???')

            self.current100_label.setText('Current 100%: ???')
            self.current100_label.adjustSize()

            self.equation_label.setText(f'Equation: ??? * {str(self.decimal)}')



#<-------------------------------------------------------------------------------------------



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWindow()
    sys.exit(app.exec_())