#def input():
# This function takes in values from the user
		
#class course_grade
	# dictionary with (lg number, grade)
	# period
	# average of lgs (overall grade)
	# stats (highest lg, lowest lg)



#class course
	# list of learning goals
	# list of student names
	# grading periods (Q1, Q2, S1, S2, etc) weeks
	# statistics
	# instructor
	# grade cut offs / assignment 
	# year

#global student_bank = {}
#global course_bank = {}
# is this the best way to do this???

def create_student(name):
	new_student = Student(name)
	student_bank[name] = new_student

def create_course(name):
	new_course = Course(name)
	course_bank[name] = new_course

def add_student_to_course(student, course):
	assert isinstance (student, Student)
	assert isinstance (course, Course)
	course.add_student(student.get_name())
	student.add_course(course.get_name())

def json_cleanup(str):
		str = str.replace('\"{', '{')
		str = str.replace('}\"', '}')
		str = str.replace('\\"','"') 
		return str
	
#module IO
#module store
#dictionary (course names, courses)
#dictionary (student name, students)
