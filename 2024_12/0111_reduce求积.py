from functools import reduce


def prod(L):
    def multiply(x, y):
        return x * y
    return reduce(multiply, L)


def main(): # test
    print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
    if prod([3, 5, 7, 9]) == 945:
        print('测试成功!')
    else:
        print('测试失败!')


if __name__ == "__main__":
    main()
