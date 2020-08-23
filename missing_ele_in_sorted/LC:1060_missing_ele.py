'''
Given a sorted array A of unique numbers, find the K-th missing number starting from the leftmost number of the array.

Example 1:

Input: A = [4,7,9,10], K = 1
Output: 5
Explanation: The first missing number is 5.

Note:
1 <= A.length <= 50000
1 <= A[i] <= 1e7
1 <= K <= 1e8

Logic: 

If the total_missing_ele < k, then missing number must be after nums[n-1], 
i.e., last number of the array. Otherwise, need to find out the starting index 
to calculate the missing number. Use binary search to have mid as candidate. 

Now total_missing_ele between numd[l] and nums[mid] is nums[mid] - nums[l]-(mid-l).

If this count >= k, then starting index must not fall into (l, r], including r.

Otherwise, starting index fall into right side. But need to update k as k-total_missing_ele.

TC: O(logn). n = len(nums).
SC: O(1).

'''

class Solution:
    def missing_element(self, nums, k):
        n = len(nums)
        total_missing_ele = nums[n - 1] - nums[0] + 1 - n
        if total_missing_ele < k:
            return nums[n - 1] + k - total_missing_ele

        l, r = 0, n - 1
        while l < r -1:
            mid = l + (r - l) // 2
            total_missing_ele = nums[mid] - nums[l] - (mid - l)
            if total_missing_ele >= k:
                r = mid
            else:
                l = mid
                k -= total_missing_ele
        return nums[l] + k

obj = Solution()
arr = [2, 3, 6, 9, 10]
print(obj.missing_element(arr, 2))