def selfDividingNumbers(self, left: int, right: int) -> list[int]:
        v = []
        for x in range(left, right+1):
            a = [*str(x)]
            d = True
          
            for r in a:
                if int(r) != 0: 
                    if x%int(r)!=0:
                        d = False
                else:
                    d = False
            if d:
                v.append(x)

        return v