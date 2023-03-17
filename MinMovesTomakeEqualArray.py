def minMoves(self, nums: list[int]) -> int:
        count=0
        m = min(nums)
        i = nums.index(m)
        for j in range(len(nums)):
            if(i==j):
                continue
            else:
                count = count+nums[j]-nums[i]
        return count