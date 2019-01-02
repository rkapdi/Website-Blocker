"""A python script that blocks access to user defined websites that cause procrastination during wokring hours)"""

""Author: Rissalat A. Kapdi
  Date: 01 /01/19"""

import time
from datetime import datetime as dt #datetime class from datetime module

hosts_temp=r'C:\Users\Kapdi\Desktop\Python\Website Blocker\hosts'
hosts_path=r"C:\Windows\System32\drivers\etc\hosts"
redirect="127.0.0.1"
website_list=["www.facebook.com","facebook.com","www.riss.ak.mail.live.com","riss.ak.mail.live.com"]

while True:
    #wokring hour threshold
    if dt(dt.now().year, dt.now().month, dt.now().day, 19) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 22):
        print("Working hours...")
        with open (hosts_temp, 'r+') as file: #open temp hosts file with read and append access
            content=file.read() # content contains entire content of temp hosts
            #iterate through website website_list
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+ " " + website + "\n")
    else:
        with open(hosts_temp, 'r+') as file:
            content=file.readlines()#readlines creates a list with items of the num of lines
            file.seek(0) #place pointer before first character of file content
            for line in content: #iterates through content list
                if not any(website in line for website in website_list): #creates a loop and checks if any element from website_list is not in current line of content list.
                    file.write(line) #if control reaches here then file does not contain element from website_list and therefore write that to the host file
            file.truncate() #deletes content of file from current point and onwards
        print("fun hours...")
    time.sleep(5)#prints  after every 5 seconds
