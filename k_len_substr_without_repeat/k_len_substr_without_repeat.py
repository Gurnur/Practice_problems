'''
LeetCode 1100. Find K-Length Substrings With No Repeated Characters

Given a string S, return the number of substrings of length K with no repeated characters.

Example 1:

Input: S = "havefunonleetcode", K = 5
Output: 6
Explanation: There are 6 substrings they are : 'havef','avefu','vefun','efuno','etcod','tcode'.

Note:
1 <= S.length <= 10^4
All characters of S are lowercase English letters.
1 <= K <= 10^4

'''

class Solution:
    def kLenSubstrNoRepeat(self, s, k):
        l, count = 0, 0
        strs = []
        d = {k: 0 for k in range(26)}

        for r in range(len(s)):
            d[ord(s[r]) - 97] += 1
            while d[ord(s[r]) - 97] > 1:
                d[ord(s[l]) - 97] -= 1
                l += 1
            if r - l + 1 == k:
                strs.append(s[l: r+1])
                d[ord(s[l]) - 97] -= 1
                l += 1
                count += 1
        return count, strs

obj = Solution()
c, res = obj.kLenSubstrNoRepeat("mississippi", 2)
print(c)
print(res)