def stock_portfolio_tracker():
    # 1. Simplified Scope: Hardcoded dictionary for stock prices
    # You can add more stocks here if you like
    stock_prices = {
        "AAPL": 150.00,  # Apple
        "GOOG": 2800.00, # Google
        "TSLA": 750.00,  # Tesla
        "MSFT": 300.00,  # Microsoft
        "AMZN": 3400.00  # Amazon
    }
    
    portfolio = {}
    total_value = 0.0

    print("Welcome to the Stock Portfolio Tracker!")
    print("Available stocks to track:", ", ".join(stock_prices.keys()))
    print("Type 'done' when you are finished adding stocks.\n")

    # 2. Key Concepts: Input loop
    while True:
        ticker = input("Enter Stock Ticker Symbol (e.g., AAPL): ").upper()
        
        if ticker == 'DONE':
            break
        
        if ticker not in stock_prices:
            print(f"Error: '{ticker}' is not in our price list. Please try again.")
            continue
        
        try:
            quantity = int(input(f"Enter quantity for {ticker}: "))
            if quantity < 0:
                print("Quantity cannot be negative.")
                continue
                
            # Add to portfolio dictionary
            if ticker in portfolio:
                portfolio[ticker] += quantity
            else:
                portfolio[ticker] = quantity
                
        except ValueError:
            print("Invalid input. Please enter a whole number for quantity.")

    # 3. Key Concepts: Calculation & Output
    print("\n--- Portfolio Summary ---")
    summary_lines = ["--- Portfolio Summary ---"] # List to store lines for the file
    
    for stock, shares in portfolio.items():
        price = stock_prices[stock]
        value = shares * price
        total_value += value
        
        line = f"{stock}: {shares} shares @ ${price} = ${value:.2f}"
        print(line)
        summary_lines.append(line)

    total_line = f"\nTotal Portfolio Value: ${total_value:.2f}"
    print(total_line)
    summary_lines.append(total_line)

    # 4. Key Concepts: File Handling (Saving to .txt)
    try:
        with open("portfolio_summary.txt", "w") as file:
            for line in summary_lines:
                file.write(line + "\n")
        print("\nSuccess: Portfolio saved to 'portfolio_summary.txt'")
    except IOError:
        print("\nError: Could not save file.")

if __name__ == "__main__":
    stock_portfolio_tracker()