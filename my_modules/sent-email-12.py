import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP, SMTPAuthenticationError, SMTPException

host = "smtp.gmail.com"
port = 587
email = "paluki.konto@gmail.com"
password = "tajedyna1"
to_list = ["paluki.konto@gmail.com", "rafal.konto@wp.pl"]


class MessageUser():
	user_details = []
	messages = []
	email_messages = []
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
				user_email = datail.get("email")
				if user_email:
					user_data = {
						"email": user_email,
						"message": new_msg
					}
					self.email_messages.append(user_data)
				else:
					self.messages.append(new_msg)
			return self.messages
		return []
	def sent_email(self):
		self.make_messages()
		if len(self.email_messages) > 0:
			for detail in self.email_messages:
				user_email = detail['email']
				user_message = detail['message']
				try:
					email_conn = SMTP(host, port)
					email_conn.ehlo()
					email_conn.starttls()
					email_conn.login(email, password)
					the_msg = MIMEMultipart("alternative")
					the_msg['Subject'] = "hello I work 2"
					the_msg["From"] = email
					the_msg["to"] = user_email
					#the_msg["To"] = to_list
					plain_text = "Testing message"
					part_1 = MIMEText(plain_text, 'plain')
					the_msg.attach(part_1)
					#print(the_msg.as_string())
					email_conn.login(email, password)
					email_conn.sendmail(email, [user_email], the_msg.as_string())
				except SMTPException:
					print("error ocured")	
			return True	
		return False	

obj = MessageUser()
obj.add_user("justin", 122.22, email='hello@get.com')
obj.add_user("justin", 172.72, email='paluki.konto@gmail.com')	
obj.add_user("justin", 192.92, email='rafal.konto@wp.pl')			
print(obj.sent_email())