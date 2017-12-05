def test_anagram(str1, str2):
	if(len(str1) != len(str2)):#if the lengths are different
		return False
	if(len(str1) == 0):#if the length is zero for both
		return True
	char_1 = str1.pop()#remove an element from 1
	if char_1 not in str2:#test if it is in the other
		return False
	str2.remove(char_1)
	return test_anagram(str1, str2)#recurr



count = 0
for i in range(512):		#size of given input
	s = input()				#read input
	arr = s.split(" ")		#split along the spaces
	print(arr)
	count += 1				#add one to note number read
	rep = True
	for j in range(len(arr)):
		temp = arr.pop()	#remove the element
		#print(temp)
		if temp in arr:		#if it's still in the list it's a dupe
			rep = False		#decrement count b/c we want only unique elements
		for k in range(len(arr)):
			if test_anagram(list(temp), list(arr[k])):#test for anagram with every other
				rep = False
				break
		if not rep:
			count -= 1
			break

print(count)

