#!/usr/bin/env python
# coding: utf-8

# In[8]:


#TASK 2-PRIME NUMBER GENERATOR
def is_prime(num):
    if num<2:
        return False
    #checking for divisors from 2 up to num - 1.
    for i in range(2, num):
        # Check for divisibility: If the remainder is 0, it is NOT prime.
        if num % i==0:
            return False      
    # If the loop finishes without finding any divisors, the number is prime.
    return True
def find_primes_in_range():
    start=-1
    end=-1
    #Input and Validation Loop 
    while True:
        try:
            start=int(input("Enter the START of the range (a positive integer): "))
            if start<1:
                print("Start must be 1 or greater.")
                continue
            end=int(input("Enter the END of the range (a positive integer): "))
            if end<1:
                print("End must be 1 or greater.")
                continue
            if start>end:
                print("Start of the range cannot be greater than the end.")
                continue
            break 
        except ValueError:
            print("Invalid input. Please enter a valid whole number.")

    #Finding all prime numbers within the given range
    prime_numbers=[]
    for number in range(start, end + 1):
        if is_prime(number):
            prime_numbers.append(number)
    
    # Display the primes in a formatted output 
    if not prime_numbers:
        print(f"\nNo prime numbers found between {start} and {end}.")
        return
    print(f"\nPrime Numbers ({len(prime_numbers)})")
    count=0
    formatted_output=""
    for prime in prime_numbers:
        formatted_output +=f"{prime:<10}" 
        count+=1
        if count%10==0 or prime==prime_numbers[-1]:
            print(formatted_output)
            formatted_output = "" 

if __name__=="__main__":
    find_primes_in_range()


# In[ ]:




