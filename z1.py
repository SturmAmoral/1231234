import csv

with open('products.csv', encoding="utf8") as file:
    reader = csv.reader(file, delimiter=',')
    answer = list(reader)[1:]
    for Category, product, Date, Price_per_unit, Count in answer:
        print({Date})