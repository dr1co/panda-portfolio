from controller.metric_analysis_controller import metric_analysis_controller
from utils.terminal_utils import clear_terminal
from view.metric_analysis_view import view_important_metrics

def menu():
    while True:
        clear_terminal()
        print('''
Bem vindo ao Panda Portfólio! O que deseja fazer?

1 - Análise métrica de desempenho
2 - Análise de alocação operacional
3 - Análise de risco de uma operação
4 - Análise de cenário

0 - Sair
''')

        option = int(input("Sua opção: "))

        if option == 1:
            clear_terminal()
            (label, data, daily, format_daily, cumulative, format_cumulative) = metric_analysis_controller()

            if (not data.empty):
                view_important_metrics(label, data, daily, format_daily, cumulative, format_cumulative)
            

        elif option == 0:
            print("Obrigado por usar o Panda Portfólio!")
            break
        
        else:
            print("Por favor, digite uma opção válida!")
