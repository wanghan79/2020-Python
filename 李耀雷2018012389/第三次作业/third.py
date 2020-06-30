import random
import string

def dataSampling(dataType, dataRange, num, strlen=8):

    try:
        if dataType is int:
            for i in range(0,num):
                j = iter(dataRange)
                temp = random.randint(next(j), next(j))
                yield temp
        elif dataType is float:
            for i in range(0,num):
                j = iter(dataRange)
                temp = random.uniform(next(j), next(j))
                yield temp
        elif dataType is str:
            for i in range(0,num):
                temp = ''.join(random.SystemRandom().choice(dataRange) for _ in range(strlen))
                yield temp
        else:
            pass

    except TypeError:
        print("The Type is error.")
    except MemoryError:
        print("The Memory is error.")
    except ValueError:
        print("The value is not correct")
    except Exception as e:
        print(e)
        print("ERROR")
    else:
        return sum
def dataScreening(data,*args):
    result = set()
    # Screening
    try:
        for item in data:
            if type(item) is int or type(item) is float:
                num = iter(args)
                if next(num) <= item <= next(num):
                    result.add(item)
            elif type(item) is str:
                for substr in args:
                    if substr in item:
                        result.add(item)
    except TypeError:
         print("The Type is error.")
    except MemoryError:
         print("The Memory is error.")
    except ValueError:
         print("The value is not correct")
    except Exception as e:
         print(e)
         print("ERROR")
    else:
         return result


def apply():
        #   int类型
        result_Int = set()
        resultInt = dataSampling(int, (0, 300), 100)
        for i in range(0,100):
            result_Int.add(next(resultInt))
        print("随机生成100个在0~300之间的整数:")
        print(result_Int)
        print("筛选100~200之间的数:")
        new_resultInt = dataScreening(result_Int, 100, 200)
        print(new_resultInt)
        print("===================================================\n")

        #   float类型
        result_Float  = set()
        resultFloat = dataSampling(float, (0.0, 120.0), 100)
        for i in range(0,100):
            result_Float.add(next(resultFloat))
        print("随机生成100个在0~120之间的浮点数:")
        print(resultFloat)
        print("筛选50~100之间的数:")
        new_resultFloat = dataScreening(result_Float, 50.0, 100.0)
        print(new_resultFloat)
        print("===================================================\n")

        #   str类型
        result_Str = set()
        resultStr = dataSampling(str, string.ascii_letters + string.digits, 100, 20)
        for i in range(0,100):
            result_Str.add(next(resultStr))
        print("随机生成100个长度为20的string")
        print(result_Str)
        print("筛选其中包含‘at’的string:")
        new_resultStr = dataScreening(result_Str, 'at')
        print(new_resultStr)
        print("===================================================\n")


apply()
