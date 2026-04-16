class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        new_hash1 = {}
        new_hash2 = {}
        for i in s:
            if i not in new_hash1:
                new_hash1[i] = 1
            else:
                new_hash1[i] += 1
        
        for j in t:
            if j not in new_hash2:
                new_hash2[j] = 1
            else:
                new_hash2[j] += 1

        if new_hash1 == new_hash2:
            return True
        else:
            return False