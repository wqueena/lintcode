class Solution:
    """
    @param str: An array of char
    @param offset: An integer
    @return: nothing
    """

    def rotateString(self, str, offset):
        # write your code here
        if len(str) == 0:
            str = ''
        else:
            for i in range(offset % len(str)):
                temp = str[-1]
                del str[-1]
                str.insert(0, temp)

    #            str.append(temp)
    #            str = str.rstrip(str[-1])
    #            str = temp + str
        return str

