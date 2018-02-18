import smtplib

host = 'smtp.gmail.com'
port = 	587
username = 'testingdake5@gmail.com'
password = 'youcandowhatyouwant'
from_email = username
to_list = ['testingdake5@gmail.com']

email_conn = smtplib.SMTP(host,port)
email_conn.ehlo()
#security measure
email_conn.starttls()
email_conn.login(username,password)
"""just to test connection
if(email_conn):
	print('you got it')
"""
email_conn.sendmail(from_email,to_list,"testing python email sending")


#another way
from smtplib import SMTP

email_conn2 = SMTP(host,port)
email_conn2.ehlo()
#security measure
email_conn2.starttls()
email_conn2.login(username,password)
"""just to test connection
if(email_conn):
	print('you got it')
"""
email_conn2.sendmail(from_email,to_list,"testing python email sending method 2")

#add this to handle authentication problems as well as other exceptions that may be thrown.
from smtplib import SMTP, SMTPAuthenticationError,SMTPException

email_conn3 = SMTP(host,port)
email_conn3.ehlo()
#security measure
email_conn3.starttls()
#use a try block to catch the exception
try:
	email_conn3.login(username,password)
	email_conn3.sendmail(from_email,to_list,"testing python exception handling")
except SMTPAuthenticationError:
	print("Could Not login")
except:
	print("An Error Occurred")


