import re
from datetime import datetime

def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(pattern, email))

def format_date(date_str):
    return datetime.strptime(date_str, '%Y-%m-%d').strftime('%Y-%m-%d')

def log_action(func):
    def wrapper(*args, **kwargs):
        print(f"Executing {func.__name__} at {datetime.now()}")
        result = func(*args, **kwargs)
        return result
    return wrapper

@log_action
def recursive_count_skills(skills, index=0):
    if index >= len(skills):
        return 0
    return 1 + recursive_count_skills(skills, index + 1)

def apply_function(func, data):
    return func(data)