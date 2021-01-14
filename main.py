import smtplib
from datetime import datetime
import pandas
import random

my_email = "XXXXXXXXX@gmail.com"
my_password = "XXXXXXXXXXXX"

today = datetime.now()
month_day = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")

birthdays_dict = {
	(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
if month_day in birthdays_dict:
	birthday_person = birthdays_dict[month_day]
	letter_number = random.choice(range(1, 4))
	letter_path = f"letter_templates/letter_{letter_number}.txt"
	with open(letter_path) as letter_file:
		contents = letter_file.read()
		contents = contents.replace("[NAME]", birthday_person["name"])

	with smtplib.SMTP("smtp.gmail.com", 587) as connection:
		connection.starttls()
		connection.login(my_email, my_password)
		connection.sendmail(
			from_addr=my_email, 
			to_addrs=birthday_person["email"],
			msg=f"Subject:Happy Birthday!\n\n{contents}")
