class Solution:
    """
    @param image: a 2-D array
    @param sr: an integer
    @param sc: an integer
    @param newColor: an integer
    @return: the modified image
    """

    def floodFill(self, image, sr, sc, newColor):
        # Write your code here
        h = len(image)
        w = len(image[0])
        color = image[sr][sc]
        if newColor == color:
            return image

        def dfs(r, c):
            if image[r][c] == color:
                image[r][c] = newColor
                if r > 0:
                    dfs(r - 1, c)
                if r < h - 1:
                    dfs(r + 1, c)
                if c > 0:
                    dfs(r, c - 1)
                if c < w - 1:
                    dfs(r, c + 1)

        dfs(sr, sc)
        return image


if __name__ == '__main__':
    so = Solution()
    print(so.floodFill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2))
