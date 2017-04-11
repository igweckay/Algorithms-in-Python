import string
#alpha is all of the alphabets, lower cased, in the english alphabet

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



print (getAvailableLetters(['e', 'i', 'k', 'p', 'r', 's']))
