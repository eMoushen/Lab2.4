#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    U = []
    D = []
    V = []
    S = []
    days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
    for i, day in enumerate(days):
        print(i, day)

        U.append(int(input('Введите значение утренней температуры: ')))
        D.append(int(input('Введите значение дневной  температуры: ')))
        V.append(int(input('Введите значение вечерней температуры: ')))
        print('\n')

        S.append(int((U[i] + D[i] + V[i])/3))

    sr_temp = 0
    for i in S:
        sr_temp += i
    sr_temp += sr_temp / 7

    print('Средние значения температуры: ', S)
