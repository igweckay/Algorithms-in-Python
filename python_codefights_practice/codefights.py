#def makeArrayConsecutive2(statues):
#    statues.sort()
#    num = statues[0]
#    setter = []
#    new_set = []
#    for x in range(1,len(statues)):
#        if statues[x] == (num +1):
#           num = statues[x]
#        else:
#            while (num < statues[x]):
#                setter.append(num+1)
#               num += 1
#    for element in setter:
#        if element not in statues:
#            new_set.append(element)
#    return (len(new_set))

#print (makeArrayConsecutive2([6, 2, 3, 8]))

#2368

#def almostIncreasingSequence(sequence):
 #   flag = 0
 #   for num in range(len(sequence)-1):
 #       if sequence[num] > sequence[num+1]:
  #          flag +=1
 #           if flag > 1:
 #               return False
 #   return True
def almostIncreasingSequenceA(sequence):
    update = sequence[0]
    old = []
    flag = 0
    flager = 0
    for num in range(1,len(sequence)):
        if (update < sequence[num]) and (sequence[num] not in old):
            update = sequence[num]
            old.append(sequence[num])
            for num_sec in old:
                if sequence[num] < num_sec:
                    flager +=1
            if flager > 1:
                flag +=1
        else:
            flag +=1/
            
def almostIncreasingSequence(sequence):
    flag = 0
    if len(list(set(sequence))) != len(sequence):
        flag = (flag +1) * (len(sequence) - len(list(set(sequence))))
        print (str(list(set(sequence))) + ' : '+ (str(sequence)))
        print (str(len(sequence)) +" : " +str(len(list(set(sequence)))))
    if list(set(sequence)) == sequence:
        return True
    for num in range(len(sequence)):
        print (str(sorted(sequence[:num-1]+ sequence[num:])) +" : " +str((sequence[:num-1]+ sequence[num:])) +" : " +str(flag))
        if sorted(sequence[:num-1]+ sequence[num:]) == (sequence[:num-1]+ sequence[num:]) and flag <= 1:
            return True
    return False



#print (str(list(set(sequence))) + ' : '+ (str(sequence)))
#print (str(len(sequence)) +" : " +str(len(list(set(sequence)))))
#print (str(sorted(sequence[:num-1]+ sequence[num:])) +" : " +str((sequence[:num-1]+ sequence[num:])) +" : " +str(flag))


#print (almostIncreasingSequence([1, 2, 3, 1]))
#print (almostIncreasingSequence([10, 1, 2, 3, 4, 5]))
#print (almostIncreasingSequence([1, 2, 3, 4, 99, 5, 6]))
#print (almostIncreasingSequence([1, 2, 3, 4, 3, 6]))
#print (almostIncreasingSequence([10, 1, 2, 3, 4, 5, 6, 1]))
#print (almostIncreasingSequence([1, 2, 1, 2]))
#print (almostIncreasingSequence([40, 50, 60, 10, 20, 30]))


def matrixElementsSum(matrix):
    sum_a = 0
    for list in matrix:
        sum_a = sum_a + sum(list)
        print (sum_a)
    return (sum_a)

print (matrixElementsSum([[0,1,1,2], 
 [0,5,0,0], 
 [2,0,3,3]]))