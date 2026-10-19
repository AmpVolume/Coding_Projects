print("program stated")

children = 8
adults = 12
seniors = 10

if children < 0 or adults < 0 or seniors < 0:
    print("Error: Number of tickets cannot be negative.")
else:
    child_price = 8.00
    adult_price = 12.00
    senior_price = 10.00

    total_price = (children * child_price) + (adults * adult_price) + (seniors * senior_price)
    print(f"Total ticket price: ${total_price:.2f}")