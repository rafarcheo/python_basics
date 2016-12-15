import csv
import datetime
import os 


# file_item_path = os.path.join(os.getcwd(), "data.csv")
file_item_path = os.path.join(os.path.dirname(__file__), "data.csv")

def read_data(user_id=None, email=None):
	file_path = file_item_path
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
					unknown_email = 'email'
		if user_id is not None:
			return "User id {user_id} not found".format(user_id=user_id)			
		if email is not None:
			return "User id {unknown_email} not found".format(unknown_email=unknown_email)	
	return None		
