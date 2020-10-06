"""
https://leetcode.com/discuss/interview-question/711486/Snap-or-NYC-or-Phone

Given a list of strings and a regex like string return all strings that match

Example:
['world', 'word', 'would', 'wont', 'which', 'hello']

'w3*d': Would return 'world' and 'would' since there are 3 wildcards between w and d

'w2*d': Would return 'word' since there are 2 wildcards between w and d

TC: O(max_word_len*no_of_words)
SC: O(n) for result
"""

class Solution:
    def string_match(self, dic, pattern):
        def regex(word):
            w, p, d = 0, 0, -1
            while w < len(word) and p < len(pattern):
                if word[w].isalpha() and word[w] == pattern[p]:
                    w += 1
                    p += 1
                elif pattern[p].isdigit():
                    d = pattern[p]
                    p += 2
                    w += int(d)
                else:
                    return False
            
            if w >= len(word) and p >= len(pattern):
                return True
            else:
                return False
            
        res = []
        for word in dic:
            if regex(word):
                res.append(word)

        return res 


obj = Solution()
words = ['world', 'word', 'would', 'wont', 'which', 'hello', 'wonderland']
pattern = 'wo2*d'
print(obj.string_match(words, pattern))