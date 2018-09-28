class Solution:
    """
    @param nums: a sorted array
    @param a: 
    @param b: 
    @param c: 
    @return: a sorted array
    """

    def sortTransformedArray(self, nums, a, b, c):
        # Write your code here
        result = []
        for x in nums:
            result.append(a * x * x + b * x + c)
        result.sort()
        return result


if __name__ == '__main__':
    so = Solution()
    print(so.sortTransformedArray([-4, -2, 2, 4], 1, 3, 5))
