def largestOddNumber(self, num: str) -> str:
        
        l=len(num)-1
        while(l>=0):
            if(int(num[l])%2!=0):
                return num[:l+1]
            l=l-1
        return ""