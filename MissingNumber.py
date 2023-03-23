def missingNumber(self, nums: list[int]) -> int:
        l=len(nums)
        nums.sort()
        missing=0

        for i in nums:
            if i!=missing:
                return missing
            missing+=1
        else:
            return missing