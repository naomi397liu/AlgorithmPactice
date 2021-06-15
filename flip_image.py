class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i, row in enumerate(image):
            row.reverse()
            for j in range(len(row)):
                if row[j] == 0:
                    image[i][j] = 1
                else:
                    image[i][j] = 0
        return image