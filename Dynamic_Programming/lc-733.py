from typing import List
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        oldColor = image[sr][sc]
        L = len(image)
        R = len(image[0])
        if (oldColor == newColor):
            return image
        def checkNeighbour(image,dr,dc):
            if (dr>=L or dr < 0 or dc >= R or dc < 0 or image[dr][dc]!=oldColor):
                return
            if (image[dr][dc] == oldColor):
                image[dr][dc] = newColor
                checkNeighbour(image, dr+1, dc)
                checkNeighbour(image, dr-1, dc)
                checkNeighbour(image, dr, dc+1)
                checkNeighbour(image, dr, dc-1)
        checkNeighbour(image, sr, sc)
        return image