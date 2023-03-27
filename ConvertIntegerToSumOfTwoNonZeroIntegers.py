def getNoZeroIntegers(self, n: int) -> list[int]:
        output = []
        for i in range(1,n):
            
            if ("0" not in str(i) and "0" not in str(n-i)):
                output.append(i)
                output.append(n-i)
                return output