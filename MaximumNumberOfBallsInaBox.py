def countBalls(self, lowLimit: int, highLimit: int) -> int:
        li=[]
        for i in range(lowLimit,highLimit+1):
            s=0
            while(i>0):
                s=s+i%10
                i=i//10
            li.append(s)
        x=Counter(li)
        return max(x.values())