#! usr/bin/python3.7

'''Challenge https://www.hackerrank.com/challenges/grading/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign'''


def gradingStudents():
    grades_count = int(input().strip())
    grades = []
    rounded_grades = []
    for x in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)
    for grade in grades:
        if grade < 38 or grade % 5 < 3:
            rounded_grades.append(grade)
        else:
            rounded_grades.append(grade + 5 -grade % 5)
    return '\n'.join(map(str,rounded_grades))

print(gradingStudents())
