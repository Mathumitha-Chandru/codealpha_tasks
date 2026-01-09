#1. Dictionary (Hardcoded Prices)
stock_prices = {
    "RELAIANCE" : 2900,
    "TCS" : 3200,
    "HDFC" : 1500,
    "INFY" : 1400,
    "ZOMATO" : 170,
    "TATAMOTORS" : 900
}

portfolio = []
total_portfolio_value = 0

print("-- Stock Portfolio Tracker --")

#2. Input & Loop (Multiple stocks)
while True:
    name = input("Enter stock name (or 'done' to finish): ").upper()
    if name == 'DONE':
        break

    if name in stock_prices:
        qty = int(input(f"Enter quantity of {name}: "))

        #3. Arthmetic Calculations
        price = stock_prices[name]
        investment = price * qty
        total_portfolio_value += investment

        #To store data
        portfolio.append(f"{name}: {qty} shares at ${price} = ${investment}")
    else:
        print("Stock not found! Try RELAIANCE, TCS, HDFC, INFY, ZOMATO, TATAMOTORS.")

#4. Output
print("\n-- Your Investment Summary --")
for item in portfolio:
    print(item)

print(f"\nGRAND TOTAL INVESTMENT VALUE: ${total_portfolio_value}")

#5. File Handling
with open("my_portfolio.csv", "w") as file:
    file.write("Stock, Quantity, Price, Total\n") #Header
    for item in portfolio:
        file.write(item.replace(":", ",").replace("shares at $", ",").replace(" = $", ",") + "\n")
        file.write(f"\nGrand Total,,,,${total_portfolio_value}")

print("\nSuccess! Your portfolio has been saved to 'my_portfolio.csv'.")
