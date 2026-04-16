class Solution:
    def isValid(self, s: str) -> bool:
        map = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        if len(s) <= 1:
            return False
        
        i, j = 0, len(s)-1
        stack = []
        for index, b in enumerate(s):
            if b in map:
                stack.append(b)
            if b not in map:
                if not stack or b != map[stack.pop()]:
                    return False
        if stack:
            return False
        return True
        
