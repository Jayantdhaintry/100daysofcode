def addBinary(self, a: str, b: str) -> str:
        result = ""
        i = len(a) - 1
        j= len(b) - 1
        
        c = 0
        
        while i >= 0 or j >= 0:
            sum_ = c
            
            if i >= 0:
                sum_ += ord(a[i]) - ord('0')
            if j >= 0:
                sum_ += ord(b[j]) - ord('0')
                
            i = i - 1
            j=j - 1  
            c = 1 if sum_ > 1 else 0 
            result += str(sum_ % 2) 
            
        if c != 0:
            result += str(c)  
            
        return result[::-1] 