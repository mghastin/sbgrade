from learning_goal import LearningGoal
from grading_scale import GradingScale
		
class Course(object):
	def __init__(self, name):
		self.students = [] # list of student names
		self.learning_goals = []
		self.grading_periods = []
		self.school_year = 0
		self.name = name
	
	def add_student(self,student_name):
		self.students.append(student_name)
	
	def remove_student(self,student_name):
		try: 
			self.students.remove(student_name)
		except ValueError:
			print "Could not find student in course list."
	
	def get_student_list(self):
		return self.students
	
	def get_grading_periods(self):
		return self.grading_periods
	
	def add_grading_period(self, period):
		self.grading_periods.add(period)
	
	def remove_grading_period(self, period):
		try: 
			self.grading_period.remove(period)
		except ValueError:
			print "Could not find grading period in course."
		
	def get_number_of_students(self):
		return len(self.students)
	
	def get_number_grading_periods(self):
		return len(self.grading_periods)
	
	def set_grade_cutoffs(self, grading_scale):
		assert isinstance(grading_scale, GradingScale)
		self.grading_scale = grading_scale
	
	def set_instructor(self,instructor):
		self.instructor = instructor
	
	def get_instructor(self):
		return self.instructor
	
	def set_year(self, year):
		self.school_year = year
	
	def get_year(self):
		return self.school_year()
	
	def add_learning_goal(self, learning_goal):
		assert isinstance(learning_goal, LearningGoal)
		self.learning_goals.append(learning_goal)
	
	def remove_learning_goal(self, learning_goal):
		try: 
			self.grading_period.remove(learning_goal)
		except ValueError:
			print "Could not find learning goal in course."	
	
	def get_learning_goals(self):
		return self.learning_goals
	
	def get_number_of_lgs(self):
		return len(self.learning_goals)
	
	def get_name(self):
		return self.name
	
	def set_name(self, new_name):
		self.name = new_name