class Solution:
    def similar_words(self, word, word_list):
        stack = word_list.split(" ")
        stack_no_dup = set(stack)
        word_set = set(s)
        count = 0
        for word in stack_no_dup:
            if word_set == set(word):
                count += 1
        return count

obj = Solution()
s = "love"
list = "velo low lovee volvell lowly lower lover levo loved love lovee lowe lowes lovey lowan lowa evolve loves volvelle lowed love vole"
print(obj.similar_words(s, list))