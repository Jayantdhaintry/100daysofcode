def arrayPairSum(self, nums: list[int]) -> int:
        output=0
        nums.sort()
        i=0
        while i<len(nums):
            if i%2==0:
                output+=nums[i]
                i+=1
            i+=1
        return output