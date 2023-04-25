def passThePillow(self, n: int, time: int) -> int:
        r=time//(n-1)
        steps=r*(n-1)
        if time<n:
            output=time+1
        elif time>n:
            if r%2==0:
                output=(time-steps)+1
            else:
                output=n-((time-steps)+1)+1
        else:
            output=time-1
        return output