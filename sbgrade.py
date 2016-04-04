
class learning_goal(Object):
	#title
	#number
	#description
	#standard
	
class student
	#work, dictionary(course name, progress...{"Engagement" : progress, "Assessment": progress, "Practice":progress})
	#name
	#current grades, dictionary with (course name, course_grades)
	# calculate grade function
		
class course_grade
	# dictionary with (lg number, grade)
	# period
	# average of lgs (overall grade)
	# stats (highest lg, lowest lg)

class progress(lg list)
	# dictionary lg_map(learning_goal, history), get lgs from course
	# number of attempts
	# get grade function 
	# get growth function 
	# type (assessment, practice, engagement)

class course
	# learning goals
	# list of student names
	# grading periods (Q1, Q2, S1, S2, etc) weeks
	# statistics
	# instructor
	# grade cut offs / assignment 
	# year

class attempt
	# score
	# out of
	# comments
	# date
	# bool most_recent
	# learning goal
	
class history
	# learning goal
	# list of attempts
	# statistics (best, most recent, average)
	
module IO
module store
dictionary (course names, courses)
dictionary (student name, students)
