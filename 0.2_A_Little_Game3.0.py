import random
import re

#This is a Program Notice 
"""------A Little Game------"""
print("\n\n--------------------------------------------------\n")
print("\033[0;31;40m\"U Know the Rules\"\033[0m\n")

print("""\033[0;34;40mThis is a little game !
Please guess a correct number 
from 1-100 to win the game \033[0m
\033[0;31;40mTry if you can!\033[0m

-----power by \033[0;34;40mVir.Proxy\033[0m""")
print("\n--------------------------------------------------")

def isnum():
    numbers = input("\n\n\nPlease input a number ~~~\n\033[0;33;40mThe number is \033[0m")

    def between(Num,Min,Max):
        if Min > Max:
            temp = Max
            Max = Min
            Min =temp
        if Num < Min :
            print("\033[0;31;40m\n\nPlease enter a number bigger than %d\033[0m" % Min)
            return isnum()
        elif Num > Max :
            print("\033[0;31;40m\n\nPlease enter a positive number less than %d\033[0m" % Max)
            return isnum()
        elif Min <= Num <= Max :
            print("\033[0;34;40mThere are %d RIGHT?\nOK That\'s fine\033[0m" % Num)
            

    while numbers.isnumeric() == False:
        if re.search(r'(-)([0-9]){0,255}','%s' % numbers):
            num = int (numbers)
            return between(num,min,max)
        elif numbers.isalpha():
            print("\033[0;31;40mPlease don't input ALPHA! ! !\033[0m")
            return isnum()
        else:
            print("\033[0;31;40mOPS! Something went wrong! :(\nPlease try again\033[0m")
            return isnum()
    else:
        num = int (numbers)
        between(num,min,max)
    


inmax = input("Please enter MAX\n")
max = int(inmax)

min = 0
isnum()