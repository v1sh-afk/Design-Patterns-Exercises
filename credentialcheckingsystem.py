import re
import random
#program7
#Vishal Prakash
#edit1: 27/11 11:38AM
#edit2: 28/11 21:47PM

print('\t\t\t\tCredential Checking System')
print('\t\t\t\t**************************')
class Credentitals:

    def username(self):
        USERNAME = str(input("ENTER YOUR USERNAME: "))
        x = re.search("[a-zA-Z]", USERNAME)
        y = re.findall("[0-9]", USERNAME)
        if x and y:
            print()
            print("VALID USERNAME")
        else:
            print()
            print("INVALID USERNAME, USERNAME MUST CONTAIN ANY OF THE ALPHABETS AND NUMBERS")
            quit()

    def password(self):
        PASSWORD = input("ENTER YOUR PASSWORD : ")
        x = re.search("[a-zA-Z]", PASSWORD)
        y = re.findall("[0-9]", PASSWORD)
        z = re.findall("[@#!*&^%$]", PASSWORD)
        if x and y and z:
            print()
            print("VALID PASSWORD")
        else:
            print()
            print("INVALID INPUT, PASSWORDS MUST CONTAIN COMBINATION OF ANY ALPHABETS AND NUMBERS SYMBOLS")
            quit()

    def mobile_number(self):
        MOBILE_NUMBER = str(input("ENTER YOUR MOBILE NUMBER : "))
        y = re.findall("\d", MOBILE_NUMBER)
        if y and len(MOBILE_NUMBER) == 10:
            print()
            print("VALID MOBILE NUMBER")
        else:
            print()
            print("INVALID MOBILE NUMBER")
            quit()

    def email_id(self):
        c = r"^\S+@\S+\.\S+$"
        EMAIL_ID = str(input("ENTER YOUR EMAIL ID : "))
        if re.fullmatch(c, EMAIL_ID):
            print()
            print("VALID EMAIL ID")
        else:
            print()
            print("INVALID EMAIL ID")
            quit()

    def captcha(self):
        words = ['heLlO','0xYzf', 'OxyMoron', 'TrEe','ClipT','ZH0nGli']
        CAPTCHA = random.choice(words)
        print(CAPTCHA)
        ENTER_CAPTCHA = input("ENTER THE ABOVE CAPTCHA : ")
        if ENTER_CAPTCHA in words:
            print()
            print("VALID CAPTCHA")
            print()
            print("****************YOU ARE LOGGED IN*****************")
        else:
            print()
            print("INVALID CAPTCHA")


C = Credentitals()
print()
C.username()
print()
C.password()
print()
C.mobile_number()
print()
C.email_id()
print()
C.captcha()


