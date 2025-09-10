class Sports:
	def __init__(self,sport_name):
		self.sport_name = sport_name

	def display_sport(self):
		# print("Your favorite sport is : ", {self.sport_name})
		print(f"Sport : {self.sport_name} ")
        # print(f"Sport: {self.sport_name}")
		
class Semister:
	def __init__(self,semister):
		self.semister = semister

	def display_semister(self):
		print(f"Your semister is : {self.semister} ",)

class Student(Sports,Semister):
	def __init__(self,sport_name,semister,name):

		self.name= name

		Sports.__init__(self,sport_name)
		Semister.__init__(self,semister)

	def display_student(self):
		print("Your name is :",self.name)
		self.display_sport()
		self.display_semister()


student1 = Student("Cricket",5,"Shashwat")
student1.display_student()