class Attempt(object):
	def __init__(self, score, outof, date, lg, comment):
		# store values in a dictionary called "info"
		self.info = {"score": score, "outof": outof, 
				   "date": date, "lg": lg, "comment": comment}
				   	
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