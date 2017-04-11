def tripletSum(x, a):
    a = sorted(a)
    num = 0
    
    while ((a[num] < x) and (num <= (len(a) - 2))):
        temp = num + 1
        for num_2 in range(temp,len(a)):
            if (x-(a[num] + a[num_2]) in a):
                if (x-(a[num] + a[num_2]) != a[num] and (x-(a[num] + a[num_2])) != a[num_2]):
                    return (True)
        num = num + 1
    return (False)

x = 5
a = [2, 3, 1]
print (tripletSum(x,a))

#def sumOfTwo(a,b,v):
#    return any(v-i in set(b) for i in a)


   #                 print (a)
  #                  print (x-(a[num] + a[num_2]))
 #                   print ("anum: " + str(a[num]))
#                    print ("anum2: " + str(a[num_2]))
#a = [1, 4, 3, 6, 10, 1, 0, 1, 6, 5]
#b = [9, 5, 6, 9, 0, 1, 2, 1, 6, 10]
#v = 8
#print (sumOfTwo(a,b,v))

#############
#def sumOfTwo(a, b, v):
#   if (a == []) or (b == []):
#      return (False)
#   a = set(a)
#   b = set(b)
#   for num in a:
#      if num > v:
#         return (False)
#      else:
#         for othr_num in b:
#            if othr_num > v:
#               break
#            else:
#               if (num + othr_num) == v:
#                  return (True)
#   return (False)
###############
