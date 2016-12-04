from smtplib import SMTP, SMTPAuthenticationError, SMTPException

host = "smtp.gmail.com"
port = 587
email = "paluki.konto@gmail.com"
password = "tajedyna1"
to_list = ["paluki.konto@gmail.com", "rafal.konto@wp.pl"]

email_conn = SMTP(host, port)
email_conn.ehlo()
email_conn.starttls()
try:
	email_conn.login(email, password)
	email_conn.sendmail(email, to_list, "test email")
except SMTPAuthenticationError:
	print("coud not login")	
except: 
	print("an error occured")	
email_conn.quit()