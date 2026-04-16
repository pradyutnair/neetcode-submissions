class Solution:
    def isPalindrome(self, x: int) -> bool:
        # String solution
        number = str(x)

        i, j = 0, len(number)-1
        while i<j:
            if number[i] != number[j]:
                return False
            i += 1
            j -= 1
        return True

