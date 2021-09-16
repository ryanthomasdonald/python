class Student:
    def __init__(self, firstName, lastName, campus):
        self.firstName = firstName
        self.lastName = lastName
        self.campus = campus

    def printStudent(self):
        print(f"{self.firstName} {self.lastName} campus: {self.campus}")

#------------------------------------------

# emily = Student("Emily", "Ye", "Atlanta")
# hunter = Student("Hunter", "Ye", "Houston")
# james = Student("James", "Ivy", "Atlanta")

# campus_list = []

# campus_list.append(emily)
# campus_list.append(hunter)
# campus_list.append(james)

# campus_list = []

# campus_list.append(Student("Emily", "Ye", "Atlanta"))
# campus_list.append(Student("Hunter", "Ye", "Houston"))
# campus_list.append(Student("James", "Ivy", "Atlanta"))

# # print(campus_list)

# for stud_obj in campus_list:
#     print(stud_obj.printStudent())