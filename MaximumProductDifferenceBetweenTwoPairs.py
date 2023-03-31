def maxProductDifference(self, nums: list[int]) -> int:
        x = max(nums)
        nums.remove(x)
        y = max(nums)
        nums.remove(y)
        
        z = min(nums)
        nums.remove(z)
        w = min(nums)
        nums.remove(w)
        
        return (x*y) - (z*w)