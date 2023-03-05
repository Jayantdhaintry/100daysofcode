def alternateDigitSum(self, n: int) -> int:
        x=str(n)
        l1=[]
        l2=[]
        for i in range(len(x)):
            if i%2==0:
                l1.append(int(x[i]))
            else:
                l2.append(int(x[i]))
        return sum(l1)-sum(l2)