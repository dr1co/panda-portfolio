import matplotlib.pyplot as plt
from datetime import datetime

def view_important_metrics(label, data, daily_returns, daily_format, cumulative_returns, cumulative_format):
    print(f"Imprimindo informações do ativo {label}...")
    print(data)
    input("Pressione ENTER para continuar")
    print(f"Imprimindo o retorno diário do ativo {label}...")
    print(daily_format)

    input("Pressione ENTER para continuar")
    print(f"Imprimindo o retorno cumulativo do ativo {label} no período estipulado...")
    print(cumulative_format)

    input("Pressione ENTER para continuar")

    total_return = ((daily_returns.iloc[-1] - daily_returns.iloc[1]) / daily_returns.iloc[1])

    if (len(daily_returns) >= 250):
        years = len(daily_returns) / 250
        annualized_return = ((1 + total_return / 100) ** (1 / years) - 1)
    else :
        annualized_return = None

    volatility = daily_returns.std()

    sharpe_ratio = (daily_returns.mean() - 0.02) / volatility

    max_drawdown = (cumulative_returns / cumulative_returns.cummax() - 1).min()
    
    print(f'''Exibindo informações métricas do ativo {label}:
- Retorno total: {'{:.2%}'.format(total_return)}
- Retorno anual: {"Não se aplica" if annualized_return is None else '{:.2%}'.format(annualized_return)}
- Volatilidade: {'{:.2%}'.format(volatility)}
- Razão Sharpe: {'{:.2f}'.format(sharpe_ratio)}
- Perda percentual máxima: {'{:.2%}'.format(max_drawdown)}
''')

    plt.figure(figsize=(10, 6))
    plt.bar(daily_returns.index, daily_returns, label="Retorno diário")
    plt.title(f'Retorno diário do ativo {label}')
    plt.xlabel('Data')
    plt.ylabel('Retorno (%)')
    plt.legend()
    plt.grid(True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    plt.savefig(f"./img_plot/{label}_{timestamp}")

    input("Um gráfico contendo as informações do mercado foi salvo! Pressione ENTER para voltar ao menu")