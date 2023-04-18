def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1: return 1

    
        count=0
        result = ''

        for i in s:
            if i not in result:
                result += i
            else:
                result = result[result.index(i)+1:] + i

            if len(result) > count:
                count = len(result)
        
        return count