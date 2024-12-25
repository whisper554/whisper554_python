from functools import reduce


DIGITS = {'0' : 0, '1' : 1, '2' : 2, '3' : 3, '4' : 4, '5' : 5,
          '6' : 6, '7' : 7, '8' : 8, '9' : 9, '.' : '.'}


def str2float(s):
    def f(x, y):
        return x * 10 + y

    s_high, s_low = s.split('.')
    n_high = reduce(f, map(lambda x: DIGITS[x], s_high))
    n_low = reduce(f, map(lambda x: DIGITS[x], s_low)) / (10 ** len(s_low))
    return n_high + n_low


def main():
    print('str2float(\'123.456\') =', str2float('123.456'))
    if abs(str2float('123.456') - 123.456) < 0.00001:
        print('测试成功!')
    else:
        print('测试失败!')


if __name__ == "__main__":
    main()
