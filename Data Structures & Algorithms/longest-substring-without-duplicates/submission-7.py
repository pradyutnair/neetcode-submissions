class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s or s == "":
            return 0

        if len(s) == 1:
            return 1

        chars = s[0]
        total = [1]
        for i in s[1:]:
            if i in chars:
                total.append(len(chars))
                # Start the sub sequence from char i
                chars = chars[chars.index(i) + 1:]
            chars += i
        # Ensure we add the current length of chars if we finished the loop
        total.append(len(chars))
        return max(total)
