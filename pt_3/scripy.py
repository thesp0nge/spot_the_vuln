import os

filename = input("Inserisci il nome del file da aprire: ")
command = "cat " + filename
os.system(command)
