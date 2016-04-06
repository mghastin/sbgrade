class GradingScale(object):
	def __init__(self):
		self.scale = {}
		
	def add_grade(self, grade, lowerbound, upperbound):
		self.scale[grade] = [lowerbound, upperbound]
	
	def delete_grade(self, grade):
		try:
			self.scale.pop(grade)
		except KeyError:
			print "Trying to remove a grade not in grading scale."