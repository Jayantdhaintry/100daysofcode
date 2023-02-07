def reverse(self, x: int) -> int:
        number = list(str(x))
        if number[0] == '-':
            reversed_number = int("-" + ''.join(number[1:][::-1]))
        else:
            reversed_number = int(''.join(number[::-1]))
        
        if reversed_number >= -2**31 and reversed_number <= 2**31 - 1:
            return reversed_number
        else:
            return 0