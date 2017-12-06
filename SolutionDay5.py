#Get Input
arr = []
for i in range(1097):
	arr.append(int(input()))

index = 0#holds the current location
count = 0#holds the amount of steps taken
while (index < len(arr)):#while were still in the maze
	temp = index		
	index += arr[index]
	if(arr[temp] < 3):#comment the if/else for part 1 solution
		arr[temp] += 1
	else:
		arr[temp] -= 1
	count += 1
print(count)

