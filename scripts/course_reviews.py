# Change the file paths and name as required
import pandas as pd
from datetime import datetime
import re

def get_course_code(course_name):
    pattern = r'^[A-Za-z]+\s*\d+'
    match = re.search(pattern, course_name)
    if match:
        return match.group().strip()
    else:
        return None
    
def get_first_name(full_name):
    first_name = full_name.split()[0]
    return first_name

current_date = datetime.now().date()
formatted_date = current_date.strftime('%Y-%m-%d')

def read_course_reviews():
    # Reading the CourseReviews.csv file
    df = pd.read_csv("course_reviews.csv")
    return df.to_dict(orient="records")

def generate_readme_file(course_data):
    for course in course_data:
        readme_content = f"""---
layout: post
title: "{course['Name of the Course:']}"
categories: [core courses]
tags: [courses]
image: assets/images/Course Reviews/Electives/US607.jpg
featured: false
hidden: false
---

#### Instructor
{course['Name of the Instructor:']}

#### Semester
{course['Semester/Year']}

#### Course Difficulty
{course['Course Difficulty:']}

#### Time Commitment Required
{course['Time commitment needed:']}

#### Grading Policy and Statistics
{course['Grading Statistics:']}

#### Attendance Policy
{course['Attendance Policy:']}

#### Pre-requisites
Not for B.Tech students 

#### Topics Covered in the Course
{course['Broad topics covered in the course:']}

#### Teaching Style
{course['Teaching Style:']}

#### Tutorials/Assignments/Projects
{course['Evaluation Scheme:']}

{course['Feedback on Assignments/ Tutorials/ Projects']}

#### Feedback on Exams
{course['Feedback on Exams (Written Evaluation):']}

#### Motivation for Taking This Course
{course['Future Tracks:']}

{course['Course Importance:']}

{course['Additional Details:']}

Review By: {course['Name:']}
"""

        course_code = get_course_code(course['Name of the Course:'])
        first_name = get_first_name(course['Name:'])
        with open(f"{formatted_date}-{course_code}_{first_name}.md", "w") as readme_file:
            readme_file.write(readme_content)

if __name__ == "__main__":
    course_data = read_course_reviews()
    generate_readme_file(course_data)
