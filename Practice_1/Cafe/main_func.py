import service_func as sf


def get_trend(data_dict: dict, months:int = 12) ->list:
    '''
    Calculating the average of every category.
    trend_analize() is a service func
    :param data_dict: dict of data
    :param months: default - 12 months. Can ba changed
    :return: list of data "category, average, comment"
    '''
    trend_list = []
    comment = ''
    for key in data_dict:
        summa = 0
        for j in data_dict[key]:
            summa += float(j)
        average = summa / months
        last_month = float(data_dict[key][months-1])
        prev_month = float(data_dict[key][months-2])

        if average > last_month and average > prev_month:
            comment = 'возрастает'
        elif average == last_month and average == prev_month:
            comment = 'стабильный'
        elif average < last_month and average < prev_month:
            comment = 'убывает'
        trend_list.append([key, average, comment])
    return trend_list


def report(trend_list: list,total: float, next_total: float, months: int = 12):
    report_str = ''
    report_str += f'Углубленный отчет о расходах кафе за последние {months} месяцев \n'
    report_str += '-------\n'
    report_str += f'Общие расходы: {total} руб.\n'
    report_str += '-------\n'
    for i in trend_list:
        report_str += f'Средние расходы по категории {i[0]}: {round(i[1])}.\nТренд расходов {i[2]} по категории {i[0]}; \n'
        report_str += '-------\n'
    report_str += f'Прогнозируемые расходы на следующий год: {round(next_total)} руб.'
    return report_str


def main_loop():
    data_dict = sf.get_data_from_file('cafe_expenses_extended')
    trend_list = get_trend(data_dict)
    total = sf.total_amount(data_dict)
    next_total = sf.next_total_amount(trend_list, 12)
    final_report = report(trend_list, total, next_total)
    sf.record_to_file(final_report)
