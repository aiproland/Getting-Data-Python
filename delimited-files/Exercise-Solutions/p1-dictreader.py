import csv

with open('dm_office_sales.csv') as f:
    reader = csv.DictReader(f, delimiter=',')
    
    for dict_row in reader:

        division = dict_row["division"]
        LOE = dict_row["level of education"]
        trainigLevel = dict_row["training level"]
        workExperience = dict_row["work experience"]
        salary = dict_row["salary"]
        sales = dict_row["sales"]

        print(division, LOE, trainigLevel, workExperience, salary, sales)