
import math
# Exercise

# Practice: values, variables and types

# Five problems, each harder than the last. Work in basics.py and check your output against the expected values.

# 1. Delivery charge. A customer, "Karachi Crafts", orders 3 lamps at Rs 2,400 each. Delivery costs Rs 350. Store each value in a variable, then print the order total including delivery. Finally, print the type of your total.

# lamp_cost = 2400;
# delivery_cost = 350;

# total_lamp_cost = 2400*3;
# order_total = total_lamp_cost + delivery_cost;
# print(order_total);



# 2. Sales tax. An order's subtotal is Rs 7,200 and sales tax is 18%. Print the tax amount and the total with tax (expected: 1296.0 and 8496.0). Print the type of the tax amount. Why is it a float when the subtotal was an int?

# subtotal = 7200;
# sales_tax = 18;

# tax_amount = ((subtotal*sales_tax)/100);
# print(tax_amount);
# print(type(tax_amount))

# total_amount= subtotal + tax_amount
# print(total_amount)



# 3. Splitting a bill. Four friends split a Rs 4,750 dinner. Print each person's share using /. Then look up the // and % operators and use them to print how many whole rupees each person pays and how many rupees are left over.

# total_bill = 4750;
# total_persons = 4;

# split_bill_one = total_bill / total_persons
# print(split_bill_one);

# split_bill_two = total_bill // total_persons
# print(split_bill_two);

# print(split_bill_one - split_bill_two)



# # 4. Discount and tax. A phone costs Rs 15,000. Apply a 10% discount, then add 18% tax to the discounted price, and print the final price. Now do it the other way round: tax first, then the discount. Do you get the same answer? Write a comment in your code explaining why or why not.

# phone_cost = 15000;
# discount = 0.1;
# tax = 0.18;

# discount_price= (phone_cost - (phone_cost * discount) );
# print("Discounted price:", discount_price)

# tax_price= (discount_price + (discount_price * tax));
# print("Taxed price:", tax_price)



# 5. Packing boxes. A shop is shipping 23 items, and each box holds 6. Using only arithmetic (no if), print the number of full boxes, the number of items left over, and the total number of boxes needed, including a partly full one (expected: 3, 5 and 4). Each box costs Rs 120 to ship: print the shipping cost. Test your code with 24 items. Does the box count still come out right?

# print("With 23 items")

# total_filled_boxes = 23 // 6
# print("Full boxes:", total_filled_boxes)

# leftover = 23 % 6
# print("Leftover items:", leftover)

# total_boxes = math.ceil(23 / 6)
# print("Total boxes needed:", total_boxes)

# print("Shipping cost:", total_boxes * 120)


# print("\nWith 24 items")

# total_filled_boxes = 24 // 6
# print("Full boxes:", total_filled_boxes)

# leftover = 24 % 6
# print("Leftover items:", leftover)

# total_boxes = math.ceil(24 / 6)
# print("Total boxes needed:", total_boxes)

# print("Shipping cost:", total_boxes * 120)

     



# Practice: working with text

# Five problems, each harder than the last. Some ask you to look up a method you haven't seen yet: search for it in the Python documentation or try it out yourself.

# 1. Clean up a name. A form gave you the name " aMNA rAZA ". Clean it so it reads Amna Raza (look up the .title() method), then print Welcome, Amna Raza! Your name has 9 characters. using an f-string and len().

# name = " aMNA rAZA ";
# title_name = name.title();

# print(f"Welcome, {title_name.strip()} Your name has 9 characters {len(name)}");



# 2. Clean an email. Clean " Ali.Khan@GMAIL.com " so it has no spaces and is all lowercase, then print Email: ali.khan@gmail.com (18 characters).

# email = " Ali.Khan@GMAIL.com "
# print(f"Email: {email.lower()} ({len(email.strip())} characters)")



# 3. A receipt line. The item name is " wireless MOUSE ", the price is 2499 and the quantity is 3. Print exactly: Wireless Mouse x3 = Rs 7,497. Work out the total in code; don't type the number.

# item = "wireless MOUSE";
# price = 2499;
# quantity = 3;

# print(f"{item.title()} x{quantity} = Rs {price}")



# 4. Order codes. Look up the .replace() and .upper() methods. Turn the raw code " ord-2024-0042 " into ORD20240042, then print Order ORD20240042 has 11 characters. Can you do the whole clean-up in one line by chaining methods?

# order_number = " ord-2024-0042 ";
# receipt= order_number.replace("-", "").strip().upper()
# print(f"Order {receipt} has {len(receipt)} characters")



# 5. Usernames. You have first = " bilal ", last = "QURESHI " and city = "lahore". Look up string slicing (for example text[0:3]). Build the username bilal.qureshi_lah (lowercase first name, a dot, lowercase last name, an underscore and the first three letters of the city), then print:

# Welcome, Bilal Qureshi from Lahore!
# Your username is bilal.qureshi_lah (17 characters).
# Change the three starting values to your own name and city, and check it still works.

# first = " ali ";
# last = "SYED ";
# city = "hunza";

# username = (f"{first.strip().lower()}.{last.strip().lower()}_{city[0:3]}")
# print("Welcome, Bilal Qureshi from Lahore!")
# print(f"Your username is {username} ({len(username)} characters)")





# Exercise

# Practice: lists and dictionaries

# Five problems, each harder than the last. Don't use loops yet: you'll learn those in Demo 5.

# 1. A product record. Create a list of three prices: [850, 1200, 400]. Print the last price and the sum of all three. Then create a dictionary for one product with the keys name, price and in_stock. Change in_stock to False and print just the product's name.

# list_prices = [850, 1200, 400];

# print(list_prices[2], sum(list_prices))

# product_details = {
#     "name": "laptop",
#     "price" : 1200,
#     "in_stock" : True
# }
# print(product_details)

# product_details["in_stock"] = False
# print(product_details)



# 2. A week of sales. Store a shop's daily sales for one week in a list: [18500, 22300, 19800, 25400, 31200, 42800, 38600]. Print Monday's and Sunday's sales, the weekly total and the daily average, formatted as Rs with commas and no decimals. Then look up max() and min() and print the best and worst days' sales.


# sales_list = [18500, 22300, 19800, 25400, 31200, 42800, 38600];

# print(f"monday sales: {sales_list[0]}")
# print(f"monday sales: {sales_list[6]}")#

# print(f"Weekly Total: {sum(sales_list)}")
# print(f"Daily Average: {sum(sales_list)//len(sales_list)}")

# print(f"Min: {min(sales_list)}")
# print(f"Max: {max(sales_list)}")



# 3. Stock levels. Create a dictionary of stock counts: {"pens": 120, "notebooks": 45, "staplers": 8}. The shop sells 30 notebooks: update the count by subtracting from the current value, not by typing 15. Add a new product, "markers", with 60 in stock. Print how many products there are (use len()) and then the whole dictionary.



