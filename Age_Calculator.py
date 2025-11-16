#!/usr/bin/env python
# coding: utf-8

# In[7]:


birth_date=None 
while birth_date is None:
    date=input("Enter Birth Date(mm/dd/yyyy):")
    try:
        birth_date=datetime.strptime(date,"%m/%d/%Y")
        print("Valid Date")
    except ValueError:
        print("Invalid Date pls try again!")

print(f"Your birth date is:{birth_date}")


# In[16]:


#TASK 1 - AGE CALCULATOR 
#importing datetime library
from datetime import datetime, date
#defing a function that change the user input into format and validationg
def age_calculation():
    birth_date=None 
    while birth_date is None:
        date_user=input("Enter Birth Date(mm/dd/yyyy):")
        try:
            birth_date=datetime.strptime(date_user,"%m/%d/%Y").date()
            print("Valid Date")
        except ValueError:
            print("Invalid Date pls try again!")
    #present day
    today_date=date.today()
    #age calculation
    age=today_date.year-birth_date.year
    # tuple comparison for the date is it not passed yet this year so reducing the 1 year from the age 
    birthday_passed=(today_date.month, today_date.day) < (birth_date.month, birth_date.day)
    if birthday_passed:
        age -=1
    print(f"Current Date: {today_date.strftime('%m/%d/%Y')}")
    print(f"Birth Date:   {birth_date.strftime('%m/%d/%Y')}")
    print(f"Your current age is: {age} years")
    # European format conversion 
    european_format=birth_date.strftime("%d/%m/%Y")
    print(f"Birth Date : {european_format}")

if __name__=="__main__":
    age_calculation()          
    


# In[ ]:




