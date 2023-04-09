def searchInsert(self, nums: list[int], target: int) -> int:
        l = 0
        h = len(nums)-1
        while(l<=h):
            mid = (l+h)//2
            if nums[mid]==target: 
                return mid
            elif nums[mid]>target: 
                h=mid-1
            else: 
                l=mid+1
        return l