def countOperations(self, num1: int, num2: int) -> int:
        ope=0
        while(num1!=0 and num2!=0):
            if(num1>=num2):
                num1-=num2
                ope+=1
            else:
                num2-=num1
                ope+=1
        return ope