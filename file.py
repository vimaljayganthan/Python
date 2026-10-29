import csv
with open("Automorphic.py","r") as f:
  r=csv.reader(f.read())
  for row in r:
        print(row)