# PASSWORD GENERATOR

import random

characters = "abcdefghijklmnopqrstuvxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*(')"
password_length = int(input("please enter the length of the password you would like to have: "))
password = " "
    
for x in range(password_length):
    password += random.choice(characters)
        
print("The password you requested for :) :", password)