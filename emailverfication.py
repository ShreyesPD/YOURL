import smtplib
import random




def email_ver(strng):
    no = str(random.randint(10000, 99999))
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login("kurupwashington@gmail.com", "pwzhrhipfrgmvleh")
    server.sendmail("kurupwashington@gmail.com", strng, no)
    server.quit()

    return no

