# sort an array containing 0, 1 & 2s in ascending order
# to be done without built-in sort functions

class Solution:
    def sort012(self, arr):
        # counters for number of 0s, 1s, 2s
        count0 = count1 = count2 = 0
        
        for num in arr:
            if num == 0:
                count0 += 1
            elif num == 1:
                count1 += 1
            else:
                count2 += 1

        arr[:] = [0] * count0 + [1] * count1 + [2] * count2

        return arr

    
sol = Solution()
print(sol.sort012([0, 1, 2, 0, 1, 2]))
print(sol.sort012([0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]))