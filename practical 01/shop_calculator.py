DISCOUNT_NUM = 0.1
num_items = int(input("Number of items: "))
total_price = 0
while num_items < 0:
    print("Invalid number of items!")
    num_items = int(input("Number of items: "))

for i in range(num_items):
    item_price = float(input("Price of item: "))
    total_price = total_price + item_price
if total_price > 100:
    discount = total_price * DISCOUNT_NUM
    total_price = total_price - discount
print(f"Total price for {num_items} items is ${total_price:.2f}")
