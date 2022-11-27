import string
import random

def generate():
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
    #only print s from 0 to 8 (8 being the maximum value of the password)
    return "".join(s[0:8])
print (generate())
