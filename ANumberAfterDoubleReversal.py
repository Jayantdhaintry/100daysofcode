def isSameAfterReversals(self, num: int) -> bool:
        original=num
        r1=0
        while num!=0:
            r1=(num%10)+r1*10
            num//=10
        r2=0
        while r1!=0:
            r2=(r1%10)+r2*10
            r1//=10
        if(r2==original):
            return True
        else:
            return False