# check if array b is a subset of array a.
'''
Input: a[] = [10, 5, 2, 23, 19], b[] = [19, 5, 3]
Output: false
Explanation: b[] is not a subset of a[]

Input: a[] = [11, 7, 1, 13, 21, 3, 7, 3], b[] = [11, 3, 7, 1, 7]
Output: true
Explanation: b[] is a subset of a[]


Expected Complexities
Time Complexity: O(n + m)
Auxiliary Space: O(n)
'''

def is_subset(a, b):
    # sorted the arrays
    a.sort()
    b.sort()
    
    # pointers for a & b respectively
    i = 0
    j = 0
    
    # length of the 2 arrays
    m = len(a)
    n = len(b)

    while i < m and j < n:
        # a is longer than b so it's easier to look through b every time.
        if a[i] < b[j]:
            i += 1  # move in a to catch up
        elif a[i] == b[j]:
            i += 1
            j += 1  # matched one element from b
        else:
            # a[i] > b[j] → means b[j] is missing
            return False

    return j == n  # all b[] matched

# sample case
a = [11, 1, 13, 21, 3, 7]
b = [11, 3, 7, 1]

if is_subset(a, b):
    print('true')
else:
    print('false')