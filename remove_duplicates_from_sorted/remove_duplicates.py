'''
Leetcode: Remove Duplicates from Sorted Array

Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:
Given nums = [1,1,2],
Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
It doesn't matter what you leave beyond the returned length.
'''
from sys import stdin

class Solution:
    def removeDuplicates(self, a):
        index = 1
        if len(a)==0:
            return 0
        previous = a[0]
        for i in range(1,len(a)):
            if previous!=a[i]:
                previous = a[i]
                a[index],a[i] = a[i],a[index]
                index+=1
        return index


input = stdin.readline
print('Input the sorted array: ')
arr = list(map(int, input().split()))
obj = Solution()
l = obj.removeDuplicates(arr)
print('Length is: %d' % l)
print(arr)