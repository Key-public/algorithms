"""
TODO:
1. Создать произвольный отсортированный массив
2. Создать функцию, принимающую на вход этот массив и произвольное загаданное число
3. В тело функции добавить алгоритм
4. На выходе функция должна возвращать загаданное число (если возможно, иначе возвращать сообщение о том, что число отсутствует в массиве) и количество шагов
"""
sorted_list = {1, 2, 3, 5, 7, 11, 13, 17, 19, 23} # простые числа по возрастанию
the_number = 3
counter = 0
def binarySearch(sorted_list, the_number):
    while check != the_number:
        counter += 1
        check = len(sorted_list) / 2
        if check = 0:
            print("There is no the_number in the array. I found this in", counter,  "tries")
        if sorted_list(check) < the_number:
            sorted_list = sorted_list[:check-1]
        else:
            sorted_list = sorted_list[check+1:]
    print("the_number is", check, ". I found this in", conuter, "tries")
