def subtractProductAndSum(self, n: int) -> int:
        product=1
        sum=0

        while(n!=0):
    
            r=n%10
            n=n//10
            product=product*r
            sum=sum+r

        output=product-sum
        return output