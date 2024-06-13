class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        count = 0
        seats.sort()
        students.sort()

        for i in range(len(seats)):
            if seats[i] > students[i]:
                count += seats[i] - students[i]
            else:
                count += students[i] - seats[i]

        return count

                    