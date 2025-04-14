import csv

dati = open("klases.csv", "r", encoding="utf-8")

csv_dati = csv.reader(dati)

datu_rindas = list(csv_dati)

numurs_burts_sk=[]
for rinda in datu_rindas[1:]:
    numurs_burts_sk.append(rinda[1]+" "+rinda[2]+" "+rinda[5])
print(numurs_burts_sk)