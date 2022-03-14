'''
Sending mail through python
'''
import smtplib
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login ("nagiosmail3","Nagios@123456789")
msg = "This is python program!!"
server.sendmail("nagiosmail@gmail.com","nagiosmail@gmail.com", msg)
server.quit()
