class Solution:
    """
    @param s: a string
    @return: return a string
    """

    def removeDuplicateLetters(self, s):
        # write your code here
        out = []
        count = [0] * 26
        for each in s:
            count[ord(each) - ord('a')] += 1
        for each in s:
            count[ord(each) - ord('a')] -= 1
            if each not in out:
                while len(out) > 0 and each < out[-1] and count[ord(out[-1]) -
                                                                ord('a')] != 0:
                    out.pop()
                out.append(each)
        return ''.join(out)


if __name__ == '__main__':
    so = Solution()
    print(so.removeDuplicateLetters('bcabc'))
    print(so.removeDuplicateLetters('cbacdcbc'))
