def isPerfectSquare(self, num: int) -> bool:
        if num==1:
            return True
        else:
            l=0
            r=num
            while l<r:
                mid=(l+r)//2
                if mid *mid ==num:
                    return True
                    break
                elif mid*mid>num:
                    r=mid
                else:
                    l=mid+1
            return False