import pandas as pd

def preprocess_input(data):
    # Map 'CourseCategory' to numerical values
    data['CourseCategory'] = data['CourseCategory'].map({
        "Business": 0,
        "Health": 1,
        "Science": 2,
        "Programming": 3,
        "Arts": 4
    })
    return data
