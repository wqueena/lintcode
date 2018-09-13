class Solution:
    """
    @param n: a integer
    @return: return a integer
    """

    # def caculate(self, n):
    #     result = 1
    #     for i in range(1, n + 1):
    #         result *= i
    #     return result

    def trailingZeroes(self, n):
        # write your code here
        result = 0
        while n > 0:
            result += n // 5
            n //= 5
        return result


if __name__ == '__main__':
    so = Solution()
    print(so.trailingZeroes(25))
