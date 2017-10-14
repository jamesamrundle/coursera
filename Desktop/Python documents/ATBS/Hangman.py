#! /usr/bin/python3
import random

words = ['dollar', 'pizza', 'canoe' , 'rifle', 'smack', 'carolina']
print("Hello!, welcome to the hangman game")

print("There is a specific word we have picked out. You have 10 guesses to guess the word completely")

print("Please guess a letter.")

wordPick = random.randint(0, int(len(words)))

gameWord = list(words[wordPick-1])
    #picks word and converts to list
blankWord =['x'] * int(len(gameWord))
    #propagates list for guesses to be inserted into
#print(gameWord)
#print (blankWord)
gameWordx =tuple( gameWord)#creates immutable copy of picked word
#print (gameWordx)
guesscount = 0
guessed = []

while tuple(blankWord) != gameWordx and guesscount <10:
    # blankword assigned tuple or types will never match
    #sglobal gameWordX , gameWord, guesscount, guessed
    
    guess = input()
    
    if guess in guessed:# first see if already guessed
        print('You have already guessed that letter')
        guesscount += 1

    elif guess not in gameWordx:
        print("Sorry there is no " + guess + " In the word.")
        guesscount += 1    

    elif guess not in guessed:
        while guess in gameWord:
            
            
         

           # print(gameWord , "*gameword")
            #print(blankWord , "*blankWord")
            #print (gameWordx, "*gamewordx")
            blankWord[gameWord.index(guess)] = guess
            gameWord[gameWord.index(guess)] = "x"# updates "guessed" word

        guesscount += 1
        print(blankWord)
        print (guesscount, "guesscount")
            ##print("ping guesscount")
    
   

    guessed.append(guess)#updates list of letters guessed

if tuple(blankWord) == gameWordx:# again, assigned tuple or types will never match
    solvedWord = ""         #
    for i in blankWord:     #unnecessary but turns user guessed word into a string
        solvedWord += i      #
    print("Great job! You guessed " + solvedWord +" in " + str(guesscount) + " guesses.")
    

else:
    print("Sorry! You ran out of guesses! The word was " + words[wordPick-1] + ".")
