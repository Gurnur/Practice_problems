#!/usr/bin/python3
'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''

from sys import stdin 

def two_sum(nums, target):
    result = {}
    for i, val in enumerate(nums):
        if (target - val) in result:
            return [result[target-val], i]
        else:
            result[val] = i
    return result

input = stdin.readline
print('Input the array: ')
arr = list(map(int, input().split()))
print('Input the target: ')
t = int(input())
print(two_sum(arr, t))

