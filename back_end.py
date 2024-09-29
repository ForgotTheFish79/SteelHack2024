import google.generativeai as genai
import os
import Student
from flask import Flask, request, render_template

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

# configure model
genai.configure(api_key=os.environ["API_KEY"])
model = genai.GenerativeModel("gemini-1.5-flash")

# create app
app = Flask(__name__)

# home page route
@app.route('/')
def home():
    return render_template('index.html')

# initialize variables
name = ""
major = ""
year = 0
interests = ""
courses = []

# creates user profile when button is clicked
@app.route('/create_profile', methods=['POST'])
def create_profile():
    # get form data
    name = request.form['username']
    email = request.form['email']
    major = request.form['major']
    year = request.form['year']
    interests = request.form['interests']
    courses = request.form['courses']
    return f"Profile created for {name} with email {email}. Major: {major}, 
             Year: {year}, Interests: {interests}, Courses: {courses}."

# runs if main script
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
    
# method to read in text from file
def read_file(file):
    with open(file, 'r') as file:
        sql_script = file.read()
    return sql_script

# create student object
given_student = Student.Student(courses, name, year, major, interests)
print(given_student)

# read in files with student info as strings
all_students = read_file("SQLTables/students.sql")
all_courses = read_file("SQLTables/courses.sql")
student_courses = read_file("SQLTables/student_courses.sql")
all_interests = read_file("SQLTables/interests.sql")
student_interests = read_file("SQLTables/student_interests.sql")

# create specific prompt with given info for Gemini
prompt = ("\nLooking at these SQL files, which 3 students would work "
        " best with the given student?\n"
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
response = "Gemini API response:", model.generate_content(prompt)
print(response.text)