import csv


def cppy_data(fromFile, toFie, change, id, new_amount,new_sent):
	fileCsv = open(fromFile, "r")
	reader = csv.DictReader(fileCsv)
	writer = open(toFie,"wb")
	writer = csv.writer(writer)

	writer.writerow(["id","name","email","amount","sent","data"])
	for row in reader:
		row_id = row["id"]
		name = row["name"]
		email = row["email"]
		sent = row["sent"]
		amount = row["amount"]
		data = row["data"]
		print(sent);
		if (change):
			if int(row_id) == id:
				sent = new_sent
				amount = new_amount
		writer.writerow([row_id,name,email,amount,sent,data])
	return True

if cppy_data("data.csv", "csv-temp.csv",True,2,12.222,""):
	cppy_data("csv-temp.csv","data.csv",False,2,12.222,"")

#cppy_data("csv-temp.csv", "data.csv")
