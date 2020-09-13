'''
1. A gardener consider aesthetically appealing gardens in which the tops of 
sequential physical trees (eg palm trees) are always sequentially going up and 
down, that is:
[3, 1, 5, 2, 4]
On the other hand, the following configurations would be invalid:
    * [4, 3, 1]   reason: 3rd tree should be higher than the 2nd one
    * [3, 3]      reason: consecutive trees cannot have the same height
Given a sequence of physical trees in a garden, what is the minimum number of physical 
trees which must be cropped/cut in order to achieve the pattern desired by that gardener?

Solution: Since we can only create valleys by cuts, not hills, so we should count 
the existing number of valid valleys at even and odd positions and cut depending on 
the result.

TC: O(n)
SC: O(1)

'''
import math

class Solution:
    def is_even(self, num):
        if num % 2 == 0:
            return True
        return False

    def min_tree_cuts(self, trees):
        even_cnt, odd_cnt = 0, 0
        for i in range(len(trees)):
            if trees[i] < trees[i-1] and trees[i] < trees[i+1]:
                if self.is_even(i+1):
                    even_cnt += 1
                else:
                    odd_cnt += 1
        if not self.is_even(len(trees)):
            even_cnt += 0.5
            odd_cnt -= 0.5
        return math.floor(len(trees) / 2 - max(odd_cnt, even_cnt))

obj = Solution()
trees = [4, 7, 7, 7, 3, 3, 3, 7, 7]
print(obj.min_tree_cuts(trees))