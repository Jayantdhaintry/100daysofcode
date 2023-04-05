def countLargestGroup(self, n: int) -> int:
        l=[]
        for i in range(1,n+1):
            s=0
            while(i>0):
                s=s+(i%10)
                i=i//10
            l.append(s)
        a=Counter(l)
        m=max(a.values())
        c=0
        for i in a.keys():
            if a[i]==m:
                c+=1
        return c