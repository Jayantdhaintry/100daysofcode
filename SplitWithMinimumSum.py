def splitNum(self, num: int) -> int:
        m = [int(x) for x in str(num)]
        m.sort()
        num1 = 0
        num2 = 0
        for i in range(0,len(m)):
            if i %2 == 0:
                num1 = num1*10 + m[i]
            elif i %2 !=0:
                num2 = num2*10 + m[i]
        return num1 + num2