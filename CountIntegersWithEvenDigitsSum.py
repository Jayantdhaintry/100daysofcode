def countEven(self, num: int) -> int:
        c=0
        for i in range(1,num+1):
            sum=0
            while(i!=0):
                r=i%10
                i=i//10
                sum=sum+r
            if(sum%2==0):
                c=c+1
        return c