from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Shirt size")  # set program name
        self.setGeometry(100, 100, 1100, 400)  # set windows size and position
        self.UiComponents()  # call the function uicomponents
        self.show()

    def UiComponents(self):
        # items
        title = QLabel("Shirt Size (cm)", self)
        busttitle = QLabel("bust : measured around the chest possition", self)
        sleevetitle = QLabel("sleeve : measured from the shoulder to the sleeve", self)
        lengthtitle = QLabel(
            "Length : measured from the top of the shoulder to the end of the hip", self
        )
        self.result = QLabel("Result...", self)
        self.bust = QLineEdit(self)
        self.sleeve = QLineEdit(self)
        self.length = QLineEdit(self)

        button = QPushButton("Determind", self)
        button2 = QPushButton("Clear", self)

        # positions and size
        title.setGeometry(275, 0, 200, 30)
        busttitle.setGeometry(200, 25, 200, 30)
        sleevetitle.setGeometry(200, 110, 200, 30)
        lengthtitle.setGeometry(200, 190, 200, 30)
        self.result.setGeometry(250, 350, 200, 30)
        self.bust.setGeometry(200, 75, 200, 30)
        self.sleeve.setGeometry(200, 150, 200, 30)
        self.length.setGeometry(200, 225, 200, 30)
        button.setGeometry(250, 300, 100, 30)

        # functions connect
        button.clicked.connect(self.clickme)
        button2.clicked.connect(self.clear)

        """
        PANTS

        """
        self.ptitle = QLabel("Pants Size (inches)", self)

        self.waist = QLineEdit(self)
        self.hip = QLineEdit(self)
        self.legheight = QLineEdit(self)

        self.waist.setGeometry(700, 75, 200, 30)
        self.hip.setGeometry(700, 150, 200, 30)
        self.legheight.setGeometry(700, 225, 200, 30)

        self.wt = QLabel("waist", self)
        self.ht = QLabel("hip", self)
        self.lht = QLabel("how long your leg is", self)

        self.wt.setGeometry(780, 25, 200, 30)
        self.ht.setGeometry(790, 110, 200, 30)
        self.lht.setGeometry(750, 190, 200, 30)

        self.ptitle.setGeometry(750, 0, 200, 30)

        self.buttonpants = QPushButton("Determind", self)
        self.buttonpants.setGeometry(750, 300, 100, 30)

        self.resultpants = QLabel("Result...", self)
        self.resultpants.setGeometry(750, 350, 200, 30)

        self.buttonpants.clicked.connect(self.clickme2)

    # click function for determining shirt size
    def clickme(self):
        x = int(self.bust.text())  # call value bust
        y = int(self.sleeve.text())  # call value sleeve
        z = int(self.length.text())  # call value length
        # if else statement determining shirt size by adding all the integers and find the corerct size
        if x + y + z >= 205:
            self.result.setText("your shirt size is XXL")
        elif 205 > x + y + y >= 196:
            self.result.setText("your shirt size is XL")
        elif 196 > x + y + z >= 189.5:
            self.result.setText("your shirt size is L")
        elif 189.5 > x + y + z >= 183:
            self.result.setText("your shirt size is M")
        elif 183 > x + y + z:
            self.result.setText("your shirt size is S")

    # clear function
    def clear(self):
        self.result.setText("Result...")  # clearing the line (optional button)
        self.resultpants.setText("Result...")
        self.bust.clear()
        self.sleeve.clear()
        self.length.clear()
        self.waist.clear()
        self.hip.clear()
        self.legheight.clear()

        # click function for determining shirt size

    def clickme2(self):
        x = int(self.waist.text())  # call value bust
        y = int(self.hip.text())  # call value sleeve
        z = int(self.legheight.text())  # call value length
        # if else statement determining shirt size by adding all the integers and find the corerct size
        if x + y + y >= 118.5:
            self.resultpants.setText("your pants size is XL")
        elif 118.5 > x + y + z >= 113:
            self.resultpants.setText("your pants size is L")
        elif 113 > x + y + z >= 108.5:
            self.resultpants.setText("your pants size is M")
        elif 108.5 > x + y + z:
            self.resultpants.setText("your pants size is S")


# dont touch(make the program run)
App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
