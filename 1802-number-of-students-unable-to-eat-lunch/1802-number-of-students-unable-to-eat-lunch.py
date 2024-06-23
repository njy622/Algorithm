class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        stu0 = students.count(0)
        stu1 = students.count(1)
        for i in sandwiches:
            if i == 0 and stu0 > 0 :
                stu0 -= 1
            elif i == 1 and stu1 > 0:
                stu1 -= 1
            else:
                break
        return stu0 + stu1