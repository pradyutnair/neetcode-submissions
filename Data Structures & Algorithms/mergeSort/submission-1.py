# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        n = len(pairs)

        def ms(arr, s, e):
            # If there's less than or eq 1 element
            if e - s + 1 <= 1:
                return arr
            # Mid point
            m = ( e + s ) // 2
            # Run on the first half 
            ms(arr, s, m)
            # Run on the second half
            ms(arr, m+1, e)
            # Merge using arr, start, end and mid index
            merge(arr, s, m , e)
            return arr

        def merge(arr, s , m, e):
            # Use i,j,k pointers to merge: i is for left half, j for right
            i, j = 0, 0 
            # k for in place
            k = s 
            # Split arrays
            L, R = arr[s:m+1], arr[m+1:e+1]

            # Compare and merge at arr[k]
            while i < len(L) and j < len(R):
                if L[i].key <= R[j].key:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1
            # Add all leftovers to arr without comparing (gets sorted at a later merge)
            while i < len(L):
                arr[k] = L[i]
                i+= 1
                k+= 1
            while j < len(R):
                j, k = j+1, k+1
        
        # Initialise indices
        s, e = 0, n
        # Merge sort in place
        ms(pairs, s, e)
        return pairs