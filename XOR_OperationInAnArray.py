def xorOperation(self, n: int, start: int) -> int:
        output=[]
        xor=0
        i=0
        while i!=n:
            output.append(start+2*i)
            i+=1
        for i in range(len(output)):
            xor^=output[i]
        return xor