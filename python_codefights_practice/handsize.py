def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    # TO DO... <-- Remove this comment when you code this function
    size = 0
    for letter in hand:
        if (hand[letter] > 0):
            size = size + hand[letter]
        print (size)
    return size

print (calculateHandlen({'a': 1, 'b': 1}))