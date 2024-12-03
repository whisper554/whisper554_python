def findMinAndMax(lst):
    if len(lst) == 0:
         return None, None
    else:
         return min(lst), max(lst)


def main():     # test
    if findMinAndMax([]) != (None, None):
        print('测试失败!')
    elif findMinAndMax([7]) != (7, 7):
        print('测试失败!')
    elif findMinAndMax([7, 1]) != (1, 7):
        print('测试失败!')
    elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
        print('测试失败!')
    else:
        print('测试成功!')


if __name__ == "__main__":
    main()