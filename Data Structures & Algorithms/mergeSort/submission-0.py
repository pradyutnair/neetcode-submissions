# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        n = len(pairs)

        def ms(arr, s, e):
            if e - s + 1 <= 1:
                return arr
            
            m = ( e + s ) // 2
            ms(arr, s, m)
            ms(arr, m+1, e)

            merge(arr, s, m , e)
            return arr
        
        def merge(arr, s , m, e):
            i, j = 0, 0
            k = s
            L, R = arr[s:m+1], arr[m+1:e+1]

            while i < len(L) and j < len(R):
                if L[i].key <= R[j].key:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1
            while i < len(L):
                arr[k] = L[i]
                i+= 1
                k+= 1
            while j < len(R):
                j, k = j+1, k+1
        
        s, e = 0, n
        ms(pairs, s, e)
        return pairs