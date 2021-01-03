from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *
from main import *
import sys
import json


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.translated_text_field = QLineEdit()
        self.text_from_speech = ''
        self.translated_text = ''
        file = open("languages.json", "r")
        self.data = json.load(file)
        self.languages = list(self.data.values())
        file.close()
        self.init_ui()

    def findLanguage(self, value):
        pos = self.languages.index(value)
        keys = list(self.data.keys())
        return keys[pos]

    def speakInput(self, my_lang, dest_lang):
        lang = self.findLanguage(my_lang)
        dest = self.findLanguage(dest_lang)
        self.text_from_speech = speak(lang)
        self.showTranslate(dest)

    def showTranslate(self, dest_lang):
        self.translated_text = translate(self.text_from_speech, dest_lang)
        self.translated_text_field.setText(self.translated_text)

    def hearTranslation(self):
        speechBack(self.translated_text)

    def init_ui(self):
        my_lang_label = QLabel("My language:")
        my_lang_box = QComboBox()
        dest_lang_label = QLabel("Translate to:")
        dest_lang_box = QComboBox()

        my_lang_box.addItems(self.languages)
        dest_lang_box.addItems(self.languages)

        my_lang_layout = QHBoxLayout()
        my_lang_layout.addWidget(my_lang_label)
        my_lang_layout.addWidget(my_lang_box)

        dest_lang_layout = QHBoxLayout()
        dest_lang_layout.addWidget(dest_lang_label)
        dest_lang_layout.addWidget(dest_lang_box)

        speak_input_btn = QPushButton("Speak")
        speak_input_btn.clicked.connect(lambda: self.speakInput(
                                                str(my_lang_box.currentText()),
                                                str(dest_lang_box.currentText())

                                            ))

        speak_translate_btn = QPushButton("Hear Translation")
        speak_translate_btn.clicked.connect(self.hearTranslation)

        warning_label = QLabel("Hearing translation doesn't support Hebrew")
        warning_label.setFont(QFont('Times', 8))

        vertical = QVBoxLayout()
        vertical.addLayout(my_lang_layout)
        vertical.addLayout(dest_lang_layout)
        vertical.addWidget(speak_input_btn)
        vertical.addWidget(self.translated_text_field)
        vertical.addWidget(speak_translate_btn)
        vertical.addWidget(warning_label)

        self.setLayout(vertical)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
