class Solution:
    def isPalindrome(self, x: int) -> bool:
        # String solution
        # number = str(x)

        # i, j = 0, len(number)-1
        # while i<j:
        #     if number[i] != number[j]:
        #         return False
        #     i += 1
        #     j -= 1
        # return True

        # Number solution
        if x < 0:
            return False
        
        n = x
        res = 0
        while n > 0:
            digit = n % 10
            res = res * 10 + digit
            n = n // 10
        return res == x


