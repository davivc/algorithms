class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        greatest = max(candies)
        withExtra = list(map(lambda x: True if(x+extraCandies) >= greatest else False, candies))
        return withExtra