def plusOne(self, digits: list[int]) -> list[int]:
        rev = 0
        for i in digits:
            rev = (rev * 10) + i
        rev += 1
        output = [int(x) for x in str(rev)]
        return output