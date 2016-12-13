import csv
# write
# with open('file.csv', 'wb') as csvfile:
# 	writer = csv.writer(csvfile)
# 	writer.writerow(["Title", "Description"])
# 	writer.writerow(["row 1", "Some text"])

with open('data.csv', 'wb') as csvfile:
	fieldnames = ["id","name","name"]
	writer = csv.DictWriter(csvfile, fieldnames = ["id", "name", "name"])
	writer.writeheader()
	writer.writerow({"id": 123, "title": "Description"})



# append
# with open("file.csv", "ab") as csvfile:
# 	write = csv.writer(csvfile)
# 	writer.writerow(["Append row", "Some desc"])	

# with open("file.csv", "r") as csvfile:
# #	reader = csv.reader(csvfile)
# 	reader = csv.DictReader(csvfile)
# 	for row in reader:
# 		print(row)
