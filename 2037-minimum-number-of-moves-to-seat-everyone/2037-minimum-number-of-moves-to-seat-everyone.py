class Solution(object):
    def minMovesToSeat(self, seats, students):
        """
        :type seats: List[int]
        :type students: List[int]
        :rtype: int
        """
        seats.sort()
        students.sort()
        total =0
        for i in range(len(students)):
            total+= abs(students[i] - seats[i])

        return total

        