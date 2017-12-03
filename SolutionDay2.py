from math import *
arr = []
currentRow = []
for j in range(16):
	s = input()
	#print(s)
	currentRow = s.split('\t')
	currentRow = [int(i) for i in currentRow]
	print(currentRow)
	arr.append(int(max(currentRow)) - int(min(currentRow)))
	#print(int(max(currentRow)))
	#print(int(min(currentRow)))
	#print(arr)
	currentRow = []
print(sum(arr))
	
