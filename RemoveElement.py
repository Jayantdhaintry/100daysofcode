def removeElement(self, nums: list[int], val: int) -> int:
    for i in nums:
        if i == val:
            nums.count(i)
            for j in range(nums.count(i)):
                nums.remove(i)
                return nums
            
a=[2,5,6,9,11]
b=int(input()) #The element to be removed
print(removeElement("The List",a,b))