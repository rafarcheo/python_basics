import csv
import shutil
import datetime
from tempfile import NamedTemporaryFile
import os

filename = "data.csv"
temp_file = NamedTemporaryFile(delete=False)

filename_temp = "csv-temp.csv"
dirname, basename = os.path.split(filename_temp)
temp = NamedTemporaryFile(prefix=basename, dir=dirname)
with open(filename, "rb") as csvfile, temp:
	reader = csv.DictReader(csvfile)
	fieldnames = ['id','name','email']
	writer = csv.DictWriter(temp, fieldnames=fieldnames)
	#writer.writeheader()
	print(temp.name)
	for row in reader:
		print(row)
		writer.writerow({
			'id' : row['id'],
			'name' : row['name'],
			'email' : row['email'],
			})
	#shutil.move(temp.name, filename)		





