# hardcoded stock prices, like a mini stock market
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 130,
    "MSFT": 310
}

def show_available_stocks():
    print("Available stocks and their prices:")
    for stock, price in stock_prices.items():
        print(f"  {stock}: ${price}")

def get_portfolio():
    portfolio = {}
    num_stocks = int(input("\nHow many different stocks do you want to add? "))

    for i in range(num_stocks):
        stock_name = input("Enter stock symbol (e.g. AAPL): ").upper()

        if stock_name not in stock_prices:
            print("Sorry, that stock isn't in our price list. Skipping it.\n")
            continue

        quantity = int(input(f"How many shares of {stock_name} do you own? "))
        portfolio[stock_name] = quantity

    return portfolio

def calculate_total(portfolio):
    total_value = 0
    print("\n--- Portfolio Summary ---")

    for stock, quantity in portfolio.items():
        price = stock_prices[stock]
        value = price * quantity
        total_value += value
        print(f"{stock}: {quantity} shares x ${price} = ${value}")

    print(f"\nTotal investment value: ${total_value}")
    return total_value

def save_to_file(portfolio, total_value):
    choice = input("\nDo you want to save this summary to a file? (yes/no): ").lower()

    if choice == "yes":
        filename = "portfolio_summary.txt"
        with open(filename, "w") as file:
            file.write("Stock Portfolio Summary\n")
            file.write("------------------------\n")
            for stock, quantity in portfolio.items():
                price = stock_prices[stock]
                value = price * quantity
                file.write(f"{stock}: {quantity} shares x ${price} = ${value}\n")
            file.write(f"\nTotal investment value: ${total_value}\n")

        print(f"Saved! Check the file '{filename}' in your project folder.")

def main():
    print("Welcome to the Stock Portfolio Tracker!\n")
    show_available_stocks()

    portfolio = get_portfolio()

    if not portfolio:
        print("No valid stocks were added. Exiting.")
        return

    total_value = calculate_total(portfolio)
    save_to_file(portfolio, total_value)

main()  