def pivotInteger(self, n: int) -> int:
        for i in range(1,n+1):
            l=((i+1)*i)//2
            r=(n*(n+1))//2-(i*(i-1))//2
            if r==l:
                return i
        return -1
