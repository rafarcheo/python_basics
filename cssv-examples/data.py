import csv
import datetime




def get_length(file_path):
	with open(file_path, "r") as csvfile:
		reader = csv.reader(csvfile)
		reder_list = list(reader)
		return int(len(reder_list))


def append_data(file_path, name, email, amount, sent):
	field_names = ['id','name','email','amount','sent','data']
	next_id = get_length(file_path),
	with open(file_path, "a") as csvfile:
		writer = csv.DictWriter(csvfile, fieldnames=field_names,  lineterminator="\n")
		next_id = next_id[0];
		data = datetime.date.today()

		if next_id == 0:
			next_id = 1
			writer.writeheader()	
		writer.writerow({
			"id": next_id,
			"name": name ,
			"email": email,
			"amount": amount,
			"sent": sent,
			"data": data
			})
		

#append_data("data.csv", "Justinos", "rafal.ja.konto.moje@wp.pl", "123.12","No")


def read_data(user_id=None, email=None):
	file_path = "data.csv"
	with open(file_path, "r") as csvfile:	
		reader = csv.DictReader(csvfile)
		items = []
		for row in reader:
			if user_id is not None:
				if int(user_id) == int(row.get("id")):
					return row 
				else: 
					unknown_id = user_id	
			if email is not None:
				if email == row.get("email"):
					return row
				else: 
					unknown_email = email
		if unknown_id is not None:
			retun "User id {user_id} not found".format(user_id=unknown_id)			
		if unknown_email is not None:
			retun "User id {unknown_email} not found".format(unknown_email=unknown_email)	
	return None		
print(read_data(user_id=1))