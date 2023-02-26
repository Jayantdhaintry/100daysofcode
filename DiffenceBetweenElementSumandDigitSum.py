def differenceOfSum(self, nums: list[int]) -> int:
        digit_sum = 0
        for i in nums:
            for j in str(i):
                digit_sum+=int(j)
        return sum(nums) - digit_sum