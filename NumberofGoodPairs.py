def numIdenticalPairs(self, nums: list[int]) -> int:
        pairs = 0
        d = {}
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        for num in d:
            val = d[num]
            for i in range(val):
                pairs += i
        return pairs