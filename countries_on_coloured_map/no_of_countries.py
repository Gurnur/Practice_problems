class Solution:
    def color (self, val, B, A, x, y):
        if x < 0 or x >= len(A):
            return
        if y < 0 or y >= len(A[0]):
            return
        if not B[x][y] :
            return
        if A[x][y] != val:
            return
        B[x][y] = False
        self.color(val, B, A, x + 1, y)
        self.color(val, B, A, x - 1, y)
        self.color(val, B, A, x, y - 1)
        self.color(val, B, A, x, y + 1)

    def countries_count(self, A):
        B = [[True for x in A[0]] for y in A]
        count = 0
        for x in range(0, len(A)):
            for y in range(0, len(A[x])):
                if not B[x][y]:
                    continue;
                count += 1
                self.color(A[x][y], B, A, x, y)
        return count

obj = Solution()
A = [
    [5, 4, 4],
    [4, 3, 4],
    [3, 2, 4],
    [2, 2, 2],
    [3, 3, 4],
    [1, 4, 4],
    [4, 1, 1]
]
print(obj.countries_count(A))
