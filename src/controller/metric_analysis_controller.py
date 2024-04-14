from utils.date_utils import get_date_from_user
from model.metric_analysis_model import retrieve_stock_data

def metric_analysis_controller():
    start_date = ""
    end_date = ""

    while start_date == end_date or start_date > end_date:
        stock_label = input("Informe o código do ativo que deseja realizar a análise (Exemplos: ['AAPL', 'MSFT', 'GOOG', 'AMZN']): ").upper()
        start_date = get_date_from_user("Agora, informe uma data de início, no formato 'AAAA-MM-DD':" )
        end_date = get_date_from_user("Agora, informe uma data de fim, no mesmo formato: ")

        if start_date == end_date:
            print("Por favor, informe datas distintas!")
        elif start_date > end_date:
            print("A data de fim não pode preceder a data de início, tente novamente!")

    stock_data = retrieve_stock_data(stock_label, start_date, end_date)

    if stock_data is None or stock_data.empty:
        input(f"A requisição das informações do ativo {stock_label} falhou... Pressione ENTER para voltar ao menu.")
        return (stock_label, stock_data, None, None, None, None)

    daily_returns = stock_data['Adj Close'].pct_change()
    daily_returns.name = "Retorno diário"
    daily_returns_format = daily_returns.map(lambda x: '{:.2%}'.format(x))

    cumulative_returns = (1 + daily_returns).cumprod() - 1
    cumulative_returns.name = "Retorno cumulativo"
    cumulative_returns_format = cumulative_returns.map(lambda x: '{:.2%}'.format(x))

    return (stock_label, stock_data, daily_returns, daily_returns_format[1:], cumulative_returns, cumulative_returns_format[1:])
