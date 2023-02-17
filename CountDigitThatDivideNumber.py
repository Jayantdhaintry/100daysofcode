def countDigits(self, num: int) -> int:
        c=0
        temp=num
       
        while(num>0):
            r=num%10
            if(temp%r==0):
                c=c+1
    
            num=num//10
        return c
