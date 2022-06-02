#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

if __name__ == '__main__':
    li = list(map(int, input("Введите элементы списка: ").split()))
    if not li:
        print("Заданный список пуст", file=sys.stderr)
        exit(1)

    m = 1
    c = 0
    k = 0

    for i, item in enumerate(li):
        if (i + 1) % 2 == 0:
            m *= item

    for i in li:
        if i == 0:
            if k == 1:
                break
            k = 1
            continue
        if k == 1:
            c += i

    li.sort(key=lambda x: x < 0)
    print('Cумма между нулевыми элементами:', c, 'Произведение четных:', m)
    print('Преобразованный список:', li)
