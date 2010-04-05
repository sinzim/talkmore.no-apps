#!/usr/bin/python

from talkmoreapi import *

def main():
    tm = Talkmore()
    login = None
    pwd = None

    creds = get_credentials()

    if creds is None:
        print "You need to enter your login and password"
        login = raw_input("Enter your login: ")
        pwd = raw_input("Enter your password: ")
        save_credentials(login,pwd)
    else:
        login, pwd = creds[0], creds[1]

    tm.login(login,pwd)

    if tm.is_logged_in():
        print "Logged in with user: " + str(tm.user)

    if (raw_input("Do you want your balance (y/n)? ")) == "y":
        print "Balance: " + str(tm.balance) + " NOK"

    if (raw_input("Do you want to send an SMS (y/n)? ")) == "y":
        while 1: # Looping in case the user wants to send SMSs several times
            sendMsg = True # Tell us if we can send the message or not
            theNumbers = raw_input("Please enter the numbers. comma separated: ")
            theMsg = raw_input("Please write your message: ")
            telNbs = theNumbers.split(",") # splits the list of CSV into an array
            print "You are going to send an SMS to", telNbs, "with the message :\n", theMsg
            if (len(theMsg) > 160): # Checkking if the message is longer than one SMS
                print "Your message is",len(theMsg),"chars long which is more than one SMS (",len(theMsg)/160+1,"SMSs to be precise)"
                if (raw_input("Do you really want to send it (y/n)? ")) != "y":
                    print "Not sending the SMS..."
                    sendMsg = False
            if (sendMsg == True):
                print "Sending the SMS(s)..."
                tm.send_sms(telNbs, theMsg)
                print "SMS(s) sent!"
            if (raw_input("One more time (y/n)? ")) == "y":
                continue
            else:
                break


    tm.logout()
    if not tm.is_logged_in():
        print "Logged out"
    else:
        print "Bye now :)"



if __name__ == "__main__":

    main()
