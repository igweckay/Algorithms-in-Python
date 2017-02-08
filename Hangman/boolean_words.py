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


def main():
    print (isWordGuessed('broccoli', ['z', 'x', 'q', 'b', 'r', 'o', 'c', 'c', 'o', 'l', 'i']))


main()