import random

"""------A Little Game------"""
print("\033[0;31;40m\"U Know the Rules\"\033[0m\n")

print("""\033[0;34;40mThis is a little game !
Please guess a correct number 
from 1-100 to win the game \033[0m
\033[0;31;40mTry if you can!\033[0m

-----power by \033[0;34;40mVir.Proxy\033[0m""")


temp = input("\n\n\nPlease Guess a number ~~~\n\033[0;33;40mThe number I guess is \033[0m")
while len(temp) == 0:
    print("\033[0;31;40mOPS! Something went wrong! :(\033[0m ")
    temp = input("\n\033[0;33;40mThe number I guess is \033[0m")
    
guess = int(temp)
times = 3
answer = random.randint(0,100)

while (guess != answer) and (times != 0):
    print("\033[0;31;40m\n\nWrong! Please try again!\033[0m")
    if guess > answer:
        print("The number you guess is \033[0;31;40mbig\033[0m\n")
    else:
        print("The number you guess is \033[0;32;40msmall\033[0m\n")
    if times != 1:
        print("You still have \033[0;37;41m%d\033[0m chances to try\n\n\n" % (times))
    else:
        print("\033[0;31;40mYOU ONLY HAVE ONE CHANCE ! ! !\n\033[0m")
    temp = input("Please try again!\n\033[0;33;40mMaybe is \033[0m")
    while len(temp) == 0:
        print("\033[0;31;40mOPS! Something went wrong! :(\033[0m ")
        temp = input("\n\033[0;33;40mThe number I guess is \033[0m")
    guess = int(temp)
    times -= 1
else:
    if guess == answer:
        print("\033[0;32;40mThat's right!!!\033[0m")
        print("\033[0;32;40mLucky One!\033[0m")  
    else:
        print("The answer is \033[0;34;40m%d\033[0m" % (answer))
        print("Try again next time")
        print("Enjoy it ~~~")