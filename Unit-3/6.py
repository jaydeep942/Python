#  Create a Student class to with the methods set_id, get_id,
# set_name, get_name, set_marks and get_marks where the
# method name starting with set are used to assign the values and
# method name starting with get are returning the values. Save
# the program by student.py.
# Create another program to use the Student class which is already
# available in student.py


import practical_6_class as student_in_main

student1 = student_in_main.Student()

student1.set_id(101)
student1.set_name("Chovatiya Shashwat ArvindBhai")
student1.set_marks(80)

print(f"\n Student Id : {student1.get_id()} ,\n Student Name : {student1.get_name()} ,\n Student Marks : {student1.get_marks()}")