import csv

score_list = {'name': 'score', 'student1': 90, 'student2': 54, 'student3': 87 }

with open('math_scores.csv', 'w') as f:
    record = csv.writer(f, delimiter=',')
    for gender, age in score_list.items():
        record.writerow([gender, age])