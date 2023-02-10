def multiply(self, num1: str, num2: str) -> str:
        num = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
        n1=0
        n2=0
        
        for i in num1:
            n1=10*n1+num[i]
        for j in num2:
            n2=10*n2+num[j]
            
        return str(n1*n2)