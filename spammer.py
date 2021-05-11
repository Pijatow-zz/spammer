import time
from colorama import Fore, Back, Style
import pyautogui as pag

from pyfiglet import Figlet
text = Figlet(font='slant').renderText('WELCOME TO THE SPAMMER')
print(text)


class Main:
    def __init__(self):
        print('')
        self.run()

    def gap(self, length):
        '''stop procedure for given amount of time'''
        time.sleep(length)

    def run(self):
        print(Fore.GREEN, '''
              spam clipboard --> 1
              spam text file --> 2
              spam string --> 3
              ''', Style.RESET_ALL)

        ACTION_TYPE = input('_> ')

        if ACTION_TYPE in ('1', 'clip', 'clipboard'):
            self.clipboard_spam()
        elif ACTION_TYPE in ('2', 'text', 'file'):
            self.file_spam()
        elif ACTION_TYPE in ('3', 'string'):
            self.string_spam()
        else:
            print(Fore.RED, 'INVALID INPUT. TRY AGAIN', Style.RESET_ALL)
            self.run()

    def clipboard_spam(self):
        print('How many times do you want to spam???')
        spam_count = int(input('___> '))

        print('How long do you want me to stop between each spam???(SECONDS)')
        gap_length = int(input('___> '))

        print(Fore.MAGENTA, 'SPAM WILL START IN 5 SECONDS', Style.RESET_ALL)
        self.gap(5)

        print(Fore.YELLOW, Back.BLUE, 'SPAMMING', Style.RESET_ALL)

        for count in range(spam_count):
            pag.hotkey('ctrl', 'v')
            pag.press('enter')
            if count != spam_count:
                self.gap(gap_length)

        print(Fore.BLUE, Back.YELLOW, 'DONE :)', Style.RESET_ALL)

    def file_spam(self):
        print('Enter the file\'s path(default is amigo.txt)')
        file_path = input('___>')
        if file_path == '':
            fhand = open('amigo.txt')
        else:
            fhand = open(file_path)

        print('How long do you want me to stop between each spam???(SECONDS)')
        gap_length = int(input('___> '))

        print(Fore.MAGENTA, 'SPAM WILL START IN 5 SECONDS', Style.RESET_ALL)
        self.gap(5)

        print(Fore.YELLOW, Back.BLUE, 'SPAMMING', Style.RESET_ALL)

        for line in fhand:
            pag.write(line)
            pag.press('enter')
            self.gap(gap_length)

        print(Fore.BLUE, Back.YELLOW, 'DONE :)', Style.RESET_ALL)

    def string_spam(self):
        print('Enter the string')
        string = input('___>')

        print('How many times do you want to spam???')
        spam_count = int(input('___> '))

        print('How long do you want me to stop between each spam ???(SECONDS)')
        gap_length = int(input('___> '))

        print(Fore.MAGENTA, 'SPAM WILL START IN 5 SECONDS', Style.RESET_ALL)
        self.gap(5)

        print(Fore.YELLOW, Back.BLUE, 'SPAMMING', Style.RESET_ALL)

        for count in range(spam_count):
            pag.write(string)
            pag.press('enter')
            if count != spam_count:
                self.gap(gap_length)

        print(Fore.BLUE, Back.YELLOW, 'DONE :)', Style.RESET_ALL)


if __name__ == '__main__':
    Main()
