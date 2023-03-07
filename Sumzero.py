def sumZero(self, n: int) -> list[int]:
        output = [] 
        i = 1 
        if n % 2 == 0:
            j = 0
        else:
            j = 1
            output.append(0)
        while j < n:
            output.append(i)
            output.append(-i)
            i += 1
            j += 2
        return output