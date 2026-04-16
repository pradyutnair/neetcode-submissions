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
        # While n exists
        while n > 0:
            # get the last digit (remainder)
            digit = n % 10
            # multiply res * 10 and add the digit
            res = res * 10 + digit
            # reduce n by factor of 10 (quotient)
            n = n // 10
        return res == x


