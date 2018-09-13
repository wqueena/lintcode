class Solution:
    """
    @param arr: the arr
    @return: the sum
    """

    def takeTheElementAndQueryTheSum(self, arr):
        # Write your code here
        _sum = sum(arr)
        _sum1 = 0
        for x in arr:
            _sum1 += x * x
        return ((_sum**2 - _sum1) // 2) % 1000000007


if __name__ == '__main__':
    so = Solution()
    print(so.takeTheElementAndQueryTheSum([1, 2, 3, 4, 5]))
