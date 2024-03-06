class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        many = max(candies)
        for i in range (0,len(candies)):
            if extraCandies + candies[i] >= many:
                result.append(True)
            else:
                result.append(False)
        return result
