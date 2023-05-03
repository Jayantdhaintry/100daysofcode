def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        set1=set(nums1)
        set2=set(nums2)
        res=[[],[]]

        for i in set1:
            if i not in set2:
                res[0].append(i)
        for i in set2:
            if i not in set1:
                res[1].append(i)
        return res