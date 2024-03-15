import csv 
 
with open('products.csv', encoding='utf8') as file:
    reader = csv.reader(file, delimiter=',') 
    answer = list(reader)[1:] 
    count_class = {} 
    sum_class = {} 
    for Category, product, Date, Price_per_unit, Count, level in answer:
        if 'Хадаров Владмир' in product:
            print(f"с {Date}, продали - {Count}")
        count_class[level] = count_class.get(level, 0) + 1 
        sum_class[level] = sum_class.get(level, 0) + (int(Price_per_unit) if Price_per_unit != 'None' else 0)
 
    for el in answer: 
        if el[-1] == 'None': 
            round(sum_class[el[-2]] / count_class[el[-2]], 3) 
 
with open("products_new.csv", 'w', encoding="utf8", newline='') as file:
    w = csv.writer(file) 
    w.writerow(['Category', 'product', 'Date', 'Price_per_unit', 'Count'])
    w.writerows(answer)