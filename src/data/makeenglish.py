import sys
import csv

with open('en') as en:
	encsv = csv.reader(en)
	words = []
	for row in encsv:
		words.append(row[0])
		
	print(tuple(words))
	
	with open('out', 'w') as out:
		outcsv = csv.writer(out)
		outcsv.writerow(tuple(words))
		