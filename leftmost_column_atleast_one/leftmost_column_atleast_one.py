'''
Leetcode: A binary matrix means that all elements are 0 or 1. 
For each individual row of the matrix, this row is sorted in 
non-decreasing order. Given a row-sorted binary matrix binaryMatrix, 
return leftmost column index(0-indexed) with at least a 1 in it. 
If such index doesn't exist, return -1.

Logic: Start at bottom right and go left if you see a one and go up if you see a zero. 
If we go out of bounds on the left that means the answer is 0. If we go out of bounds 
on the top the answer is the column we are at+1. Only case left to handle is with no ones.

TC: O(r + c)
SC: O(1)

However, for larger value matrix with most of the right values as 1, 
binary search on columns will be efficient.
'''

class Solution:
    '''O(r + c)'''
    def lowest_left_column(self, binary_matrix):
        if not binary_matrix:
            return -1
        r, c = len(binary_matrix) - 1, len(binary_matrix[0]) - 1
        while r >= 0 and c >= 0:
            if binary_matrix[r][c] == 0:
                r -= 1
            else:
                c -= 1
        if c == len(binary_matrix[0]) - 1:
            return -1
        else:
            return (c + 1)


    def lowest_left_column_binary_search(self, binary_matrix):
        if not binary_matrix:
            return -1
        r, c = len(binary_matrix), len(binary_matrix[0])

        def is_all_column_zero(colm):
            for i in range(r):
                if binary_matrix[i][colm] == 1:
                    return False
            return True

        start, end = 0, c
        while start < end:
            mid = start + (end - start) // 2
            if is_all_column_zero(mid):
                start = mid + 1
            else:
                end = mid
        if start >= c:
            return -1
        else:
            return start

obj = Solution()

matrix = [[0, 0, 0, 1], 
[0, 0, 0, 0],
[0, 1, 1, 1],
[0, 0, 0, 0],
[0, 0, 1, 1]]

print("With O(r + c):", obj.lowest_left_column(matrix))
print("With O(r * log(c)):", obj.lowest_left_column_binary_search(matrix))
