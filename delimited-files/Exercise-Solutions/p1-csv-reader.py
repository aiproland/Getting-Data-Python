import csv

with open("dm_office_sales.csv") as f:
    mfile = csv.reader(f, delimiter=",")
    # next(mfile)
    for row in mfile:
        division = row[0]
        LOE = row[1]
        trainigLevel = row[2]
        workExperience = row[3]
        salary = row[4]
        sales = row[5]
        print(division, LOE, trainigLevel, workExperience, salary, sales)
