##################### Normal Starting Project ######################
# pythonanywhere is a way to run your python program in the cloud
from pandas import read_csv
import datetime as dt
import random
import smtplib

MY_EMAIL = "mail@mail.com"
PASSWORD = "something"
today = dt.datetime.now()
today_tuple = (today.month, today.day)

data = read_csv("birthdays.csv")
data_dict = data.to_dict(orient="records")

birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["mail"],
            msg=f"Subject:Happy Birthday\n\n{contents}")
