
# coding: utf-8

# In[11]:

from datetime import date
name= input("Please enter your name here:--> ")
age= input("Please enter your current age:--> ")
#print("Hii, "+name+" your age is "+age)
if int(age) < 95:
    year= 95 - int(age)
    print("You will be of 95 years in : ")
    print (date.today().year + year)
    
else:
    print("You are already "+ age)

