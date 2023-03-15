def sumOfThree(self, num: int) -> list[int]:
        if num%3==0:
            c=num//3
            return [c-1,c,c+1] 
        else:
            return []