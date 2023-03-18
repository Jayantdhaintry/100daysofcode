def countTriples(self, n: int) -> int:
        count=0
        for i in range(1,n):
            for j in range(i+1,n):
                sqr=math.sqrt((i**2)+(j**2))
                if sqr<=n and int(sqr)==sqr:
                    count+=2
        return count