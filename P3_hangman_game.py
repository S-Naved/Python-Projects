#Hangman Game
import random
from collections import Counter
somewords='''apple banana mango watermelon strawberry orange grape pineapple 
apricot lemon coconut cherry papaya berry peach lychee muskmelon '''
somewords=somewords.split(' ')
word=random.choice(somewords)
if __name__ == '__main__':
    print("Guess the word! HINT:word is a name of a fruit, first letter of word is=",word[0],"and last letter of word is=",word[-1])
    for i in word:

        print('_',end=' ')
    print()
    playing = True
    letterGuessed=''
    chance=len(word)+2
    correct=0
    flag=0
    try:
        while(chance != 0) and flag == 0: #flag is updated when word is correctly guessed
            print()
            chance -=1
            try:
                guess=str(input('Enter a character to guessed:'))
            except:
                print('Enter only a character!:')
                continue
            if not guess.isalpha():
                print('Enter only a character:')
                continue
            elif len(guess)>1:
                print('Enter only a one character')
                continue
            elif guess in letterGuessed:
                print('you have already guessed that character')
                continue
            #if letter guessed correctly
            if guess in word:
                k=word.count(guess)
                for _ in range(k):
                    letterGuessed += guess
            for char in word:
                if char in letterGuessed and(Counter(letterGuessed)!=Counter(word)):
                    print(char,end=' ')
                    correct +=1
                elif(Counter(letterGuessed)==Counter(word)):    
                    
                    print('the word is',end=' ')
                    print(word)
                    flag=1
                    print("congratulation")
                    break
                    break
                else:
                    print('_',end=' ')
        if chance<=0 and (Counter(letterGuessed)!=Counter(word)):
            print()
            print("you lost")
            print('the word was {}'.format(word))
    except KeyboardInterrupt:
        print()
        print('good by')
        exit()
                