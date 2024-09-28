class Student:
    # Student constructor
    def __init__(self, courses, study_time, name, year=0, major=""):
        self.courses = courses
        self.study_time = study_time
        self.name = name

    # create getters and setters for each variable:
    
    # courses
    def get_courses(self):
        return self.courses
    
    def set_courses(self, new_courses):
        self.courses = new_courses

    # study time
    def get_study_time(self):
        return self.study_time
    
    def set_study_time(self, new_study_time):
        self.study_time = new_study_time
    
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
    
