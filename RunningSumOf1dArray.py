def runningSum(self, nums: list[int]) -> list[int]:
        sums=0
        output=[]
        for i in nums:
            sums+=i
            output.append(sums)
        return output