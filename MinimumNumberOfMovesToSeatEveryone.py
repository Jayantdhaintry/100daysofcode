def minMovesToSeat(self, seats: list[int], students: list[int]) -> int:
        count = 0
        seats.sort()
        students.sort()
        for i in range(len(students)):
            count += abs(students[i]-seats[i])
        return count