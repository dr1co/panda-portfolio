import yfinance as yf

def retrieve_stock_data(label, start_date, end_date):
    data = yf.download(label, start=start_date, end=end_date)

    return data
