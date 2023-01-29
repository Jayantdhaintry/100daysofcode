def balancedStringSplit(self, s: str) -> int:
        stack, result = [], 0
                        
        for char in s:            
            if stack == []:
                stack.append(char)
                result += 1
            elif char == stack[-1]:
                stack.append(char)
            else:
                # []
                stack.pop()
                
        return result

s="RLRRLLRLRL"
print(balancedStringSplit("Output",s))