import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP, SMTPAuthenticationError,SMTPException
import smtplib

#connection details
host = 'smtp.gmail.com'
port =  587
username = 'testingdake5@gmail.com'
password = 'youcandowhatyouwant'
from_email = username
to_list = ['testingdake5@gmail.com']

#MessageUser Class used to email users from a list of them, the list is static for now.
class MessageUser():
    user_details = []
    messages = []
    email_messages = []
    base_message = """Greetings {name}! Thanks for contacting me on {date}. 
I am really happy that you decided to choose us! As a reminder your total of ${total}
is the current amount on your tab. We will begin work as soon as the balance is paid.
DD
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
        detail['date'] = date_text
        if email is not None: # if email != None
            detail["email"] = email
        self.user_details.append(detail)
    def get_details(self):
        return self.user_details
    def make_messages(self):
        if len(self.user_details) > 0:
            for detail in self.get_details():
                name = detail["name"]
                amount = detail["amount"]
                date = detail["date"]
                message = self.base_message
                new_msg = message.format(
                    name=name,
                    date=date,
                    total=amount
                )
                user_email = detail.get("email")
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
    def send_email(self):
        self.make_messages()#format the message 
        if len(self.email_messages) > 0:
            for detail in self.email_messages:#get individual details
                user_email = detail['email']
                user_message = detail['message']
                #run email from pymail2.py
                try:
                    email_conn = SMTP(host,port)
                    email_conn.ehlo()
                    email_conn.starttls()
                    email_conn.login(username,password)
                    the_msg = MIMEMultipart("alternative")
                    the_msg['Subject'] = "Customer Support"
                    the_msg['From'] = from_email
                    the_msg['To'] = user_email
                    part_1 = MIMEText(user_message,'plain')              
                    the_msg.attach(part_1)
                    #test in terminal
                    #print(the_msg.as_string())
                    email_conn.sendmail(from_email,[user_email], the_msg.as_string())
                    email_conn.quit()
                except smtplib.SMTPException:
                    print("Error Sending Message")
            return True
        return False


obj = MessageUser()
obj.add_user("Justin", 123.32, email='testingdake5@gmail.com')
obj.add_user("jOhn", 94.23, email='testingdake5@gmail.com')
obj.add_user("Sean", 93.23, email='testingdake5@gmail.com')
obj.add_user("Emilee", 193.23, email='testingdake5@gmail.com')
obj.add_user("Marie", 13.23, email='testingdake5@gmail.com')
obj.get_details()

obj.send_email()