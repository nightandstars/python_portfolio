from collections import namedtuple

from portfolio_loader import PortfolioLoader

Position = namedtuple("Position", ["symbol", "quantity", "purchase_price", "purchase_date"])
Transaction = namedtuple("Transaction", ["date", "symbol", "quantity", "price", "type"])

def convert_to_positions(portfolio_dict):
    try:
        file_type = type(portfolio_dict)
        data = []
        if file_type == dict:
            position_data = portfolio_dict["positions"]
            for item in position_data:
                data.append(Position(**item))
        else:
            next(portfolio_dict)
            for row in portfolio_dict:
                data.append(Position(
                    symbol = row[0],
                    quantity = int(row[1]),
                    purchase_price = float(row[2]),
                    purchase_date = row[3]
                ))
        return data
    except KeyError:
        print("Could not find the specified key in the json file")
    except IndexError:
        print("Incorrect index")

def show_positions(positions):
    for position in positions:
        print(f"symbol: {position.symbol}, quantity: {position.quantity}, purchase price: {position.purchase_price}, date purchased: {position.purchase_date}")

if __name__ == "__main__":
    loader = PortfolioLoader()
    portfolio = loader.read_portfolio_json("portfolio_sample.json")
    conversion = convert_to_positions(portfolio)
    show_positions(conversion)