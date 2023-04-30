def distributeCandies(self, candies: int, num_people: int) -> list[int]:
        arr = [0 for i in range(num_people)]
        i = 0
        j = 1
        while candies > 0:
            if i == len(arr):
                i = 0
            if candies >= j:
                arr[i] =arr[i]+ j
                candies=candies- j
                j += 1
            else:
                arr[i] =arr[i]+candies
                break
            i += 1
        return arr