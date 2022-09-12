from list_function import *
from text_search import *
from errors_def import *

# This Program was created by zlELo
# Developer: github.com/zlElo

print("""
                        ██████████████████████████████████████████████████████████████████
                        █─▄─▄─█▄─▄▄─█▄─▀─▄█─▄─▄─█▀▀▀▀▀██─▄▄▄▄█▄─▄▄─██▀▄─██▄─▄▄▀█─▄▄▄─█─█─█
                        ███─████─▄█▀██▀─▀████─██████████▄▄▄▄─██─▄█▀██─▀─███─▄─▄█─███▀█─▄─█
                        ▀▀▄▄▄▀▀▄▄▄▄▄▀▄▄█▄▄▀▀▄▄▄▀▀▀▀▀▀▀▀▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀▄▀▄▀


Dieses Programm ist dafür da, Personen zu helfen, die an Filterlisten und Blocklisten arbeiten! Mit diesem 
Programm können .txt Dateien analysiert werden um beispielsweise alle Einträge einer Filterliste nach 
Alphabet zu sortieren oder bereits notierte Domains zu erkennen und anzuzeigen.

----------------------------------------------------------------------------------------------------------

Diese Funktionen können Sie nutzen:

- Einträge nach Alphabet sortieren und anschließend speichern (Command: sortieren)
- Text nach Duplikaten durchsuchen (Command: search)

Errors:

- Lassen Sie sich die Definitionen der Error Codes ausgeben (Comand: errors)

----------------------------------------------------------------------------------------------------------

""")

question2 = input('Welche Funktion möchten Sie nutzen?: ')

if question2 == 'sortieren':
    clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
    clearConsole()
    ShowStartScreenSort()
    searchFile()
    sorting()

if question2 == 'search':
    clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
    clearConsole()
    ShowStartScreenSearch()
    startCheck()

if question2 == 'errors':
    clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
    clearConsole()
    showErrorDefs()

if question2 == '':
    clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
    clearConsole()
    print('Es ist ein Fehler aufgetreten! Error-1')
    sleep(2)
    input('Bitte drücken Sie Enter um das Programm zu beenden und starten Sie es neu...')