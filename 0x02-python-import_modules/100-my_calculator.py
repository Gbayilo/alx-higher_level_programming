#!/usr/bin/python3

if __name__ == '__main__':
    from calculator_1 import add, sub, mul, div
    import sys
    from sys import argv

    if len(argv) != 4:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        sys.exit(1)
    elif argv[2] != '+' and argv[2] != '-' and argv[2] != '*' and \
            argv[2] != '/':
        print('Unknown operator. Available operators: +, -, * and /')
        sys.exit(1)
    else:
        if argv[2] == '+':
            print('{} + {} = {}'.format(int(argv[1]), int(argv[3]),
                  add(int(argv[1]), int(argv[3]))))
        elif argv[2] == '-':
            print('{} - {} = {}'.format(int(argv[1]), int(argv[3]),
                  sub(int(argv[1]), int(argv[3]))))
        elif argv[2] == '*':
            print('{} * {} = {}'.format(int(argv[1]), int(argv[3]),
                  mul(int(argv[1]), int(argv[3]))))
        else:
            print('{} / {} = {}'.format(int(argv[1]), int(argv[3]),
                  div(int(argv[1]), int(argv[3]))))
