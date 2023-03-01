def findGCD(self, nums: list[int]) -> int:
        x= min(nums)
        y = max(nums)
        output = 1
        for i in range(1, x + 1):
            if x % i ==0 and y % i == 0:
                output = max(i, output)
        return output