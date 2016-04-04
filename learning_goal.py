class LearningGoal(object):
	def __init__(self, title, number, description, standard):
		# store values in a dictionary called "info"
		self.info = {"title": title, "number": number, 
				   "description": description, "standard": standard}
	def get_title(self):
		return self.info["title"]
	
	def get_number(self):
		return self.info["number"]
	
	def get_description(self):
		return self.info["description"]
	
	def get_standard(self):
		return self.info["standard"]
	
	def update(self,field_to_change, new_value):
		new_info = {}
		for field, value in self.info.items():
			if(field == field_to_change):
				new_info[field] = new_value
			else:
				new_info[field] = value
		self.info = new_info