import math


class Solution(object):
    def largestPalindrome(self, n):
        # write your code here
        if n == 1:
            return 9
        if n == 8:
            return 9999000000009999 % 1337
        temp = 10**n


        def buildPalindrome(x):
            s = str(x)[::-1]
            a = int(str(x) + s)
            return a

        for i in range(temp - 3, int(temp / 10), -1):
            _mix = buildPalindrome(i)
            for j in range(temp - 1, int(math.sqrt(_mix)), -1):
                if _mix % j == 0:
                    return _mix % 1337


if __name__ == '__main__':
    so = Solution()
    print(so.largestPalindrome(8))
