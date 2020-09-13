'''
Two English words are similar iff they only contain the same alphabetical letters. 
For example, ​food ​and g​ood​ are not similar, but ​dog ​and g​ood ​are similar. 
If A​ ​is similar to ​B​,then all letters in A ​​are contained in ​B,​ and vice versa.
10 < |​L|​ < 500.000 

Solution: Use sets to get unique characters in the word. Beware of duplicate 
words in the list of words.

TC: O(n) n = total chars in the list of words
SC: O(n)
'''
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