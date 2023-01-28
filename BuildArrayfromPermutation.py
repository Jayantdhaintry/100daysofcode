def buildArray(self, nums: list[int]) -> list[int]:
        n = len(nums)
        val = 0
        for i in range(0, n):
            nums[i] = n * ( nums[nums[i]] % n) + nums[i]
        for i in range(0,n):
            nums[i] = nums[i] // n
        return nums


a=[5,8,10,15]

print(buildArray("Array:",a[2]))
