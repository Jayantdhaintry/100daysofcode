def leftRigthDifference(self, nums: list[int]) -> list[int]:
        

        left  = 0
        right=sum(nums)      

        for i, num in enumerate(nums):  
                                        
            left=left+ num                 
            nums[i] = abs(right-left)  
            right=right-num                 
                                         
        return nums