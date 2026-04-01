class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        i = 0
        found = False
        while i < len(flowerbed) - 1:
            if flowerbed[i] == 0 and flowerbed[i+1] == 0:
                n -= 1
                if n == 0:
                    found = True
                    break
                i += 1
            elif flowerbed[i] == 1:
                i += 1
            i += 1
        if not found:
            if i < len(flowerbed) and flowerbed[i] == 0 and flowerbed[i-1] == 0:
                n -= 1
        return True if n == 0 else False
