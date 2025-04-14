import csv

#atver failu
dati = open("example.csv", "r", encoding="utf-8")

#nolasa datus
csv_dati = csv.reader(dati)

#parveido datus python listā
datu_rindas = list(csv_dati)

print (datu_rindas[100][3])
print(len(datu_rindas))

for rinda in datu_rindas[1:6]:
    print(rinda)

#tikai epasti
'''
visi_epasti = []

for rinda in datu_rindas[1:]:
    visi_epasti.append(rinda[3])
print(visi_epasti)'''

vardi_uzvardi=[]
for rinda in datu_rindas[1:]:
    vardi_uzvardi.append(rinda[1]+" "+rinda[2])
print(vardi_uzvardi)