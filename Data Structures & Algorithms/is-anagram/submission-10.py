class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counter_s = dict()
        counter_t = dict()

        for i, j in zip(s,t):
            if i in counter_s:
                counter_s[i] += 1
            else:
                counter_s[i] = 1
            
            if j in counter_t:
                counter_t[j] += 1
            else:
                counter_t[j] = 1
        
        for k, v in counter_s.items():
            if k not in counter_t or counter_t[k] != v:
                return False
        return True
        

        