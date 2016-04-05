from progress import Progress
	
class Student(object):
	def __init__(self, name):
		self.name = name
		work = {}
		schedule = []
	
	def set_schedule(self, schedule):
		assert isinstance(schedule, list), "schedule given is not a list."
		self.schedule = schedule
	
	def add_course(self, course):
		schedule.append(course)
		work[course] = []
	
	def add_progress(self, course, type, progress):
		assert isinstance(progress, Progress), "Progress not given."
	 	if self.work[course][type] != []:
			raise "Trying to overwrite student's %r progress for course %r" \
			% (type, course) 
		self.work[course][type] = progress
		
	def grades(self, lg = None):
		snapshot = {}
		for course, progresses in self.work.items():
			for type, progress in self.work[course].items():
				snapshot[course][type] = progress.most_recent()
		return snapshot
				
		
	