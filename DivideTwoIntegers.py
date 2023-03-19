def divide(self, dividend: int, divisor: int) -> int:
        check=False
        if dividend < 0 or divisor < 0:
            check=True

        if dividend < 0 and divisor < 0:
            check = False
        result = abs(dividend) // abs(divisor)
        if check:
            result = -result
        
        if dividend==-2147483648 and divisor==-1 :
            return 2147483647
        return result