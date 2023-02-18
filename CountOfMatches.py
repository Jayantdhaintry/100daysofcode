def numberOfMatches(self, n: int) -> int:
        c=0
        while(n!=1):
            if(n%2==0):
                m= int(n/2)
                n=int(n/2)
                c+=m
            else:
                m=int(((n-1)/2)+1)
                n=int((n-1)/2)
                c+=m
        return c