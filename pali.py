def pali(x):
	if len(x) <= 1:
		return True
	if x[0] == x[-1]:
		return pali(x[1:-1])
	else:
		return False


print (pali('hannah'))
print (pali('cathsgndasas'))



