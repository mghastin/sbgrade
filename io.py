import json
from student import Student

class StudentEncoder(json.JSONEncoder):
	def default(self, student_obj): 
		if isinstance(student_obj, Student):
			student_work = {}
			for course, info in student_obj.work.items():
				progresses = {}
				for type, progress_obj in info.items(): 
					progress = progress_obj.get_json()
					progresses[type] = progress
				student_work[course] = progresses
			student_dict = {"__student__" : true, "name" : student_obj.get_name(),\
						"work" : student_work, "schedule" : student_obj.get_schedule()}
			return student_dict
		return json.JSONEncoder.default(self, obj)

# __student__ is used in JSON decoder to determine it is a Student object

def decode_object(json_dict):
	if "__student__" in json_dict:
		new_student = Student(json_dict["name"])
		json_dict.pop("__student__")
		for course, info in json_dict["work"].items():
			new_student.add_course(course)
			for type, progress in info.items():
				progress_obj = Progress(type)
				for lg, attempts in progress.items():
					progress_obj.add_lg(lg)
					for attempt in attempts:
						progress_obj.add_attempt(attempt["lg"], \
							Attempt(attempt["score"], attempt["outof"], \
							attempt["date"], attempt["lg"], attempt["comment"]))
				new_student.add_progress(course, type, progress_obj)
	# for later: add in a decoder for courses, learning goals

def store(obj)
	if isinstance(obj, Student)
		with open(obj.get_name()+'.txt', 'w') as outfile:
			json.dump(obj, cls=StudentEncoder)					