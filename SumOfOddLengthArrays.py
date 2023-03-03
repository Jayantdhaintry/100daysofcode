def sumOddLengthSubarrays(self, arr: list[int]) -> int:
        output=0
        for i in range(len(arr)):
            for j in range(i,len(arr),2):
                output+=sum(arr[i:j+1])
        return output