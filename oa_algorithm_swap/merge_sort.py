"""
Merge Sort
"""
class Sort:
    def mergesort(self, arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            left = arr[:mid]
            right = arr[mid:]

            self.mergesort(left) 
            self.mergesort(right)
            return self.merge(arr, left, right)
    
    def merge(self, arr, left, right):
        i, j, k = 0, 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
                k += 1
            else:
                arr[k] = right[j]
                j += 1
                k += 1
            
        while i < len(left):
            arr[k] = left[i]
            i += 1
        
        while j < len(right):
            arr[k] = right[j]
            j += 1

        return arr

obj = Sort()
arr = [3, 5, 1, 2, 7, 0, 4, -1]
print(obj.mergesort(arr))