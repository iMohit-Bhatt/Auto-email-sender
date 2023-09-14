import smtplib

# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
s.starttls()

# Authentication
s.login("mohit.bhatt.work@gmail.com", "gnqulfcourgaibfe")

# message to be sent
message = "Subject: Sale! \n\nThe sale has been started please start doing the shoping fastly!"

# sending the mail
s.sendmail("mohit.bhatt.work@gmail.com", "mohit.bhatt.work@gmail.com", message)

# terminating the session
s.quit()


