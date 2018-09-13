class Solution:
    """
    @param n: a integer
    @return: return a string
    """

    def convertToTitle(self, n):
        # write your code here
        out = ''

        while int(n / 27) != 0:
            if n % 26 == 0:
                out = chr(90) + out
                n = int(n / 26 - 1)
            else:
                out = chr(n % 26 + 64) + out
                n = int(n / 26)
        if n <= 26:
            out = chr(n + 64) + out
        print(out)
        return out


if __name__ == '__main__':
    so = Solution()
    so.convertToTitle(27)
    so.convertToTitle(676)
