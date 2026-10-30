def apply_discount(total, rate):
    discount = total * rate
    return total - discount

print(apply_discount(12800, 0.1))   # 11520.0 
print(apply_discount(4500, 0.2))    # 3600.0

