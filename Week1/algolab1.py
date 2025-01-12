def binary_search(needle,haystack):
	low = 0
	high = len(haystack) - 1
	mid = 0

	while low <= high:

		mid = (high + low) // 2
		if haystack[mid] < needle:
			low = mid + 1
		elif haystack[mid] > needle:
			high = mid - 1
		else:
			return mid
	return -1


haystack = [ 2, 3, 4, 10, 40 ]
needle = 10
result = binary_search(needle,haystack)

if result != -1:
	print("Element is present at index", result)
else:
	print("Element is not present in array")
