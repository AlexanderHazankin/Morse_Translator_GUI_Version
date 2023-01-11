# Morse_Translator_GUI_Version
This is a PyQt5-based GUI application that allows users to translate text between three different languages: English, Morse code, and "bits" (a simple representation of English using 1s and 0s).

## Requirements
Python 3

PyQt5

## Features
Translate text between English, Morse code, and "bits"
GUI interface with dropdown menus to select source and target languages, a text box to enter the text to be translated, and a label to display the translated text
Translation is performed by a function called translate that takes the source language, target language, and text to be translated as arguments and returns the translated text

## Customization
The list of languages and the corresponding translations can be modified by editing the language dictionary in the languages module. The dictionary maps language names to lists of characters, where each character in the list represents a letter or symbol in the language.
To add a new language, create a new list of characters and add it to the language dictionary with a key representing the name of the language. Then, update the source_language_combo_box and target_language_combo_box in the TranslatorWindow class to include the new language as an option.

## Troubleshooting
If you have any issues running the program or have suggestions for improvements, please open an issue or submit a pull request on GitHub.

## Credits
The code created by Alexander Hazankin.

The PyQt5-based GUI implementation and modifications to the original code were done by ChatGPT.

## Contact
For any questions or comments, you can reach me at:

https://www.linkedin.com/in/hazankin

https://github.com/AlexanderHazankin

https://replit.com/@Hazankin

## License
This project is licensed under the [MIT License](LICENSE)

Copyright (c) 2022 Alexander Hazankin

Permission is hereby granted, free of charge
