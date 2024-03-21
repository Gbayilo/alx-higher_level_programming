#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv

    new_argv = [int(x) for x in argv[1:]]
    print(sum(new_argv))
