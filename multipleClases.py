#object Oriented Programming in Python.
#Create the class Student, initate it from the biggining with init and define the atributes, self to initiate, name, age, and grede
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade # 0 -100

    def get_grade(self):
        return self.grade

#Create the class Course where we will add the students for the course, and define the method  with its attributes
class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []
#Create a method that will help us to add the students to the list, but will also compare the stunds with the max admited in the course.
    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False
#Define a method that will returm the avarage greade in the course.
    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade
        
        return value / len(self.students)


#Now I will create students to be added to the list
s1 = Student("Tim", 19, 95)
s2 = Student("Jerry", 19, 75)
s3 = Student("Jill", 19, 65)
#Also I will create a course where the students will be added, and delimited the number of students.
course = Course("Science", 2)
course.add_student(s1)
course.add_student(s2)
#Now I want to see if the students were added to the list.
print(course.students[1].name)
#Now I want to see the average grade in the mentioned course
print(course.get_average_grade())