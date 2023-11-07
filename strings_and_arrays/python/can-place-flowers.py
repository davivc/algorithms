class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        cont = 0
        for i in range(len(flowerbed)):
            if len(flowerbed) == 1:
                pr = 0
                ne = 0
            elif i == 0:
                pr = 0
                ne = flowerbed[i+1]
            elif i == len(flowerbed)-1:
                pr = flowerbed[i-1]
                ne = 0
            else:
                pr = flowerbed[i-1]
                ne = flowerbed[i+1]

            if flowerbed[i] == 0 and pr+ne == 0:
                cont += 1
                flowerbed[i] = 1

            if cont >= n:
                break

        if cont >= n:
            return True
        return False
