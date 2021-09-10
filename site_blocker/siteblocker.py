#Import libraries time and datatime
import time
from datetime import datetime as dt

#Path to the host file, redirect to local host, list of websits to block
host_path = "C:/Windows/System32/drivers/etc/hosts"
redirect = "127.0.0.1"
website_list = ["seasonvar.ru","www.facebook.com","www.instagram.com"]

#Condition
while True:
    #Check time
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,16):
        print("You must work")

        # Open and read file
        file = open(host_path, "r+")
        content = file.read()
        for website in website_list:
            if website in content:
                pass
                # Write blocked site and redirect it
            else:
                file.write(redirect + " " + website + "\n")

    else:
        print("Okay, need a little rest")
    
        #Open file and read content line by line
        file = open(host_path,'r+')
        content = file.readlines()
        #Take back pointer to starting of the file from the end of file
        file.seek(0)
        for line in content:
            # If this line hawe not website from our list
            if not any(website in line for website in website_list):
                file.write(line)
            file.truncate()

        
    time.sleep(300)