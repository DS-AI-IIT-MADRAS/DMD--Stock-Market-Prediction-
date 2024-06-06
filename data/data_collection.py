import yfinance as yf

def get_stock_data(ticker, start_date, end_date):
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    return stock_data['Close']

if _name_ == "_main_":
    ticker = 'AAPL'
    start_date = '2020-01-01'
    end_date = '2023-01-01'
    data = get_stock_data(ticker, start_date, end_date)
    data.to_csv(f"../data/{ticker}_data.csv")
