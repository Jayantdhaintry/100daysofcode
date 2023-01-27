def lengthOfLastWord(self, s: str) -> int:
         s = s.rstrip()  
         return len(s.split()[-1])
        
s=input()
print(lengthOfLastWord("length:",s))