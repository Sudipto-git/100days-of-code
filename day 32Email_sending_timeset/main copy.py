##################### Hard Starting Project ######################
import smtplib
from datetime import datetime
import random
import pandas
import os


mail = "sudiptop760@gmail.com"
password = "vudaxcjkosnzjuxk"


today = datetime.now()
today_tuple = (today.month,today.day)

data = pandas.read_csv("/Users/sudipto/Documents/code/projects/100days of code/day 32Email_sending_timeset/birthdays.csv")
birthdays_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}


if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path= f"/Users/sudipto/Documents/code/projects/100days of code/day 32Email_sending_timeset/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])
        
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=mail, password=password)
        connection.sendmail(
            from_addr=mail,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday\n\n{contents}"
        )
        print("Email sent")
        
else:
    print("No birthday today")
    
       



