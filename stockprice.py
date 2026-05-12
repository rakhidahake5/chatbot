# Stock Portfolio Tracker

# Hardcoded dictionary of stock prices (in USD)
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "MSFT": 320,
    "AMZN": 130
}

portfolio = {}  # to store user input
total_investment = 0

print(" Stock Portfolio Tracker")
print("Enter stock name and quantity (type 'done' to finish):")

while True:
    stock = input("Stock name: ").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print(" Stock not found in price list.")
        continue
    try:
        quantity = int(input("Quantity: "))
        portfolio[stock] = quantity
    except ValueError:
        print(" Please enter a valid number.")

# Calculate total investment
for stock, qty in portfolio.items():
    investment = stock_prices[stock] * qty
    total_investment += investment
    print(f"{stock}: {qty}  ${stock_prices[stock]} = ${investment}")

print(f"\n Total Investment Value: ${total_investment}")

# Optional: Save to file
save_choice = input("Do you want to save the result to a file? (yes/no): ").lower()
if save_choice == "yes":
    with open("portfolio_summary.txt", "w") as file:
        file.write("Stock Portfolio Summary\n")
        file.write("-----------------------\n")
        for stock, qty in portfolio.items():
            file.write(f"{stock}: {qty}  ${stock_prices[stock]} = ${stock_prices[stock]*qty}\n")
        file.write(f"\nTotal Investment Value: ${total_investment}\n")
    print(" Portfolio saved to 'portfolio_summary.txt'")

