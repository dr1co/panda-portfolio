import datetime

def get_date_from_user(prompt):
    while True:
        date = input(prompt)
        try:
            date_obj = datetime.datetime.strptime(date, '%Y-%m-%d')
            return date_obj
        except ValueError:
            print("Formato de data inválido. Por favor informe uma data no formato 'AAAA-MM-DD'")
