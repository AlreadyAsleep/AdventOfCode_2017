from math import *
arr = []
currentRow = []
for j in range(16):
	s = input()
	currentRow = s.split('\t')
	currentRow = [int(i) for i in currentRow]
	stop = False
	for i in range(16):
		for k in range(16):
			if(i == k):
				continue
			if ( currentRow[i] % currentRow[k] == 0):
				arr.append(currentRow[i] // currentRow[k])
				stop = True
				break
			elif (currentRow[k] % currentRow[i] == 0):
				arr.append(currentRow[k] // currentRow[i])
				stop = True
				break
		if stop:
			break
	currentRow = []
print(sum(arr))
	
