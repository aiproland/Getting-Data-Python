import csv

with open('export_products2.txt', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f, delimiter=',')
    for dict_row in reader:
        pnumber = dict_row["part_number"]
        price = float(dict_row["price"])
        brand = dict_row["manufacturer"]
        print(pnumber, price, brand)