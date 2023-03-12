def averageValue(self, nums: list[int]) -> int:
        sum = 0
        divisor = 0
        for num in nums:
            if num%2==0 and num%3==0:
                sum+=num
                divisor+=1
        if divisor == 0:
            return 0
        return int(sum/divisor)