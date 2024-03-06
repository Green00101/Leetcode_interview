class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        if len(flowerbed) == 1:
            if flowerbed[0] == 1:
                if n == 0:
                    return True
                else:
                    return False
            else:
                return True
        if flowerbed[0] == 0 and flowerbed[1] == 0:
            flowerbed[0] = 1
            count+=1
        for i in range (1,len(flowerbed)-1):
            if flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                flowerbed[i] = 1
                count+=1
        if flowerbed[-1] == 0 and flowerbed[-2] == 0:
            flowerbed[-1] = 1
            count+=1
        if count >= n:
            return True
        else:
            return False
