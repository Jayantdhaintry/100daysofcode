def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        output=[]
        for i in range(len(nums)):
            count=0
            for j in range(len(nums)):
                if nums[i]>nums[j]:
                    count+=1
            output.append(count)    
        return output

