def calculate_final_price(price, tax_rate):
    total = price + price*tax_rate
    print(f"Total: {total}")
    return total
calculate_final_price(price=3000, tax_rate=0.15) #Total: 3450.0
calculate_final_price(tax_rate=0.15, price=3000) #Total: 3450.0


##
def send_email(user_email, subject="Welcome!", body="Thanks for joining."):
    print(f"To: {user_email}")
    print(f"Subject: {subject}")
    print(f"Content: {body}")
send_email("support@ostad.com")
