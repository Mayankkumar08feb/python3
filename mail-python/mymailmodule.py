'''
Sending mail through python
'''
import smtplib
def my_mail_mod(msg_to_send):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login ("nagiosmail3","Nagios@123456789")
    msg = "This is python program!!, sending 2nd msg"
    server.sendmail("nagiosmail3@gmail.com","nagiosmail3@gmail.com", msg)
    server.quit()

