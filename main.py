from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QTextEdit, QMessageBox
from PyQt5 import uic
import sys
import os



os.environ['QT_AUTO_SCREEN_SCALE_FACTOR'] = '1'

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # Load the ui file
        uic.loadUi("morse-code.ui", self)
        self.setWindowTitle("Morse Code Translator")


        # Define our widgets
        self.text_box = self.findChild(QTextEdit, "textbox")
        self.morse_text_box = self.findChild(QTextEdit, "morsecodebox")


        self.t_button = self.findChild(QPushButton, "Translate")
        self.clear_button = self.findChild(QPushButton, "pushButton")



        self.text_label = self.findChild(QPushButton, "label")
        self.morse_code_label = self.findChild(QPushButton, "morse_code_label")

        #click the buttons
        self.t_button.clicked.connect(self.translate)
        self.clear_button.clicked.connect(self.clear)

        # morse code dictionary
        self.morse_code_dict = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
                                'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
                                'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
                                'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
                                'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
                                'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--',
                                '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
                                '9': '----.', '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.',
                                '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...',
                                ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-',
                                '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.', ' ': '/'
                                }


        # If one would like to creat a Reverse Morse Code Dictionary
        # self.reverse_morse_code_dict = {v: k for k, v in self.morse_code_dict.items()}

        # Show The App
        self.show()



    def clear(self):
        #clear text boxes
        self.text_box.setText("")
        self.morse_text_box.setText("")

    def translate(self):
        #get original language
        text = self.text_box.toPlainText()
        if not text:
            QMessageBox.about(self, "Translator", "Please enter text")
            return
        # if Morse code is entered
        for char in text:
            if char in self.morse_code_dict.values():
                QMessageBox.about(self, "Translator", "Cannot input Morse code in this option.")
                return
        # Convert the text to Morse code
        try:
            morse_text = ''
            for char in text.upper():
                if char in self.morse_code_dict:
                    morse_text += self.morse_code_dict[char] + ' '

        except Exception as e:
            QMessageBox.about(self, "Translator", str(e))

        else:
        #output
            self.morse_text_box.setText(morse_text)




# Initialize The App
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()

