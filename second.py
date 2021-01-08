def determinePrime(number):
	if number < 2:
		return False
	if number == 2:
		return True
	for i in range(2,number):
		if number % i == 0:
			return False
	return True


def checkPrimeDuplicate(d):
	count = 0
	for i in range(0,len(d)):
		for specific in d[i]:
			if determinePrime(specific)==True:
				count = count + 1
	return count

print(checkPrimeDuplicate([[0,1,3],[3,2,4,5,2],[6]]))


def testCheckPrimeDuplicate():
	print("testing checkPrimeDuplicate")
	assert(checkPrimeDuplicate([[2,3,4,5],[6,4,5]])==4)