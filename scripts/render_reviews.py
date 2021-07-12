# Replace relevant file and folder paths as needed.

import pandas as pd
import os

def clean_prof_name(prof):
    prof = prof.split(",")[0].lower()
    replace_strs = ["professor", "prof", "."]
    for s in replace_strs:
        prof = prof.replace(s, "")
    prof = prof.split()[0]
    return prof

def get_file_name(row):
    date = pd.to_datetime('today').strftime("%Y-%m-%d")
    code = row['Course Code']
    prof = clean_prof_name(row['Instructor'])
    return f"{date}-{code}_{prof}.md"

def get_item(row, idx):
    content = row[idx].replace("\n", "  \n")
    return f'\n#### {idx}\n{content}\n'
    
def get_review(row):
    keys = list(row.index)[3:]
    
    review = f'''---
layout: post
title: "{row['Course Code']} - {row['Course Name']}"
categories: [core courses]
tags: [courses]
image: assets/images/Course Reviews/Core/ce102.png
featured: false
hidden: false
---
'''
    
    for key in keys:
        if pd.isnull(row[key]):
            continue
        review += get_item(row, key)
    
    review += f"\n*Review By:* {row['Name']}" 
    return review

def generate_reviews(df, save_folder):
    for i, row in df.iterrows():
        file_name = get_file_name(row)
        with open(os.path.join(save_folder, file_name), 'w', encoding='utf8') as f:
            f.write(get_review(row))


if __name__ == "__main__":
    ### Core Courses

    cols = ['Name', 'Course Code', 'Course Name', 'Professor(s)', 'Section', 'Semester', 'Course Difficulty.1','Time commitment required',
            'Grading Policy and Statistics', 'Attendance Policy', 'Prerequisites (also if any skill / knowledge that would impart an advantage)',
    'Evaluation Scheme / Weightages', 'Course Contents (in brief)', 'Mechanism of Instruction and Teaching Style',
    'Feedback on Tutorials/Assignments/Projects etc.', 'Feedback on Exams', 'Highlights of the course',
    'Comments on Course Importance', 'Going Forward', 'References Used', 'Other Remarks', 'Interesting relevant links']
    new_cols = ['Name', 'Course Code', 'Course Name', 'Instructor', 'Section', 'Semester', 'Course Difficulty', 'Time Commitment Required',
        'Grading Policy and Statistics', 'Attendance Policy', 'Pre-requisites', 'Evaluation Scheme',
        'Topics Covered in the Course', 'Teaching Style', 'Tutorials/Assignments/Projects', 'Feedback on Exams',
        'Course Highlights', 'Course Importance', 'Going Forward', 'References Used', 'Other Remarks', 'Interesting relevant links']
    assert len(cols) == len(new_cols)

    df = pd.read_csv(r"C:\Users\shubh\Downloads\core.csv")
    df = df[cols]
    df.columns = new_cols 
    df["Course Code"] = df["Course Code"].apply(lambda x: x.replace(" ", ""))

    save_folder = r"C:\Users\shubh\Downloads\reviews\core"
    generate_reviews(df, save_folder)

    ### Electives

    cols = ['Name', 'Course Code', 'Course Name', 'Professor(s)', 'Semester', 'Course Difficulty.1',
            'Time commitment required', 'Grading Policy and Statistics', 'Attendance Policy',
            'Prerequisites (also if any skill / knowledge that would impart an advantage)',
            'Evaluation Scheme / Weightages', 'Course Contents (in brief)',
            'Mechanism of Instruction and Teaching Style', 'Feedback on Tutorials/Assignments/Projects etc.',
            'Feedback on Exams', 'Motivation for taking this course', 'Highlights of the course',
            'Comments on Course Importance', 'How strongly would you recommend others to take this course? ',
            'When did you take this course? What will be the ideal semester for taking this course? ',
            'Going Forward', 'References Used', 'Other Remarks', 'Interesting relevant links']
    new_cols = ['Name', 'Course Code', 'Course Name', 'Instructor', 'Semester', 'Course Difficulty', 'Time Commitment Required',
        'Grading Policy and Statistics', 'Attendance Policy', 'Pre-requisites', 'Evaluation Scheme',
        'Topics Covered in the Course', 'Teaching Style', 'Tutorials/Assignments/Projects', 'Feedback on Exams', 
        'Motivation for taking this course', 'Course Highlights', 'Course Importance', 'How strongly would I recommend this course?',
                'When to take this course?',  'Going Forward', 'References Used', 'Other Remarks', 'Interesting relevant links']
    assert len(cols) == len(new_cols)

    df = pd.read_csv(r"C:\Users\shubh\Downloads\electives.csv")
    df = df[cols]
    df.columns = new_cols 
    df["Course Code"] = df["Course Code"].apply(lambda x: x.replace(" ", ""))

    save_folder = r"C:\Users\shubh\Downloads\reviews\electives"
    generate_reviews(df, save_folder)