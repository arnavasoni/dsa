class Solution:
    def segregateElements(self, arr):
        # No returning of arr, perform in-place on array.
        n = len(arr)
        neg, pos = [], []

        for i in range(n):
            if arr[i] < 0:
                neg.append(arr[i])
            else:
                pos.append(arr[i])
        
        # positive and negative elements' array made.

        # arrange the numbers from last to first
        j = n-1
        while neg:
            arr[j] = neg.pop() # here you're directly mutating the original list arr
            j -= 1
        
        while pos:
            arr[j] = pos.pop() # here you're directly mutating the original list arr
            j -= 1

sol = Solution()
arr = [1, -1, 3, 2, -7, -5, 11, 6 ]

"""Because the list is being modified in-place,
and the fact that the function doesn't return anything (returns None by default)
changes are happening to the list itself. No need for a variable to call the function.
After the function runs, arr already contains the rearranged elements."""

sol.segregateElements(arr)
print(arr)