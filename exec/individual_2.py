#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    first_dict = {3: 'tree',
                2: 'two',
                1: 'one'}
    second_dict = dict(map(reversed, first_dict.items()))
    print(first_dict.items())
    print(second_dict.items())
    