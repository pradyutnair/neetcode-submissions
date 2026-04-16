from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) <= 1:
            return [strs]
        
        
        char_map = defaultdict(list)
        for word in strs:
            char_idx = [0] * 26
            for char in word:
                index = ord(char) - ord('a')
                char_idx[index] += 1
            key = tuple(char_idx)
            char_map[key].append(word)
        
        return list(char_map.values())


            

        

            
