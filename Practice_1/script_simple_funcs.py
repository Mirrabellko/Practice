# 1
def find_max(numbers: list) ->tuple:
    '''
    Необходимо найти максимальное число из массива и его индекс
    :param numbers: list
    :return: tuple max, index
    '''
    max_num = numbers[0]
    max_index = 0
    for i in range(len(numbers)):
        if numbers[i] > max_num:
            max_num = numbers[i]
            max_index = i
    return max_num, max_index

print('Task 1:')
example1 = [1, 88, 75, 15.2, 199, 0]
example2 = [5, 3, 65, 35.2, 349, 88]
example3 = [3, 6, 2, 85.3, -69, 125]

resuilt1 = find_max(example1)
resuilt2 = find_max(example2)
resuilt3 = find_max(example3)

print(resuilt1)
print(resuilt2)
print(resuilt3)

# 2
def invert_numbers(numbers: list, lft_brd=0, rgt_brd= -1) ->list:
    '''
    Инвертировать числа без изменения исходного массива
    :param numbers: list of integers
    :param lft_brd: 0, user can input another value
    :param rgt_brd: -1, user can input another value
    :return: list of inverted numbers
    '''
    result = []
    for i in numbers:
        i = str(i)
        result.append(i[rgt_brd::-1])
    return result

print('Task 2:')
example4 = [25, 158, 8596, 36587]
example5 = [15, 658, 8325, 12387]
example6 = [95, 638, 8544, 37654]

resuilt4 = invert_numbers(example4)
resuilt5 = invert_numbers(example5)
resuilt6 = invert_numbers(example6)

print(resuilt4)
print(resuilt5)
print(resuilt6)

# 3
def summa_elem(numbers: list, serv_func) -> int:
    '''
    Главная функция - сложение элементов, служебная - проверка условия
    :param numbers: list of numbers
    :param serv_func: need to check condition
    :return:
    '''
    result = 0
    for i in numbers:
        if serv_func(i):
            result += i
    return result

def check_num(number: int):
    if number > 20:
        return True

print('Task 3:')
example7 = [55, 21, 0, 8]
example8 = [153, 1111, 87, 2]
example9 = [634, 1, 10, 8]

resuilt7 = summa_elem(example7, check_num)
resuilt8 = summa_elem(example8, check_num)
resuilt9 = summa_elem(example9, check_num)

print(resuilt7)
print(resuilt8)
print(resuilt9)

# 4
def sort_bubble(numbers: list, serv_func) -> list:
    '''
    Главная функция - сортировка пузырьком, служебная - проверка условия
    :param numbers: list of integers
    :param serv_func: check the condition
    :return: new sorted list
    '''
    numbers_copy = numbers.copy()
    if serv_func():
        flag = 1
        while flag == 1:
            flag = 0
            for i in range(1, len(numbers_copy)):
                if numbers_copy[i-1] > numbers_copy[i]:
                    numbers_copy[i], numbers_copy[i-1] = numbers_copy[i-1], numbers_copy[i]
                    flag = 1
    return numbers_copy

def check_cond():
    return True

print('Task 4:')
example10 = [5, 87, 99, 62, 1, 27]
example11 = [23, 67, 12, 32, 41, 76]
example12 = [6, 32, 87, 1, 34, 56]

resuilt10 = sort_bubble(example10, check_cond)
resuilt11 = sort_bubble(example11, check_cond)
resuilt12 = sort_bubble(example12, check_cond)

print(resuilt10)
print(resuilt11)
print(resuilt12)

