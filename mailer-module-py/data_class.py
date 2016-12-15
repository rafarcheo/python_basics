import csv
import datetime
import os 
from utils.templates import get_template, render_context
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP, SMTPAuthenticationError, SMTPException

host = "smtp.gmail.com"
port = 587
email = "paluki.konto@gmail.com"
password = "tajedyna1"
to_list = ["paluki.konto@gmail.com", "rafal.konto@wp.pl"]


file_item_path = os.path.join(os.path.dirname(__file__), "data.csv")

class UserManager():

	def render_message(self, user_data):
		file_ = 'templates/message_text.txt';
		file_html = 'templates/message_text.html';
		template = get_template(file_)
		template_html = get_template(file_html)
		if isinstance(user_data, dict):
			try:	
				context = user_data
				plain_ = render_context(template, context)
				html_ = render_context(template_html, context)
				# return (plain_,html_)
				user_email = user_data.get("email", "paluki1.konto@gmail.com")
				to_list.append(user_email)
				email_conn = SMTP(host, port)
				email_conn.ehlo()
				email_conn.starttls()
				email_conn.login(email, password)
				the_msg = MIMEMultipart("alternative")
				the_msg['Subject'] = "hello I work"
				the_msg["From"] = email
				the_msg["to"] = user_email
				part_1 = MIMEText(plain_, 'plain')
				part_2 = MIMEText(html_, 'html')				
				the_msg.attach(part_1)
				the_msg.attach(part_2)
				email_conn.sendmail(email, to_list, the_msg.as_string())
				email_conn.quit()				
			except SMTPException:
				print("error ocured")	
			return None
		return (None, None)


	def message_user(self, user_id=None, email=None):
		user = self.get_user_data(user_id=user_id, email=email)
		if user:
			plain_, html_ = self.render_message(user)
			print(plain_, html_)

		return None


	def get_user_data(self, user_id=None, email=None):
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
				print("User id {user_id} not found".format(user_id=user_id))		
			if email is not None:
				print("User id {unknown_email} not found".format(unknown_email=unknown_email))	
		return None		