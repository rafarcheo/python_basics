from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP, SMTPAuthenticationError, SMTPException

host = "smtp.gmail.com"
port = 587
email = "paluki.konto@gmail.com"
password = "tajedyna1"
to_list = ["paluki.konto@gmail.com", "rafal.konto@wp.pl"]


try:
	email_conn = SMTP(host, port)
	email_conn.ehlo()
	email_conn.starttls()
	email_conn.login(email, password)
	the_msg = MIMEMultipart("alternative")
	the_msg['Subject'] = "hello I work"
	the_msg["From"] = email
	#the_msg["To"] = to_list

	plain_text = "Testing message"
	html_text ="""\
	<html>
	<head></head>
		<body>
			<a href="google.pl">Link</a>
		</body>
	</html>
	"""

	part_1 = MIMEText(plain_text, 'plain')
	part_2 = MIMEText(html_text, 'html')

	the_msg.attach(part_1)
	the_msg.attach(part_2)

	#print(the_msg.as_string())

	email_conn.login(email, password)
	email_conn.sendmail(email, to_list, the_msg.as_string())
except SMTPException:
	print("error ocured")	