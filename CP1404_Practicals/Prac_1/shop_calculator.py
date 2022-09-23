number_of_items = int(input("Number of items: "))
raw_total_price = 0
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))
for i in range(0, number_of_items, 1):
    current_item_price = int(input("Price of item: "))
    raw_total_price = raw_total_price + current_item_price
if raw_total_price > 100:
    final_price = raw_total_price * 0.9
else:
    final_price = raw_total_price
print("Total price for {:.0f} items is ${:.2f}".format((number_of_items), final_price))
