import portfolio_calculations, portfolio_structures
from portfolio_loader import PortfolioLoader

def calculate_values_positions(positions):
    try:
        values = list(map(portfolio_calculations.position_value, positions))
        return values
    except OverflowError:
        print("Result of the calculation is too large")

def calculate_portfolio_earnings(positions, actual_prices_dict):
    try:
        earnings = list(map(portfolio_calculations.absolute_earnings, positions, actual_prices_dict))
        return earnings
    except FloatingPointError:
        print("Error when calculating float numbers")

def calculate_portfolio_yield(positions, actual_prices_dict):
    try:
        portfolio_yield = list(map(portfolio_calculations.yield_in_percent, positions, actual_prices_dict))
        return portfolio_yield
    except FloatingPointError:
        print("Error when calculation float numbers")
    except ZeroDivisionError:
        print("Division by 0 is impossible")

def show_results():
    loader = PortfolioLoader()
    portfolio = loader.read_portfolio_json("portfolio_sample.json")
    positions = portfolio_structures.convert_to_positions(portfolio)
    actual_prices = loader.read_portfolio_csv("portfolio_actual_prices_sample.csv")
    positions_real_prices = portfolio_structures.convert_to_positions(actual_prices)
    print(f"values: {calculate_values_positions(positions)}")
    print(f"earnings: {calculate_portfolio_earnings(positions, positions_real_prices)}")
    print(f"yield in percent: {calculate_portfolio_yield(positions_real_prices, positions)}")

if __name__ == "__main__":
    show_results()