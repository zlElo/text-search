from tkinter import filedialog
from time import sleep

# This Program was created by zlELo
# Developer: github.com/zlElo

def sorting(filename):
  infile = open(filename)
  words = []
  for line in infile:
    temp = line.split()
    for i in temp:
      words.append(i)
  infile.close()
  words.sort()
  outfile = open("sortierte-liste.txt", "w")
  for i in words:
    outfile.writelines(i)
    outfile.writelines("\n")
  outfile.close()
  if outfile.write() == False:
    print('Es ist ein Fehler aufgetreten! Error-3')
    sleep(2)
    input('Bitte drücken Sie Enter um das Programm zu beenden und starten Sie es neu...')
  input('Drücken Sie bitte Enter um das Programm zu schließen...')

def searchFile():
    sorting(filedialog.askopenfilename(initialdir = "/", title = "Wähle eine Datei", filetypes = (("txt files", "*.txt*"), ("all files", "*.*"))))

def ShowStartScreenSort():
  print("""

                                          █▀ █▀█ █▀█ ▀█▀ █ █▀▀ █▀█ █▀▀ █▄░█
                                          ▄█ █▄█ █▀▄ ░█░ █ ██▄ █▀▄ ██▄ █░▀█

  """)