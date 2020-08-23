'''
Given a strictly ascending array of positive integers, output the Kth number that is missing from it.

For example:

(2, 14, 16, 17) K = 4 output: 5 (explanation: missing numbers are 1,3,4,5,6,.. and find the Kth missing number which is 5 as K = 4)
(8, 9) K = 1 output: 1
(8, 9) K=1000000 output:1000002
Expected runtime O(log N) where N = array length

Logic: Binary search
TC: O(logn)
'''

class Solution:
    def missing_element(self, nums, k):
        n = len(nums)
        l, r = 0, len(nums) - 1

        if nums[n - 1] < n + k: return n + k

        while l <= r:
            mid = l + (r - l) // 2
            # total missing numbers from beginning to mid
            missing = nums[mid] - (mid + 1)
            if missing < k:
                l = mid + 1
            else:
                r = mid - 1
        return l + k

obj = Solution()
arr = [2, 3, 6, 9, 10]
print(obj.missing_element(arr, 2))