import smtplib 
import datetime as dt
import random

mail = "sudiptop760@gmail.com"
password = "vudaxcjkosnzjuxk"
now = dt.datetime.now()
weekday=now.weekday()

if weekday==weekday:
    with open("/Users/sudipto/Documents/code/projects/100days of code/day 32Email_sending_timeset/quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=mail, password=password)
        connection.sendmail(from_addr=mail, to_addrs="sbusiness869@gmail.com", msg=f"Subject:Monday Motivation\n\n{quote}")