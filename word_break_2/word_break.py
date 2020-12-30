class Solution(object):
    def wordBreak(self, s, wordDict): 
        memo = {} 
        return self.word_search(s, wordDict, memo)

    def word_search(self, s, wordDict, memo):
        if s in memo:
            return memo[s]
        if len(s) == 0:
            return []
        paths = []
        for word in wordDict:
            if not s.startswith(word):
                continue
            if len(word) == len(s):
                paths.append(word)
            else:
                path = self.word_search(s[len(word):], wordDict, memo)
                for p in path:
                    p = word + ' ' + p
                    paths.append(p)
        memo[s] = paths
        return paths

obj = Solution()
s = "catsanddog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
res = obj.wordBreak(s, wordDict)
print(res)