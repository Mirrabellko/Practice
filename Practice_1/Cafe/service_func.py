def get_data_from_file(file_name: str) -> dict:
    '''
    Allow to get data from file.
    make_path() make a correct path
    make_list() make a list of data
    make_dict() make a dictionary
    :param file_name: str, file format - csv
    :return: list of data
    '''
    path = make_path(file_name)
    with open(path, 'r', encoding='utf8') as file:
        data = file.read()
    data = make_list(data)
    dict = make_dict(data)
    return dict


def make_dict(data:list) -> dict:
    '''
    Service func, use list make dict
    :param data: list of data
    :return: dictionary of data
    '''
    data_dict = {}
    for i in data[1:-1]:
        buf = i.split(',')
        data_dict[buf[0]] = buf[1:len(i)]
    return data_dict


def make_path(file_name:str) ->str:
    '''
    Service func help to get correct path
    :param file_name: str
    :return: str
    '''
    path = ''
    if file_name[-4:] == '.csv':
        path += file_name
    else:
        path = file_name + '.csv'
    return path


def make_list(data:str) ->list:
    '''
    Use str make a list of data
    :param data: str
    :return: list of data
    '''
    data = data.split('\n')
    for i in data:
        i = i.split(',')
    return data

def total_amount(data_dict: dict) -> float:
    '''
    Count total amount for last year
    :param data_dict: dict
    :return: float
    '''
    total = 0
    for key in data_dict:
        for value in data_dict[key]:
            total += float(value)
    return total


def next_total_amount(trend_list: list, months: int) -> float:
    '''
    Count total amount for next year
    :param trend_list: list
    :param months: int
    :return: float
    '''
    total = 0
    for i in trend_list:
        total += i[1]
    return total


def record_to_file(report: str):
    '''
    Save final report as file .txt
    :param report: final version str
    :return: None
    '''
    path = 'cafe_expenses_extended_report.txt'
    with open(path, 'w') as file:
        file.write(report)