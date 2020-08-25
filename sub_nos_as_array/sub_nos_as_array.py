class Solution:
    def subtract(self, n1, n2):
        if not n1 or not n2:
            return 
        i, j, s, carry = len(n1) - 1, len(n2) - 1, 0, 0
        res = []
        ans = []
        while i >= 0 or j >= 0:
            a = 0 if i < 0 else n1[i]
            b = 0 if j < 0 else n2[j]
            s = a - b + carry
            if s < 0:
                carry = -1
                s += 10
            else:
                carry = 0    
            res.append(s)
            i -= 1
            j -= 1

        if carry < 0:
            tmp = self.subtract(n2, n1)
            tmp[0] *= -1
            return tmp

        res = res[::-1]
        for d in res:
            if d == 0:
                continue
            ans.append(d)
        return ans

obj = Solution()
print(obj.subtract([1], [1, 0, 0, 0]))
print(obj.subtract([3, 4, 5], [5, 7, 1]))
print(obj.subtract([1, 0], [1, 0, 0, 0]))
print(obj.subtract([1, 0], [3]))