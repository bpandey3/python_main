myset = {"Red", "Green", "Blue"}
print(myset)

class Course:
    def __init__(self, name) -> None:
        self.name = name
        print("Passed name is {0}".format(self.name))
        self.student =[]

    def add_students(self,student):
        self.student.append(student)
        print("Appended name is {0}".format(self.student))

    def print_list(self):
        print("Printed list name is {0}".format(self.student))
    def __delete_students(self,student):
        self.student.remove(student)
        print("Delete from private fn name is {0}".format(self.student))

    def delete_public_students(self,student):
        print("Delete public fn name is {0}".format(self.student)) 
        self.__delete_students(student)
           

class FullCourse(Course):
    def __init__(self, name) -> None:
        super().__init__(name)

    def print_full_name(self):
        print("From full name find a way to print {0}".format(self.student))


c1 = Course("Bipin")
# c2 = Course("Bipin Pandey")
# c1.add_students("Harita")
# c1.add_students("Triaksha")
# # c2.add_students("Varnika")
# # c2.delete_public_students("Varnika")
# #private access
# #c.__delete_students("Varnika")
# #del c1
# c1.print_list()

# print("Fetch from child class")
# c2 = FullCourse("PPP")
# c2.print_full_name()

print(hasattr(c1,'add_student'))

print(hasattr(c1,'add_students'))
