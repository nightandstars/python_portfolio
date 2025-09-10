import csv, json, pathlib

class PortfolioLoader:

    def read_portfolio_csv(self, filename):
        try:
            return csv.reader(open(filename))
        except FileNotFoundError:
            print(f"Could not locate {filename}")

    def read_portfolio_json(self, filename):
        try:
            return json.load(open(filename))
        except FileNotFoundError:
            print(f"Could not locate {filename}")

    def show_portfolio(self, filename):
        try:
            file_extension = self.determine_file_extension(filename)
            if file_extension == ".csv":
                portfolio = self.read_portfolio_csv(filename)
                for row in portfolio:
                    print(", ".join(row))
            if file_extension == ".json":
                portfolio = self.read_portfolio_json(filename)
                for i in portfolio["positions"]:
                    print(i)
        except KeyError:
            print("Could not find the specified key in the json file")

    def save_portfolio(self, portfolio, filename):
        try:
            file_extension = self.determine_file_extension(filename)
            if file_extension == ".csv":
                csv.writer(filename).writerows(portfolio)
            if file_extension == ".json":
                json.dump(portfolio, filename)
        except FileNotFoundError:
            print(f"Could not locate {filename}")

    def determine_file_extension(self, filename):
        return pathlib.Path(filename).suffix

if __name__ == "__main__":
    loader = PortfolioLoader()
    loader.show_portfolio("portfolio_sample.json")