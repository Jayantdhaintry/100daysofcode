def minimumSum(self, num: int) -> int:
        l=[]
        while(num!=0):
            a=num%10
            l.append(a)
            num//=10
        l.sort()
        output=(l[1]*10+l[2])+(l[0]*10+l[3])
        return output