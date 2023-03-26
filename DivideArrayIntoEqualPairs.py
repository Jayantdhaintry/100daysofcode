def divideArray(self, nums: list[int]) -> bool:
        if len(nums)%2!=0:
            return False
        else:
            for i in nums:
                if (nums.count(i)%2!=0):
                    return False
            else:
                return True