#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    li = []
    m = 1
    c = 0
    k = 0

    n = int(input('Введите количество чисел в списке: '))
    print('Введите числа в список: ')
    for i in range(n):
        li.append(int(input()))
        if (i+1) % 2 == 0:
            m *= li[i]

    for i in li:
        if i == 0:
            if k == 1:
                break
            k = 1
            continue
        if k == 1:
            c += i

    li.sort(reverse=True)
    print('Cумма между нулевыми элементами:', c, 'Произведение четных:', m)
    print('Преобразованный список:', li)