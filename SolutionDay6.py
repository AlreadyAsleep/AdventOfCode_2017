from math import *
s = input()									#read input
arr = s.split("\t")							#split into a list
arr = [int(i) for i in arr]					#cast to an int list
snapshot = [str(arr)]						#push a snapshot of the list into another list
index = 0		
count = 0
seen_again = ""								#used to store the first repeat we find
seen_again_bool = False
seen_again_count = 0
while(True):
	if arr[index] == max(arr):				#if the current element is the largest
		count += 1
		temp = arr[index]
		arr[index] = 0
		i = index + 1
		while(temp > 0):
			if(i == len(arr)):
				i = 0
			arr[i] += max(1, temp // len(arr))			#how much to redistribute
			temp -= max(1, temp // len(arr))			#remove it from the largest
			i += 1									
		if not (seen_again_bool):
			if str(arr) in snapshot:			#if we've seen this arrangement
				seen_again = str(arr)
				seen_again_bool = True
			else:
				snapshot.append(str(arr))
		else:
			seen_again_count += 1
			if str(arr) == seen_again:			#once we've found a repeat find it again
				break
		index = 0
		continue
	index += 1
	if(index == len(arr)):
		index = 0
print(seen_again_count)