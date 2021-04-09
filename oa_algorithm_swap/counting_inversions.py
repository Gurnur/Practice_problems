"""
Problem: Evaluate the efficiency of a sorting algorithm.
https://aonecode.com/amazon-online-assessment-algorithm-swap

For the input arr of size n, do
    1. Find the smallest pair of indices 0 <= i <= j <= n-1, such that
    arr[i] > arr[j]
    2. If there is no such pair, stop
    3. Otherwise swap arr[i] and arr[j] and repeat finding the next pair.
Write a function to calculate the number of swaps performed by the above algorithm.

Same as: https://www.geeksforgeeks.org/counting-inversions/

Brute force TC: O(n^2):
def getInvCount(arr, n):
	inv_count = 0
	for i in range(n):
		for j in range(i + 1, n):
			if (arr[i] > arr[j]):
				inv_count += 1
	return inv_count

Better approach:
1. Use merge sort to divide and conquer the elements to compare.
2. Every swap count in left and right array is added to count_inversions.
3. When calling merge on left and right array, if there is a swap, add 
len(left_arr - i) to count_inversions. Reasonn being, 
ith element of left arr > jth element of right arr, and since left and 
right arrays are already sorted, all the elements from i to len(left_arry - i)
will need to be swapped in order to bring the jth element in.

TC: O(nlogn)
SC: O(n)
"""
class Sort:
    def mergesort(self, arr):
        count_inversions = 0
        if len(arr) > 1:
            mid = len(arr) // 2
            left = arr[:mid]
            right = arr[mid:]

            count_inversions += self.mergesort(left) 
            count_inversions += self.mergesort(right)
            count_inversions += self.merge(arr, left, right)
        return count_inversions
    
    def merge(self, arr, left, right):
        i, j, k = 0, 0, 0
        count_inversions = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
                k += 1
            else:
                arr[k] = right[j]
                count_inversions += (len(left) - i)
                j += 1
                k += 1
            
        while i < len(left):
            arr[k] = left[i]
            i += 1
        
        while j < len(right):
            arr[k] = right[j]
            j += 1

        return count_inversions

obj = Sort()
arr = [8, 4, 2, 1]
print(obj.mergesort(arr))
arr = [3, 1, 2]
print(obj.mergesort(arr))