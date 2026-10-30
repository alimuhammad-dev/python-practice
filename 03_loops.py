# orders = [
#     {"id": "A101", "total": 4500, "status": "delivered"},
#     {"id": "A102", "total": 12800, "status": "pending"},
#     {"id": "A103", "total": 2300, "status": "delivered"},
# ]

# pending_count = 0
# for order in orders:
#     if order["status"] == "pending":
#         pending_count += 1
#         print(f"Pending: {order['id']}")

# print(f"{pending_count} order(s) pending")


# arr = [1,2,3,4,5]
# for i in range(len(arr)):
#     print(i, "ali")










# Exercise
# Practice: repeating work with loops
# Five problems, each harder than the last: 1 to 3 are core, 4 and 5 are stretch. Problems 3 to 5 need you to plan before you type: write the steps as comments first, then fill in the code.

# 1. Delivered revenue. Using the same orders list from the demo, write a loop that adds up the totals of the delivered orders only, then prints Delivered revenue: Rs 6,800.

# orders = [
#     {"id": "A101", "total": 4500, "status": "delivered"},
#     {"id": "A102", "total": 12800, "status": "pending"},
#     {"id": "A103", "total": 2300, "status": "delivered"},
# ]

# delivered_revenue = 0
# for order in orders:
#     if order["status"] == "delivered":
#         delivered_revenue += order["total"]
#         print(f"Delivered: {order['id']}")

# print(f"Delivered revenue: Rs {delivered_revenue} ")



# 2. Numbered items. Loop over the prices [850, 1200, 400, 3100, 650] and print each one numbered, as Item 1: Rs 850, Item 2: Rs 1,200 and so on, using a counter variable. At the end, print the total and how many items cost more than Rs 1,000.

# prices = [850, 1200, 400, 3100, 650]

# counter = 0;
# for price in prices:
#     counter += 1
#     print(f"Item {counter}: {price}")

# print(f"Total: {sum(prices)}")

# item_counter= 0;
# for price in prices:
#     if price > 1000:
#       item_counter += 1
# print(f"Number of items costing more then 1000: {item_counter}")



# 3. The biggest order. Using the orders list from the demo, find the order with the highest total without using max(). Keep a "biggest so far" variable and update it inside the loop. Print Biggest order: A102 (Rs 12,800). What happens if two orders have the same highest total?

# orders = [
#     {"customer": "Noor Foods", "total": 4500},
#     {"customer": "Karachi Crafts", "total": 12800},
#     {"customer": "Noor Foods", "total": 2300},
#     {"customer": "Bilal Traders", "total": 7600},
#     {"customer": "Karachi Crafts", "total": 3900},
#     {"customer": "Noor Foods", "total": 6100},
# ]

# biggest_so_far = orders[0]

# for order in orders:
#     if order["total"] > biggest_so_far["total"]:
#         biggest_so_far = order

# print(biggest_so_far) 



# 4. Totals per customer. Starting from this list, build a dictionary that holds each customer's total spend:

# orders = [
#     {"customer": "Noor Foods", "total": 4500},
#     {"customer": "Karachi Crafts", "total": 12800},
#     {"customer": "Noor Foods", "total": 2300},
#     {"customer": "Bilal Traders", "total": 7600},
#     {"customer": "Karachi Crafts", "total": 3900},
#     {"customer": "Noor Foods", "total": 6100},
# ]
# # You need to check whether a customer is already in the dictionary: look up how in works with dictionaries. Then look up the dictionary .items() method and loop over your result to print:

# customer_totals = {}

# for order in orders:
#     customer = order["customer"]
#     total = order["total"]

#     if customer in customer_totals:
#         customer_totals[customer] += total
#     else:
#         customer_totals[customer] = total

# for customer, total in customer_totals.items():
#     print(f"{customer}: Rs {total}")



# 5. Reorder report. For each product below its reorder_level, order enough to bring its stock up to twice the reorder level:

# inventory = [
#     {"name": "Notebook", "stock": 8, "reorder_level": 15, "unit_cost": 90},
#     {"name": "Pen", "stock": 140, "reorder_level": 50, "unit_cost": 25},
#     {"name": "Stapler", "stock": 2, "reorder_level": 5, "unit_cost": 650},
#     {"name": "Marker", "stock": 30, "reorder_level": 30, "unit_cost": 120},
#     {"name": "Folder", "stock": 11, "reorder_level": 20, "unit_cost": 60},
# ]               
# Print one line per product to reorder, such as Reorder 22 x Notebook (Rs 1,980), and finish with the total cost (expected: Rs 8,920). If no product needs reordering, print All stock OK instead. Test that by raising every stock level. Why isn't Marker on the list?


# for product in inventory:
#     if product["stock"] < product["reorder_level"]:
#         target_stock = product["reorder_level"]*2
#         quantity_to_order = target_stock - product["reorder_level"]; 
      
           
#     print(f"Product: {product['name']}")
#     print(f"Order quantity: {quantity_to_order}")
#     print("-----")  

