import sys
from PyQt5 import QtWidgets

# Import the languages module
import languages

# Use a dictionary to map language names to languages lists
language = {
    "english": languages.english_alphabet,
    "bits": languages.english_alphabet_bits,
    "morse": languages.international_alphabet_morse
}


def translate(source_language, target_language, text_input):
    """Translate the text from one language to another"""
    # Initialize an empty list to store the translated text
    translated_text = []
    # Iterate through each character in the text to be translated
    for char in text_input:
        # Find the index of the character in the source language
        index = language[source_language].index(char)
        # Append the character in the target language at the same index to the translated text list
        translated_text.append(language[target_language][index])
    return " ".join(translated_text)


class TranslatorWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # Create a combo box to select the source language
        self.source_language_combo_box = QtWidgets.QComboBox(self)
        self.source_language_combo_box.addItems(["English", "Morse", "Bits"])

        # Create a combo box to select the target language
        self.target_language_combo_box = QtWidgets.QComboBox(self)
        self.target_language_combo_box.addItems(["English", "Morse", "Bits"])

        # Create a text edit widget to enter the text to be translated
        self.text_edit = QtWidgets.QTextEdit(self)

        # Create a button to start the translation
        self.translate_button = QtWidgets.QPushButton("Translate", self)
        self.translate_button.clicked.connect(self.on_translate)

        # Create a label to display the translated text
        self.translated_text_label = QtWidgets.QLabel(self)

        self.init_ui()

    def init_ui(self):
        # Create a layout and add the widgets to it
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.source_language_combo_box)
        layout.addWidget(self.target_language_combo_box)
        layout.addWidget(self.text_edit)
        layout.addWidget(self.translate_button)
        layout.addWidget(self.translated_text_label)

    def on_translate(self):
        # Get the selected source and target languages
        source_language = self.source_language_combo_box.currentText().lower()
        target_language = self.target_language_combo_box.currentText().lower()

        # Get the text to translate
        text_to_translate = self.text_edit.toPlainText().lower()

        # Translate the text
        translated_text = translate(source_language, target_language, text_to_translate)

        # Display the translated text
        self.translated_text_label.setText(translated_text)


app = QtWidgets.QApplication(sys.argv)
window = TranslatorWindow()
window.show()
sys.exit(app.exec_())
