def mul(*x):
    """
    简单连乘程序
    """
    if len(x) == 0:         # None
        raise TypeError     # TypeError
    mul_sum = 1             # normal
    for n in x:
        mul_sum *= n
    return mul_sum


def main():     # test
    print('----------start----------')
    print('mul(5) =', mul(5))
    print('mul(5, 6) =', mul(5, 6))
    print('mul(5, 6, 7) =', mul(5, 6, 7))
    print('mul(5, 6, 7, 9) =', mul(5, 6, 7, 9))

    if mul(5) != 5:
        print('mul(5)测试失败!')
    elif mul(5, 6) != 30:
        print('mul(5, 6)测试失败!')
    elif mul(5, 6, 7) != 210:
        print('mul(5, 6, 7)测试失败!')
    elif mul(5, 6, 7, 9) != 1890:
        print('mul(5, 6, 7, 9)测试失败!')
    else:
        try:
            mul()
            print('mul()测试失败!')
        except TypeError:
            print('-----------end-----------')
            print('测试成功!函数程序正常')


if __name__ == "__main__":
    main()
    