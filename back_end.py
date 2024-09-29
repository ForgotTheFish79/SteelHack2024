import google.generativeai as genai
import os
import Student

'''
We are using Python 3.10.
Note: in order to use Gemini API, you need an API key.
Steps to get API key:
    1. Visit https://ai.google.dev/ and sign in
    2. Click "Get API key in Google AI Studio"
    3. Click "Create API key"
    4. Click "Create API key in new project"
        This step will NOT work with Pitt emails!
    5. Type in your console:
        export API_KEY=<API_KEY_HERE>       
        This stores your key as an environmental variable.    
Now you should be able to run your code in the console normally.    
'''

genai.configure(api_key=os.environ["API_KEY"])
model = genai.GenerativeModel("gemini-1.5-flash")

# get student info from HTML
# sample info below
courses = {"DSA 1"}
name = "Chris"
year = 2027
major = "Computer Science"
given_student = Student.Student(courses, name, year, major)
print(given_student)

# method to read in text from file
def read_file(file):
    with open(file, 'r') as file:
        sql_script = file.read()
    return sql_script

# read in relevant files
all_students = read_file("SQLTables/students.sql") # SQL database of students
all_courses = read_file("SQLTables/courses.sql") # all courses
student_courses = read_file("SQLTables/student_courses.sql") # courses taking
all_interests = read_file("SQLTables/interests.sql")
student_interests = read_file("SQLTables/student_interests.sql")

# create specific prompt with given info for Gemini
prompt = ("\nLooking at these SQL files, which students would work best with "
         "the given student?\n"
         f"File of all students: \n{all_students}\n" 
         f"File of all courses: \n{all_courses}\n" 
         f"File of classes each student is taking: \n{student_courses}\n"
         f"File of all interests: \n{all_interests}\n"
         f"File of student intersts: \n{student_interests}\n"
         f"Given student: \n{given_student}\n"
         "\nOnly answer with the names of three other students "
         "in a single sentence.")

print(f"\n{prompt}\n")

# prompt model
response = model.generate_content(prompt)
print(response.text)

# send output to HTML
# code here...