count = 0
for i in range(0, 512):		#size of given input
	s = input()				#read input
	arr = s.split(" ")		#split along the spaces
	count += 1				#add one to note number read
	for j in range(len(arr)):
		temp = arr.pop()	#remove the element
		if temp in arr:		#if it's still in the list its a dupe
			count -= 1		#decrement count b/c we want only unique elements
			break
print(count)
