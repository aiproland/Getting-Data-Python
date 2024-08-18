import csv

price_list = {'name': 'price', 'product1': 90.91, 'product2': 41.68, 'product3': 64.5 }

with open('prices.csv', 'w') as f:
    stock = csv.writer(f, delimiter=',')
    for name, price in price_list.items():
        stock.writerow([name, price])