def getConcatenation(self, nums: list[int]) -> list[int]:
        n=len(nums)
        output=[]
        for i in range(0,2*n):
            if i<n:
                output.append(nums[i])
            else:
                output.append(nums[i-n])
        return output