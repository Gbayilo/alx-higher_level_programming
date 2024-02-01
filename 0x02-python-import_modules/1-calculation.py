#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1

    a = 10
    b = 5

    add_result = calculator_1.add(a, b)
    print('{:d} + {:d} = {:d}'.format(a, b, add_result))

    sub_result = calculator_1.sub(a, b)
    print('{:d} - {:d} = {:d}'.format(a, b, sub_result))

    mul_result = calculator_1.mul(a, b)
    print('{:d} * {:d} = {:d}'.format(a, b, mul_result))

    div_result = calculator_1.div(a, b)
    print('{:d} / {:d} = {:d}'.format(a, b, div_result))
