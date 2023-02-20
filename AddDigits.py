def addDigits(self, num: int) -> int:
       
        while(num>9):
            c=0
            while(num):
                r=num%10
                c=c+r
                num=num//10
                
            num=c
        return num