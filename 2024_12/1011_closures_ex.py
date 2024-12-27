def createCounter():
    num = 0
    def counter():
        nonlocal num
        num += 1
        return num
    return counter


def main():     # test
    counter_a = createCounter()
    print(counter_a(), counter_a(), counter_a(), counter_a(), counter_a())  # 1 2 3 4 5
    counter_b = createCounter()
    if [counter_b(), counter_b(), counter_b(), counter_b()] == [1, 2, 3, 4]:
        print('测试通过!')
    else:
        print('测试失败!')


if __name__ == "__main__":
    main()
