def arraySign(self, l: list[int]) -> int:
        product=1
        for i in l:
            product=product*i
        if(product>0):
            return 1
        elif(product<0):
            return -1
        else:
            return 0