class Solution:
    """
    @param s: a string
    @param t: a string
    @return: the letter that was added in t
    """

    def findTheDifference(self, s, t):
        # Write your code here
        count1 = [0] * 26
        count2 = [0] * 26
        for each in s:
            count1[ord(each) - ord('a')] += 1
        for each in t:
            count2[ord(each) - ord('a')] += 1
        for i in range(26):
            if count1[i] != count2[i]:
                return chr(i + ord('a'))


if __name__ == '__main__':
    so = Solution()
    print(so.findTheDifference('abcd', 'abdcd'))
