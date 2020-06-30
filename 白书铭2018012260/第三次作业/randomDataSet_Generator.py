"""
Author: ShuMing.Bai
Purpose: Third Homework: Generate random data set by Generator.
Created: 2020.6.17
"""
import random
import string


def dataSampling(dataType, dataRange, num, strLen=8):
    """
    :Description: Generate random data set samples
    :param dataType: type of data generated
    :param dataRange: range of data generated
    :param num: the number of data in set
    :param strLen: maximum length of string( By default,it's 8)
    """
    try:
        if dataType is int:
            for i in range(0, num):
                iran = iter(dataRange)
                item = random.randint(next(iran), next(iran))
                yield item
        elif dataType is float:
            for i in range(0, num):
                iran = iter(dataRange)
                item = random.uniform(next(iran), next(iran))
                yield item
        elif dataType is str:
            for i in range(0, num):
                item = ''.join(random.SystemRandom().choice(dataRange) for _ in range(strLen))
                yield item
        else:
            pass
    except TypeError:
        print("There is TypeError occurred in dataSampling")
    except MemoryError:
        print("There is MemoryError occurred in dataSampling")
    except Exception as e:
        print(str(e))
        print("This Error occurred in dataSampling")
    finally:
        print("dataSampling finally...")


def dataScreening(data, *conditions):  # conditions 为可变参数*args,*args 表示任何多个无名参数，它是一个 tuple
    """
    :Description:This function can generate new data set according to the condition screen old data set
    :param data: Data set to be screened
    :param conditions:Screening conditions
    :return:filtered data set(a new data set)
    """
    result = set()
    try:
        # 判断在int和float类型的情况下，输入的conditions是否满足条件
        for item in data:
            if (type(item) is int or type(item) is float) and len(conditions) > 2:
                print("Warning: There are only two numbers needed for data filtering.The first two numbers are "
                      "used as condition ranges")
                i = iter(conditions)
                if next(i) >= next(i):
                    print("Warning: The filtered set will be empty because the former is larger than the latter")
                else:
                    pass
                break
            else:
                break
        # Screening
        for item in data:
            if type(item) is int or type(item) is float:
                num = iter(conditions)
                if next(num) <= item <= next(num):
                    result.add(item)
            elif type(item) is str:
                for substr in conditions:
                    if substr in item:
                        result.add(item)
            else:
                pass
    except TypeError:
        print("There is TypeError occurred in dataScreening")
    except MemoryError:
        print("There is MemoryError occurred in dataScreening")
    except Exception as e:
        print(str(e))
        print("This Error occurred in dataScreening")
    else:
        return result
    finally:
        print("dataScreening finally...")


def Test():
    #   test: data Type is str
    print("data Type is str:")
    result_Str = set()
    f_Str = dataSampling(str, string.ascii_letters + string.digits, 100, 20)
    while True:
        try:
            result_Str.add(next(f_Str))
        except StopIteration:
            break
    new_resultStr = dataScreening(result_Str, 'at', 'aa', 'a')
    print("resultStr:", result_Str)
    print("new_resultStr:", new_resultStr)
    print("===================================================\n")

    #   test: data Type is int
    print("data Type is int:")
    result_int = set()
    f_int = dataSampling(int, (100, 1000), 100)
    while True:
        try:
            result_int.add(next(f_int))
        except StopIteration:
            break
    new_resultInt = dataScreening(result_int, 200, 600)
    print("resultInt:", result_int)
    print("new_resultInt:", new_resultInt)
    print("===================================================\n")

    #   test: data Type is float
    print("data Type is float:")
    result_Float = set()
    f_float = dataSampling(float, (10.0, 1000.0), 100)
    while True:
        try:
            result_Float.add(next(f_float))
        except StopIteration:
            break
    new_resultFloat = dataScreening(result_Float, 660.0, 888.0)
    print("resultFloat:", result_Float)
    print("new_resultFloat:", new_resultFloat)
    print("===================================================\n")


if __name__ == '__main__':
    Test()
