##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.



import pandas
import datetime as dt
import os
import random
import smtplib

value = pandas.read_csv("E:/program/working with smtp/automated bday wisher/birthdays.csv")
now_time = dt.datetime.now()

for i in range(len(value)):
    if now_time.month == value["month"][i] and now_time.day == value["day"][i]:
        print(value["name"][i])

        path = "E:/program/working with smtp/automated bday wisher/letter_templates"
        choice = random.choice(os.listdir(path))
        with open(f"E:/program/working with smtp/automated bday wisher/letter_templates/{choice}") as file:
            letter = file.readlines()

            letter[0] = letter[0].replace("[NAME]", value["name"][i])
            str1 = ""
            for j in range(len(letter)):
                str1 += letter[j]

            


            my_email = "sivaop459@gmail.com"
            password = "Guhapriyaa_123"

            with smtplib.SMTP("smtp.gmail.com", port = 587) as connection:
                connection.starttls()
                connection.login(user = my_email, password = password)

                
                connection.sendmail(
                    from_addr = my_email, 
                    to_addrs = f"{value['email'][i]}", 
                    msg = f"Subject:Happy Birthdayy!!!\n\n {str1}."
                )

            



