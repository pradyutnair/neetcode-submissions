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
                chars = chars[chars.index(i) + 1:]
            chars += i
        total.append(len(chars))
        return max(total)
