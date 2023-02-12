def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        ans = [] 
        for i in range(len(candies)):
            m = candies[i] + extraCandies
            if m >= max(candies):
                ans.append(True)
            else:
                ans.append(False)
        return ans