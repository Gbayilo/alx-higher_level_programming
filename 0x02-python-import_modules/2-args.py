#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv

    if len(argv) - 1 == 0:
        print('0 arguments.')
    elif len(argv) - 1 == 1:
        print('1 argument:')
        print('1:', argv[1])
    else:
        print(len(argv) - 1, 'arguments:')
        count = 1
        while count < len(argv):
            print('{}: {}'.format(count, argv[count]))
            count += 1
