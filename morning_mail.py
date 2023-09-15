from datetime import datetime
import smtplib
import random

dt = datetime.now()
day_name = dt.strftime('%A')


if day_name == "Thursday":
#---------------------------getting one quote:------------------------

    with open("quotes.txt", "r") as datafile:
        all_quotes = datafile.readlines()
        quote = random.choice(all_quotes)

#----------------------------sending mail------------------------------
    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()

    # Authentication
    s.login("your_email", "your_pass")

    # message to be sent
    message = f"Subject: {day_name} Quote! \n\n{quote}\n\n Thanks you!"

    # sending the mail
    s.sendmail("mohit.bhatt.work@gmail.com", "mohit.bhatt.work@gmail.com", message)

    # terminating the session
    s.quit()

else:
    print(f"Today is not the day to send the email to the users{day_name}")
