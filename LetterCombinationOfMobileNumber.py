def letterCombinations(self, digits: str) -> list[str]:
        
        # If digit is empty return empty
        if not digits:
            return []
        
        # Variables required
        d={"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        res=[""]
        

        # Three for loops, first iterate digits, x will contain each word, iterate each string corresponding to digit in the 
        # dictionary, Then whatever is in result, add iterate that and append with j and k in x, then store it in res.
        for i in digits:
            x=[]
            for j in d[i]:
                for k in res:
                    x.append(k+j)
                    
                    
            res=x
            
        return res
        
