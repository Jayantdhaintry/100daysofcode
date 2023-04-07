def shuffle(self, nums: list[int], n: int) -> list[int]:
        left = 0
        right = n
        result = []
        while left < n:
            result.append(nums[left])
            result.append(nums[right])
            left+=1
            right+=1
        return result