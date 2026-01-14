import csv
sales_data = [
    ['Product', 'Price', 'Quantity', 'Date'],
    ['Laptop', '45000', '5', '2024-01-10'],
    ['Mouse', '500', '20', '2024-01-11'],
    ['Keyboard', '1500', '15', '2024-01-11'],
    ['Monitor', '12000', '8', '2024-01-12'],
    ['Headphones', '2500', '12', '2024-01-12']
]
# Write sample data to CSV
with open('sales_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(sales_data)
# Read and analyze the CSV file
total_revenue = 0
total_items_sold = 0
highest_revenue = 0
best_seller = ''
total_price = 0
product_count = 0
expensive_products = []
with open('sales_data.csv', 'r') as file:
    reader = csv.DictReader(file)
    print(reader.fieldnames)
    for row in reader:
        price= float(row['Price'])
        quantity= int(row['Quantity'])
        revenue= price*quantity
        total_revenue += revenue
        total_items_sold += quantity
        total_price += price
        product_count += 1
        if revenue > highest_revenue:
            highest_revenue = revenue
            best_seller = row['Product']
        if price > 5000:
            expensive_products.append(row)
average_price = total_price / product_count
# Print analysis results
print("Total Revenue: ₹{:,}".format(int(total_revenue)))
print("Best Seller:", best_seller, "(₹{:,})".format(int(highest_revenue)))
print("Total Items Sold:", total_items_sold)
print("Average Price: ₹{:,}".format(int(average_price)))
# Save expensive products to new CSV
with open('expensive_products.csv', 'w', newline='') as file:
    filednames= ['Product', 'Price', 'Quantity', 'Date']
    writer= csv.DictWriter(file, fieldnames=filednames)
    writer.writeheader()
    writer.writerows(expensive_products)
print("Expensive products saved to 'expensive_products.csv'")
