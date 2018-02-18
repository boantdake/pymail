from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP, SMTPAuthenticationError,SMTPException
import smtplib

#connection details
host = 'smtp.gmail.com'
port = 	587
username = 'testingdake5@gmail.com'
password = 'youcandowhatyouwant'
from_email = username
to_list = ['testingdake5@gmail.com']

try:
	email_conn = SMTP(host,port)
	email_conn.ehlo()
	email_conn.starttls()
	email_conn.login(username,password)
	the_msg = MIMEMultipart("alternative")
	the_msg['Subject'] = "Hello Subject"
	the_msg['From'] = from_email
	plain_txt = "testing python exception handling"
	html_txt = """\
	<html>
		<head><head>
		<body>
			<p>HTML Message<br>
				Testing the HTML <b>Messaging from python</b> made by <a href='https://github.com/boantdake' >Bo Dake</a>
			</p>
		</body>
	</html>
	"""
	part_1 = MIMEText(plain_txt,'plain')
	part_2 = MIMEText(html_txt,"html")
	the_msg.attach(part_1)
	the_msg.attach(part_2)
	#test in terminal
	#print(the_msg.as_string())
	email_conn.sendmail(from_email,to_list, the_msg.as_string())
	email_conn.quit()
except smtplib.SMTPException:
	print("Error Sending Message")