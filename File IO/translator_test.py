from translate import Translator

try:
    with open('apple.txt', 'r') as my_file:
        translation = Translator(to_lang=input('Choose a language: \n1.en\n2.ja\n3.zh\n'))
        print(translation.translate(my_file.read()))
except FileNotFoundError:
    print('Check your file path buddy!')
