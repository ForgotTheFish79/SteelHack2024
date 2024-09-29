class Student:
    # Student constructor
    # lets year & major be optional fields
    def __init__(self, courses, name, year=0, major=""):
        self.courses = courses
        self.name = name
        self.year = year
        self.major = major

    # create getters and setters for each variable:
    
    # courses
    def get_courses(self):
        return self.courses
    
    def set_courses(self, new_courses):
        self.courses = new_courses
    
    # name
    def get_name(self):
        return self.name
    
    def set_name(self, new_name):
        self.name = new_name
    
    # year
    def get_year(self):
        return self.year
    
    def set_year(self, new_year):
        self.year = new_year
    
    # major
    def get_major(self):
        return self.major
    
    def set_major(self, new_major):
        self.major = new_major   
        
    # String representation of a student
    def __repr__(self): 
        return (f"This student's name is {self.name}, their major is "
                f"{self.major}, and they graduate in {self.year}. "
                f"They are currently taking: {self.courses}.")