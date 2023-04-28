def minCostToMoveChips(self, position: list[int]) -> int:
        c1=0
        c2=0
        for i in position:
            if i%2==0:
                c1+=1
            else:
                c2+=1
        if(c1>c2):
            return c2
        else:
            return c1
       