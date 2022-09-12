from collections import Counter
from time import sleep
from tkinter import filedialog
import os

# This Program was created by zlElo
# Developer: github.com/zlElo

def startCheck():
    file = (filedialog.askopenfilename(initialdir = "/", title = "Wähle eine Datei", filetypes = (("txt files", "*.txt*"), ("all files", "*.*"))))
    if file == '':
            clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
            clearConsole()
            print('Es ist ein Fehler aufgetreten! Error-1')
            sleep(2)
            input('Bitte drücken Sie Enter um das Programm zu beenden und starten Sie es neu...')
            clearConsole()
    with open(file) as f:
        check=Counter(c.strip().lower() for c in f if c.strip())
        for line in check:
            if check[line]>1:
                print(line)
                sleep(1) # If the program doenst found duplicates, jump it to the input and print nothing
    input('Drücken Sie bitte Enter um das Programm zu schließen...')

def ShowStartScreenSearch():
    print("""
    
                            █▀▄ █░█ █▀█ █░░ █ █▀▀ ▄▀█ ▀█▀ █▀▀  █▀▄ █▀▀ ▀█▀ █▀▀ █▀▀ ▀█▀ █▀█ █▀█
                            █▄▀ █▄█ █▀▀ █▄▄ █ █▄▄ █▀█ ░█░ ██▄  █▄▀ ██▄ ░█░ ██▄ █▄▄ ░█░ █▄█ █▀▄
    
    """)