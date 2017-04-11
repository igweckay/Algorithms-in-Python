import string
import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

wordlist = loadWords()
def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    alpha = (string.ascii_lowercase)
    alpha_list = list(alpha)#[' '] * len(alpha)
    for letter in range(0, len(lettersGuessed)):
        for letter_in_ascii in range(0,len(alpha_list)):
             if (lettersGuessed[letter] == alpha[letter_in_ascii]):
                alpha_list[letter_in_ascii] = ''
            
    return (''.join(alpha_list))

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    temp=['_'] * len(secretWord)
    letters_used=[]
    for letter in range(0,len(lettersGuessed)):
        if (lettersGuessed[letter] not in letters_used):
            for letter_in_word in range(0, len(secretWord)):
                if (lettersGuessed[letter] == secretWord[letter_in_word]):
                    temp[letter_in_word] = (lettersGuessed[letter])
                    letters_used.append(lettersGuessed[letter])

    return (' '.join(temp))

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    temp=[]
    letters_used=[]
    for letter in range(0,len(lettersGuessed)):
        if (lettersGuessed[letter] not in letters_used):
            for letter_in_word in range(0, len(secretWord)):
                if (lettersGuessed[letter] == secretWord[letter_in_word]):
                    temp.append(lettersGuessed[letter])
                    letters_used.append(lettersGuessed[letter])

    if (len(secretWord) == len(temp)):
        return True
    else:
        return False

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print ('Welcome to the game, Hangman!\nI am thinking of a word that is '+str(len(secretWord))+' letters long.')
    guesses = 8
    lettersGuessed = []
    flag = 0
    while (guesses > 0):
        print ('-------------')
        print ('You have '+str(guesses)+' left.')
        print ('Available letters: '+ (getAvailableLetters(lettersGuessed)))
        letterGuessed = input('Please guess a letter: ')

        if (letterGuessed in lettersGuessed):
            print ("Oops! You've already guessed that letter: " + (getGuessedWord(secretWord, lettersGuessed)))
        elif (letterGuessed in secretWord):
            flag += 1
            lettersGuessed.append(letterGuessed)
            print ('Good guess: ' + (getGuessedWord(secretWord, lettersGuessed)))
        else:
            guesses -= 1
            lettersGuessed.append(letterGuessed)
            print ("Oops! That letter is not in my word: " + getGuessedWord(secretWord, lettersGuessed))
        if (isWordGuessed(secretWord, lettersGuessed)):
            break

    if (isWordGuessed(secretWord, lettersGuessed)):
        print ('-------------')
        print ('Congratulations, you won!')
    else:
        print ('-------------')
        print ('Sorry, you ran out of guesses. The word was ' + secretWord)



hangman(chooseWord(wordlist))