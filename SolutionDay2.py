from math import *
arr = []
currentRow = []
for j in range(16):
	s = input()
	currentRow = s.split('\t')
	currentRow = [int(i) for i in currentRow]
	print(currentRow)
	arr.append(int(max(currentRow)) - int(min(currentRow)))
	currentRow = []
print(sum(arr))
	
