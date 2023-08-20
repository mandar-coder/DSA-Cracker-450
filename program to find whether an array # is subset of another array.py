# Python 3 program to find whether an array
# is subset of another array

# Return 1 if arr2[] is a subset of
# arr1[]


def isSubset(arr1, arr2, m, n):
	i = 0
	j = 0
	for i in range(n):
		for j in range(m):
			if(arr2[i] == arr1[j]):
				break

		# If the above inner loop was
		# not broken at all then arr2[i]
		# is not present in arr1[]
		if (j == m):
			return 0

	# If we reach here then all
	# elements of arr2[] are present
	# in arr1[]
	return 1


# Driver code
if __name__ == "__main__":
	#input from user
	m = int(input("Enter array1 size:"))
	n = int(input("Enter array2 size:"))
	
	for i in range(0, n):
        arr1 = int(input())
    # adding the element
    arr1.append(ele)
    
	for i in range(0, m):
        arr2 = int(input())
    # adding the element
    arr2.append(ele)   
    
	if(isSubset(arr1, arr2, m, n)):
		print("arr2[] is subset of arr1[] ")
	else:
		print("arr2[] is not a subset of arr1[]")

