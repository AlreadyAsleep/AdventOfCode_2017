from math import *
arr = []
currentRow = []
for j in range(16):
	s = input()#read the input
	currentRow = s.split('\t')#convert it to a list
	currentRow = [int(i) for i in currentRow]#cast each element to an int
	stop = False
	for i in range(16):
		for k in range(16):
			if(i == k):#b/c n % n always == 0
				continue
			#find the first evenely divisible pair
			if ( currentRow[i] % currentRow[k] == 0):
				arr.append(currentRow[i] // currentRow[k])
				stop = True
				break
			elif (currentRow[k] % currentRow[i] == 0):
				arr.append(currentRow[k] // currentRow[i])
				stop = True
				break
		if stop:#stated only one occurence per line in problem desc.
			break
	currentRow = []
print(sum(arr))#print the sum of all div pairs
	
