# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.mergeSortHelper(pairs, 0, len(pairs) - 1)

    def mergeSortHelper(self,pairs,s,e):
        if e - s + 1 <= 1:
            return pairs

        m = (s + e) // 2
        
        self.mergeSortHelper(pairs, s, m)
        self.mergeSortHelper(pairs,m + 1, e)
        self.merge(pairs, s, m , e)

        return pairs

    def merge(self, arr, s, m, e):
        L = arr[s: m + 1]
        R = arr[m + 1: e + 1]

        i, j ,k  = s,0, 0 

        while j < len(L) and k < len(R):
            if L[j].key <= R[k].key:
                arr[i] = L[j]
                j += 1
            else:
                arr[i] = R[k]
                k += 1
            i += 1

        while j < len(L):
            arr[i] = L[j]
            j += 1
            i += 1
        while k < len(R):
            arr[i] = R[k]
            k += 1
            i += 1