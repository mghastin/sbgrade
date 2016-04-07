from learning_goal import LearningGoal
from attempt import Attempt
import json
import string
from sbgrade import json_cleanup

class Progress(object):
	
	def __init__(self, type): 
		self.attempts = {}
		self.type = type

	def add_lg(self, lg): # lg number
		self.attempts[lg] = [] # initialize array

	def get_type(self):
		return self.type
		
	def get_learning_goals(self):
		return self.attempts.keys()
	
	def get_attempts(self,lg): # need to pass a LearningGoal object
		assert isinstance(lg, LearningGoal), "Not Learning Goal"
		return self.attempts[lg] # returns a list of Attempts
	
	def add_attempt(self, attempt, lg): 
		assert isinstance(attempt, Attempt), "Not Attempt"
		#assert isinstance(lg, LearningGoal), "Not Learning Goal"
		assert lg in self.attempts, "Progress does not track this Learning Goal."
		self.attempts[lg].append(attempt)
		self.attempts[lg].sort(reverse = True) # sort newest first

	def most_recent(self, lg): # pass a Learning Goal, gives most recent attempt
		assert type(lg) is LearningGoal, "Not a Learning Goal."
		assert lg in self.attempts, "Progress does not track this Learning Goal."
		return self.attempts[lg][0]
	
	def most_recent(self): 
		most_recents = {}
		for lg, history in self.attempts:
			most_recents[lg] = history[0]
		return most_recents
	
	def get_json(self): # returns a dictionary that can be json serialized
		json_attempts = {} # dictionary to store json attempts
		for lg, attempt_list in self.attempts.items():
			json_list = []
			for attempt in attempt_list:
				json_list.append(attempt.get_json())
			lg_num = lg.get_number()
			json_attempts[lg_num] = json_list
		return json_attempts
	# for later: make attempt search function
	# for later: make attempt delete function
	# store the best attempt for each learning goal (highest!!)