############################################
# Midterm problem functions from Python MIT
# by Kay
############################################
def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    count = -1
    while True:
    	count += 1
    	temp = base ** count
    	if (temp > num):
    		if ((temp - num) < (num - (base**(count - 1)))):
    			return count 
    		else:
    			return (count - 1)

def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''
    sum = 0
    for element in range(len(listA)):
    	sum = sum + (listA[element] * listB[element])

    return sum

def deep_reverse(L):
    """ assumes L is a list of lists whose elements are ints
    Mutates L such that it reverses its elements and also 
    reverses the order of the int elements in every element of L. 
    It does not return anything.
    """
    for element in range(len(L)):
        L[element] = L[element][::-1]
    L.reverse()


def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    tupl = ()
    d1_keys, d2_keys = [], []
    d3 = {}
    d4 = {}
    for i in d1.keys():
        d1_keys.append(i)
    for x in d2.keys():
        d2_keys.append(x)

    for i in d1_keys:
        if ((i not in d2_keys) and (i not in d4.keys())):
            d4[i] = d1[i]
    for x in d2_keys:
        if ((x not in d1_keys) and (x not in d4.keys())):
            d4[x] = d2[x]


    if (len(d1_keys) > len(d2_keys)):
        length = len(d1_keys)
    else:
        length = len(d2_keys)

    for element in d1_keys:
        for other_element in d2_keys:
            if element == other_element:
                if (d1[element] == d2[element]):
                    d3[element] = d1[element]
                else:
                    d3[element] = d1[element] + d2[element]

    tupl = (d3,d4)
    return (tupl)



d1 = {1:30, 2:20, 3:30, 5:80}
d2 = {1:30, 2:50, 3:60, 4:70, 6:90}
dict_interdiff(d1,d2)

def flatten(a_List):
    if isinstance(a_List, list):
        if len(a_List) == 0:
            return []
        first, rest = a_List[0], a_List[1:]
        return flatten(first) + flatten(rest)
    else:
        return [a_List]
  
#L = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
#print (flatten(L))
