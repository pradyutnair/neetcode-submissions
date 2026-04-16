from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) <= 1:
            return [strs]
        
        # Create a dictionary of lists (values = lists)
        char_map = defaultdict(list)
        for word in strs:
            # For each word create [000...0] 
            char_idx = [0] * 26
            # For each letter of each word
            for char in word:
                # Get the index of the letter in {0, 25}
                index = ord(char) - ord('a')
                # Add it to the unique 26 identifier: eg: [0,1,2..2]
                char_idx[index] += 1
            # Use the identifier as a key
            key = tuple(char_idx)
            # Add the word to value list
            char_map[key].append(word)
        
        # return the list of values which contains the groups of words sharing the same key
        return list(char_map.values())


            

        

            
