from math import *
arr = []
currentRow = []
for j in range(16):
	s = input()#read the input
	currentRow = s.split('\t')#convert it to a list
	currentRow = [int(i) for i in currentRow]#cast each element to an int
	print(currentRow)
	arr.append(int(max(currentRow)) - int(min(currentRow)))#add the checksum to a list
	currentRow = []
print(sum(arr))#return the checksum
	
