class Solution:
    def kthSmallest(self, arr, k):
        # sort the array first
        # using bubble sort
        for i in range(len(arr)-1, 0, -1):
            swapped = False
            for j in range(i):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    swapped = True
            
            if not swapped:
                break
        
        return arr[k]

arr = [6, 6, 2]
sol = Solution()
print(sol.kthSmallest(arr, 2)) # k = 3