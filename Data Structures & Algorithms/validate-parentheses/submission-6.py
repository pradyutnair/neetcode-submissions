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
            # If opening bracket
            if b in map:
                stack.append(b)
            if b not in map:
                # If empty stack or last opening bracket != closing bracket
                if not stack or b != map[stack[-1]]:
                    return False
                else:
                    # Remove item from stack
                    stack.pop()
        if stack:
            return False
        return True
        
