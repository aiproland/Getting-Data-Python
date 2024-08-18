import csv

with open("export_products2.csv", encoding='utf-8-sig') as f:
    mfile = csv.reader(f, delimiter=",")
    next(mfile)
    for row in mfile:
        pnumber = row[0]
        price = row[1]
        manufacturer = row[2]
        print(pnumber, price, manufacturer)


        