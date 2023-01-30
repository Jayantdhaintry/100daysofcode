def finalValueAfterOperations(self, operations: list[str]) -> int:
        x=0
        for i in operations:
            if i=='X--' or i=='--X':
                x-=1
            if i=='++X'or i=='X++':
                x+=1
                print(x)
        return x

