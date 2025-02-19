import os.path
import sys
from PyQt5.QtWidgets import * 
from PyQt5 import QtGui
from PyQt5 import QtCore

class FormatSelectedText(QWidget):
    def __init__(self,browser):
        self.browser = browser
        super(FormatSelectedText, self).__init__()
        self.setAttribute(QtCore.Qt.WA_QuitOnClose,False)
        self.resize(400,150)
        self.setWindowTitle("Format Selected Text")
        self.setWindowIcon(QtGui.QIcon(os.path.join("src", "img", "format.png")))
        self.font_options = QComboBox()
        self.font_options.addItems(["Arial","Times New Roman","Comic Sans","Calibri","Ubuntu"])
        self.font_size_box = QSpinBox()
        self.font_size_box.setValue(14)
        self.font_size_box.setFixedWidth(50)
        self.clear_formating_btn = QPushButton("Clear Formating")
        self.clear_highlighting_btn = QPushButton("Clear Hightlighting")
        self.clear_highlighting_btn.clicked.connect(self.clear_highlighting)
        # self.clear_formating_btn.clicked.connect(self.clear_formating)
        

        layout = QGridLayout()
        layout.addWidget(self.clear_formating_btn,0,0)
        layout.addWidget(self.clear_highlighting_btn,0,1)
        layout.addWidget(self.font_options,1,0)
        layout.addWidget(self.font_size_box,1,1)
        self.setLayout(layout)
    
    
    def clear_highlighting(self):
        cursor = self.browser.textCursor()
        if cursor.hasSelection():
            the_format = QtGui.QTextCharFormat()
            the_format.setBackground(QtGui.QBrush(QtGui.QColor("Transparent")))
            the_format.setUnderlineStyle(QtGui.QTextCharFormat.NoUnderline)
            cursor.mergeCharFormat(the_format)

    def clear_formating(self):
        cursor = self.browser.textCursor()
        if cursor.hasSelection():
            the_format = QtGui.QTextCharFormat()
            the_format.setFontPointSize(14)
            the_format.setFontWeight(0)
            the_format.setBackground(QtGui.QBrush(QtGui.QColor("Transparent")))
            cursor.setCharFormat(the_format)

    def change_font_type(self):
        cursor = self.browser.textCursor()
        if cursor.hasSelection():
            font = self.font_options.currentText()
            the_format = QtGui.QTextCharFormat()
            weight = cursor.charFormat().fontWeight()
            the_format.setFont(QtGui.QFont(font))
            the_format.setFontWeight(weight)
            cursor.mergeCharFormat(the_format)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FormatSelectedText()
    window.show()
    sys.exit(app.exec())