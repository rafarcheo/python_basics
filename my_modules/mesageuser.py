import datetime

class MessageUser():
	user_details = []
	messages = []
	base_message = """Hi {name}!
	Thank you for the purchase on {date}.
	We hope you are exicted about using it. Jast as abc
	reminder the purcase total was ${total}.
	Have a great one!

	Team 
	"""
	def add_user(self, name, amount, email=None):
		name = name[0].upper() + name[1:].lower()
		amount = "%.2f" %(amount)
		detail = {
			"name": name,
			"amount": amount,
		}
		today = datetime.date.today()
		date_text = '{today.month}/{today.day}/{today.year}'.format(today=today)
		detail["date"] = date_text
		if email is not None:
			detail['email'] = email
		self.user_details.append(detail)
	def get_details(self):
		return self.user_details
	def make_messages(self):
		if len(self.user_details) > 0:
			for datail in self.get_details():
				name = datail["name"]
				amount = datail["amount"]
				date = datail["date"]
				message = self.base_message
				new_msg = message.format(
					name=name,
					date=date,
					total=amount
					)
				self.messages.append(new_msg)
			return self.messages
		return []	

obj = MessageUser()
obj.add_user("justin", 122.22, email='hello@get.com')
obj.add_user("justin", 172.72, email='paluki.konto@gmail.com')	
obj.add_user("justin", 192.92, email='rafal.konto@wp.pl')			
print(obj.get_details())

print(obj.make_messages())