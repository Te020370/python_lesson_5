'''
LIGHT
Необходимо реализовать модуль divisor_master.
Все функции модуля принимают на вход натуральные числа от 1 до 1000. Модуль содержит функции:
'''

print('Task_1: проверка числа на простоту (простые числа - это те числа у которых делители единица и они сами;')

def primes (n): # проверка последовательности на простоту
    list_numbers = list(range(1, n+1))
    print(list_numbers)

    list_primes = [2]
    for i in range(3, n + 1, 2):
        if (i > 10) and (i % 10 == 5):
            continue
        for j in list_primes:
            if j * j - 1 > i:
                list_primes.append(i)
                break
            if (i % j == 0):
                break
        else:
            list_primes.append(i)
    print (list_primes)

#primes(1000)

def primes_one (): #проверка числа на простоту
    n = int(input('Введите число для проверки: '))
    j = 2
    if (n > 10) and (n % 10 == 5):
        print(n, '- составное число')
    if j * j - 1 > n:
        print(n, '- простое число')
    if (n % j == 0):
        print(n, '- составное число')
    else:
        print(n, '- простое число')

#primes_one()

print('Task_2: выводит список всех делителей числа;')
def dividers (n): # выводит список всех делителей всех чисeл из последовательности
    list_numbers = list(range(1, n + 1))
    print(list_numbers)

    for i in range(2, n + 1):
        list_dividers = [1]
        for d in range(2, i + 1):
            if i % d == 0:
                list_dividers.append(d)
            else:
                continue

        print('Список всех делителей числа', i, '- ', list_dividers)

#dividers(1000)

print('Task_3: выводит самый большой простой делитель числа;')
def dividers_big (n):
    list_numbers = list(range(1, n + 1))
    print(list_numbers)

    for i in range(2, n + 1):
        list_dividers = [1]
        for d in range(2, i + 1):
            if i % d == 0:
                list_dividers.append(d)
            else:
                continue
        print(i, '- ', list_dividers)
        list_primes = []
        for i in range(1,len(list_dividers)):
            if list_dividers[i] == 2:
                list_primes.append(list_dividers[i])
                continue
            j = 2
            if (list_dividers[i] > 10) and (list_dividers[i] % 10 == 5):
                continue
            if j * j - 1 > list_dividers[i]:
                continue
            if (list_dividers[i] % j == 0):
                break
            else:
                list_primes.append(list_dividers[i])
        list_primes_1 =str(list_primes[len(list_primes)-1])
        print('Наибольший простой делитель числа', list_dividers[len(list_dividers)-1], ':', list_primes_1)

#dividers_big(48)
if __name__ == '__main__':
    primes(1000)
    primes_one()
    dividers(1000)
    dividers_big(48)