def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
    result = []
    for i in sorted(heights)[::-1]:
	    result.append(names[heights.index(i)])
         
    return result