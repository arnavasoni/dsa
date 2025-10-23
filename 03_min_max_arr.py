class Solution:
    def getMinMax(self, arr):
        min_val = max_val = arr[0]
        for num in arr[1:]:
            if num < min_val:
                min_val = num
            elif num > max_val:
                max_val = num
        
        return [min_val, max_val]
    
arr = [1, 4, 3, -5, -4, 8, 6]
sol = Solution()
print(sol.getMinMax(arr))