def maximumProduct(self, nums: list[int]) -> int:
        if len(nums) == 3:
            return nums[0] * nums[1] * nums[2]
        max1 = max2 = max3 = -1000 
        min1 = min2 = 1000
        for i in nums:
            if i > max1:
                max3 = max2
                max2 = max1
                max1 = i
            elif i > max2:
                max3 = max2
                max2 = i
            elif i > max3:
                max3 = i
            if i < min1:
                min2 = min1
                min1 = i
            elif i < min2:
                min2 = i

        return max(max1 * max2 * max3, min1 * min2 * max1)