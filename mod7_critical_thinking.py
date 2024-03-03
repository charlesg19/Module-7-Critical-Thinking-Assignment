room_number = {"CSC101":"3004", "CSC102":"4501", "CSC103":"6755", "NET110":"1244", "COM241":"1411"}
instructor = {"CSC101":"Haynes", "CSC102":"Alvarado", "CSC103":"Rich", "NET110":"Burke", "COM241":"Lee"}
meeting_time = {"CSC101":"8:00 a.m", "CSC102":"9:00 a.m.", "CSC103":"10:00 a.m.", "NET110":"11:00 a.m.", "COM241":"1:00 p.m."}

def print_course_info(course):
    print("Room Number:", room_number[course])
    print("Instructor:", instructor[course])
    print("Meeting Time:", meeting_time[course])

course_number = input("Enter course number:\n")
if (course_number in room_number) and (course_number in instructor) and (course_number in meeting_time):
    print_course_info(course_number)
else:
    print("Course number not found.")
