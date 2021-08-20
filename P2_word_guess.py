import random
name=input("\033[1;33;40m What is your name: ")
print("Good luck!",name)
words_list=['rainbow','computer','python','programing','naved','conditon','ilsa']
#function will chose random word 
word=random.choice(words_list)
print("guess the character")
guess=''
turns=8
while turns>0:
#counts the number of time user fails
    failed=0
    for char in word:
        if char in guess:
            print(char)
        else:
            print("_")
            failed += 1
    if failed==0:
        print("\n \033[1;32;40m you win...")
        print("the word is:",word)
        break
    guesses=input("guess the character:")
    guess +=guesses
    if guesses not in word:
        turns -=1
        print("\033[1;31;40m wrong")
        print("you have",+turns,"guess left")
        if turns==0:
            print("you losoe")    
            print(word)