from user import User
import random

class Teacher(User):
    '''Class "Teacher" in teacher.py'''

    knowledge = [
        "str is a data type in Python",
        "programming is hard, but it's worth it",
        "JavaScript async web request",
        "Python function call definition",
        "object-oriented teacher instance",
        "programming computers hacking learning terminal",
        "pipenv install pipenv shell",
        "pytest -x flag to fail fast",
    ]

    def __init__(self, first_name, last_name):
        '''initializes with first and last name'''
        super().__init__(first_name, last_name)

    def teach(self):
        '''returns a random element from self.knowledge'''
        return random.choice(self.knowledge)