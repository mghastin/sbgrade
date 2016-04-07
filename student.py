from progress import Progress

	
class Student(object):
	def __init__(self, name):
		self.name = name
		self.work = {}
		self.schedule = []
	
	def set_schedule(self, schedule):
		assert isinstance(schedule, list), "schedule given is not a list."
		self.schedule = schedule
	
	def add_course(self, course): # course identifier, not Course object
		self.schedule.append(course)
		self.work[course] = {}
	
	def add_progress(self, course, type, progress):
		assert isinstance(progress, Progress), "Progress not given."
		self.work[course][type] = progress
		
	def grades(self):
		snapshot = {}
		for course, progresses in self.work.items():
			for type, progress in self.work[course].items():
				snapshot[course][type] = progress.most_recent()
		return snapshot
	
	def get_name(self):
		return self.name	
		
	def get_schedule(self):
		return self.schedule
		
	def store(self):	
		# write to json file
			
				 
			
	