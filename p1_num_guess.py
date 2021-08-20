import math
import random
#taking user input
lower=int(input("Enter lower range:"))
upper=int(input("Enter upper range:"))
#genrating random number
a=random.randint(lower,upper)
# checking the random number -->print(a)
#minimum number guessing formula= log(upper bound - lower bound+1,2)

#colortext-->code[Text Style,Text color,background
print("\n \033[1;33;40m You Have Only",round(math.log(upper - lower+1,2)),"Chance To Guess The Correct Number \n")

#initializing the number of guesses.
count =0
while count<math.log(upper-lower+1,2):
    count +=1
    
    #taking guess number as input
    guess=int(input("\033[1;33;40m Guess a number:"))
    if guess==a:
        print("\n\033[1;32;40m Congratulation!......., You Guess The Correct Number")
        break
    elif a > guess :
        print("\033[1;36;40m You Guess To Small Number...")
    elif a< guess:
        print("\033[1;36;40m You Guess To Big Number")
    print("\n\033[1;31;40m you have ",round(math.log(upper-lower+1,2))-count,"chances left")
if count>math.log(upper-lower+1,2):
    print("\n\033[1;31;40m The Correct Number Is =",a)
    print("\n Better Luck Next Time!")
