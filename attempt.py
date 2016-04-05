import string 
class Attempt(object):
	def __init__(self, score, outof, date, lg, comment):
		# store values in a dictionary called "info"
		self.info = {"score": score, "outof": outof, 
				   "date": date, "lg": lg, "comment": comment}
		self.month, self.day, self.year = self.__parse_date__()
	
	def __parse_date__(self):
		# date must be in mm/dd/yyyy format
		month, day, year = string.split(self.info["date"], "/")
		return int(month), int(day), int(year)
	
	# define comparison function so can sort attempts by date!
	def __cmp__(self, other): # return -1 if self less, 0 if same, 1 if self more
		if self.year < other.year:
			return -1
		elif self.year == other.year: # if same year, compare months
			if self.month < other.month: 
				return -1
			elif self.month == other.month: # if same month, compare days
				if self.day < other.day:
					return -1
				elif self.day == other.day: # same month, day, yr -> equal!
					return 0
				else:
					return 1
			else:
				return 1
		else:
			return 1			
					   	
	def get_score(self):
		return self.info["score"]
	
	def get_outof(self):
		return self.info["outof"]
	
	def get_date(self):
		return self.info["date"]
		
	def get_learning_goal(self):
		return self.info["lg"]
	
	def get_comment(self):
		return self.info["comment"]
		
	def update(self, field_to_change, new_value):
		new_info = {}
		for field, value in self.info.items():
			if(field == field_to_change):
				new_info[field] = new_value
			else:
				new_info[field] = value
		self.info = new_info