import heapq

class Solution:
    def mergeSortedArrays(self, arrays):
        pq = []
        for i, arr in enumerate(arrays):
            pq.append((arr[0], i, 0))
        heapq.heapify(pq)

        res = []
        while pq:
            num, i, j = heapq.heappop(pq)
            res.append(num)
            if j + 1 < len(arrays[i]):
                heapq.heappush(pq, (arrays[i][j + 1], i, j + 1))
        
        return res

obj = Solution()
mat = [[-10, 0, 1], [ 1,  5,  9],[10, 11, 13],[12, 13, 15]]
print(obj.mergeSortedArrays(mat))