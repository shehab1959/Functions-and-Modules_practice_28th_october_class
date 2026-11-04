def calculate_final_price(price, tax_rate):
    total = price + price*tax_rate
    print(f"Total: {total}")
    return total
calculate_final_price(price=3000, tax_rate=0.15) #Total: 3450.0
calculate_final_price(tax_rate=0.15, price=3000) #Total: 3450.0