import smtplib

user = "" # Enter your gmail username
pswd = "" # Enter your gmail password

with smtplib.SMTP("smtp.gmail.com") as connection:
	connection.starttls()  # tls stands for Transfer Layer Security. Its a standard procedure.
	connection.login(user = user,password=pswd)
	connection.sendmail(
		from_addr = user  # Here user is the variable which has your username
		to_addr = "" # Enter the mail ID you want to send the mail to
		msg = "Subject: Mic testing 1..2..3 \n\n Hello there thanks for visiting this repository !!!"  # Change the message according to your wish
	)
		
		
