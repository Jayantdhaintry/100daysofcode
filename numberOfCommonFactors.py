def commonFactors(self, a: int, b: int) -> int:
        minimum=min(a,b)
        c=0
        while minimum>0:
            if ( a%minimum==0 and b%minimum==0):
                c+=1
            minimum-=1
        return c