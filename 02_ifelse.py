# if else

# age = 18;

# if age > 18:
#     print("You are an Adult")
#     print("You can vote")
# elif age > 12:
#     print("You are a teenager")
# else:
#     print("You are a child")




# 1. Free delivery. Create two variables: total = 6200 and city = "Lahore". Print Free delivery if the total is at least Rs 5,000 and the city is Lahore. Otherwise print Delivery charge: Rs 350.

# total = 6200;
# city = "Lahore";

# if total >= 5000 and city =="Lahore":
#     print("Free delivery")
# else:
#     print("Delivery charges: 350")



# 2. Grades. Given marks, print A for 80 and above, B for 65–79, C for 50–64 and Fail below 50. Test with exactly 80, 79, 50 and 49. Boundary values are where bugs hide.

# marks = 49;

# if marks >= 80:
#     print("A grade")
# elif marks >= 65 and marks <=79:
#     print("B grade")
# elif marks >= 50 and marks <=64:
#     print("C grade")
# elif marks < 50 :
#     print("Fail")
# else:
#     print("wrong input")



# 3. Stock check. Given stock = 12 and quantity, print:

# Invalid quantity if the quantity is 0 or less
# Only 12 left in stock if the quantity is more than the stock
# Confirmed. 7 left after this order otherwise (here, for a quantity of 5)
# Work out every number in the message from the variables.

# stock = 12
# quantity = 5

# if quantity <= 0:
#     print("Invalid quantity")
# elif quantity > stock:
#     print(f"Only {stock} left in stock")
# else:
#     remaining = stock - quantity
#     print(f"Confirmed. {remaining} left after this order")



# 4. Shipping rules. Given weight_kg, order_total and city, work out the shipping charge:

# Orders over Rs 10,000 ship free anywhere.
# Karachi, Lahore and Islamabad: Rs 200 up to 5 kg, Rs 400 above that.
# Every other city: Rs 350 up to 5 kg, Rs 700 above that.
# Customers type the city themselves, so clean city first: " karachi " must count as Karachi. Print Shipping to Karachi: Rs 200. Test at least five combinations, including exactly 5 kg.


# weight_kg = 5
# order_total = 8000
# city = " islamabad "

# # Clean the city name
# city = city.strip().title()

# if order_total > 10000:
#     shipping = 0
# elif city in ["Karachi", "Lahore", "Islamabad"]:
#     if weight_kg <= 5:
#         shipping = 200
#     else:
#         shipping = 400
# else:
#     if weight_kg <= 5:
#         shipping = 350
#     else:
#         shipping = 700

# print(f"Shipping to {city}: Rs {shipping}")



# 5. Ticket triage. A support ticket has a plan ("free", "pro" or "enterprise"), hours_open and a message. Look up how in works with strings (for example "refund" in text). Print its priority:

# Urgent if the plan is enterprise and it has been open more than 4 hours
# High if the message mentions "refund" or "charged twice" in any capitalisation, or the plan is pro and it has been open more than 24 hours
# Normal otherwise
# Check your code against these cases:

# plan	hours_open	message	Expected
# "enterprise"	6	"Login is broken"	Urgent
# "free"	1	"I want a REFUND"	High
# "pro"	30	"Dashboard is slow"	High
# "enterprise"	2	"Question about invoices"	Normal
# An enterprise ticket that has been open 6 hours and asks for a refund should be Urgent. Does your code agree? Write a comment explaining why the order of your checks matters.

# plan = "enterprise"
# hours_open = 6
# message = "I need a REFUND"

# message = message.lower()

# # Check Urgent first because it takes priority over High.
# if plan == "enterprise" and hours_open > 4:
#     priority = "Urgent"
# elif "refund" in message or "charged twice" in message or (plan == "pro" and hours_open > 24):
#     priority = "High"
# else:
#     priority = "Normal"

# print(priority) 