import string
import random


def generate(passlen):
    s1= string.ascii_uppercase
    s2=string.ascii_lowercase
    s3= string.digits
    s4=string.punctuation
    s=[]
    #add all the characters into a list
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    #shuffle the entire list
    random.shuffle(s)
    #only print s from 8 ro passlen
    return "".join(s[0:passlen])
passlen = int(input("Please enter password length:"))
print (generate(passlen))
