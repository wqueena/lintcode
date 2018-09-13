class Solution:
    """
    @param str: the origin string
    @return: the start and end of every twitch words
    """

    def twitchWords(self, str):
        # Write your code here
        str = str + ' '
        c = str[0]
        left = 0
        out = []
        for i in range(len(str)):
            if str[i] != c:
                if i - left >= 3:
                    out.append([left, i - 1])
                c = str[i]
                left = i
        return out


if __name__ == '__main__':
    so = Solution()
    print(so.twitchWords("whaaaaattt"))
