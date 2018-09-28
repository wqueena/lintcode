class Solution:
    """
    @param matrix: a lists of integers
    @return: nothing
    """

    def rotate(self, matrix):
        # write your code here
        for i in range(len(matrix)):
            for j in range(i + 1, len(matrix)):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
        for i in range(len(matrix)):
            matrix[i].reverse()
        return matrix


if __name__ == '__main__':
    so = Solution()
    print(so.rotate([[1, 2], [3, 4]]))
