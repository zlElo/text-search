from subprocess import call
import os
from time import sleep

# This Program was created by zlELo
# Developer: github.com/zlElo

def showErrorDefs():
    print("""
                                                ┏━━━┓
                                                ┃┏━━┛
                                                ┃┗━━┳━┳━┳━━┳━┳━━┓
                                                ┃┏━━┫┏┫┏┫┏┓┃┏┫━━┫
                                                ┃┗━━┫┃┃┃┃┗┛┃┃┣━━┃
                                                ┗━━━┻┛┗┛┗━━┻┛┗━━┛

------------------------------------------------------------------------------------------------------------------------

Error-1 = Dieser Error bedeutet dass keine .txt Datei ausgewählt wurde, die analyziert werden konnte.
Error-2 = Dieser Error bedeutet dass kein Command eingegeben wurde.
Error-3 = Dieser Error bedeutet dass die geschriebene Textdatei nicht gemäß geschrieben werden konnte.

    """)

    question5 = input('Geben Sie "Start" ein um wieder auf die Programmübersicht zu gelangen oder "Ende" um das Programm zu schließen: ')

    if question5 == 'Ende':
        quit()
    if question5 == 'Start':
        clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
        clearConsole()
        call(['python', 'program.py'])
    if question5 != 'Ende' or 'Start':
        clearConsole()
        print('Es ist ein Fehler aufgetreten! Error-4')
        sleep(2)
        input('Bitte drücken Sie Enter um das Programm zu beenden und starten Sie es neu...')
        clearConsole()