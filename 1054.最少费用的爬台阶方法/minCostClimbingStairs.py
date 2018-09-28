class Solution:
    """
    @param cost: an array
    @return: minimum cost to reach the top of the floor
    """

    def minCostClimbingStairs(self, cost):
        # Write your code here
        if len(cost) < 2:
            return 0
        if len(cost) == 2:
            return min(cost[0], cost[1])
        dp = [0, 0]
        for i in range(2, len(cost) + 1):
            dp.append(min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2]))
        return dp[-1]


if __name__ == '__main__':
    so = Solution()
    print(so.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))