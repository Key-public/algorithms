"""
TODO:
1. Создать произвольный отсортированный массив
2. Создать функцию, принимающую на вход этот массив и произвольное загаданное число
3. В тело функции добавить алгоритм
4. На выходе функция должна возвращать загаданное число (если возможно, иначе возвращать сообщение о том, что число отсутствует в массиве) и количество шагов
"""


sorted_list = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23] # простые числа по возрастанию
the_number = 5

def binarySearch(array, guess):
    assert type(guess) == int, 'the_number must be integer'
    counter = 1
    check = len(array) // 2
    while array[check] != guess:
        if check == 0:
            print("There is no", the_number, "in the array. I found this with", counter,  "tries")
            return 1
        if array[check] > guess:
            array = array[:check]
        else:
            array = array[check+1:]
        check = len(array) // 2
        counter += 1
    print("It's", array[check], "and I found this with", counter, "tries")
    return 0

binarySearch(sorted_list, the_number)