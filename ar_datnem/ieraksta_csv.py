import csv

eksport = open("dati_ieraksti.csv", "a", newline="")

csv_rakstitajs = csv.writer(eksport, delimiter=",")

csv_rakstitajs.writerow(["a", "b", "c"])
csv_rakstitajs.writerows([["1", "2", "3"],["4", "5", "6"],["7", "8", "9"]])
eksport.close()