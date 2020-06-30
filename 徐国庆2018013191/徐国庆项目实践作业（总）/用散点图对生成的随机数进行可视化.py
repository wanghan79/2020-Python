"""
    Author: GQ.Xu
    Purpose:Visual operation of generated random number
    Creat:29/6/2020
"""

import random
import string
import traceback
from iserror import IsError as ie
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif']='SimHei'
plt.rcParams['axes.unicode_minus']=False
from error import DatatypeError, DatarangeError, NumError, StrlenError, RangeError


#dataSampling函数的异常生成函数
def DataError(datatype, datarange, num, strlen):
    '''
    dataSampling函数的异常生成函数
    :param datatype:Type of random data
    :param datarange:
    :param num:Random number
    :param strlen:length of string
    :return: a data set
    '''
    if ie('Type', datatype, (int, str, float)).ErrorSelection():
        raise DatatypeError(datatype)
    if ie('Iter', datarange).ErrorSelection():
        raise DatarangeError(datarange)
    if ie('Range', datarange).ErrorSelection():
        raise RangeError
    if type(num) is not int:
        raise NumError
    if type(strlen) is not int:
        raise StrlenError


def dataSampling(datatype, datarange, num, strlen=8):
    '''

    :param datatype:Type of random data
    :param datarange:range of data
    :param num:Random number
    :param strlen:length of string
    :return: a data set
    '''
    try:
        result = set()
        DataError(datatype, datarange, num, strlen)
        if datatype is int:
            while len(result) != num:
                it = iter(datarange)
                item = random.randint(next(it), next(it))
                result.add(item)
        elif datatype is float:
            while len(result) != num:
                it = iter(datarange)
                item = random.uniform(next(it), next(it))
                result.add(item)
        elif datatype is str:
            while len(result) != num:
                item = ''.join(random.choice(datarange) for _ in range(strlen))
                result.add(item)
        else:
            pass
        return result
    except DatatypeError as e:
        print("Type", e.datatype, "is not include")
    except DatarangeError as e:
        print("Datarange can't be iterated.   Datarange:", e.datarange)
    except NumError:
        print("num'type must be 'int'")
    except StrlenError:
        print("strlen'type must be 'int'")
    except ValueError as e:
        print(e)
    except MemoryError as e:
        print(e)
    except TypeError as e:
        print(e)
    except Exception as e:
        print(e)
        traceback.print_exc()


def dataScreening(data, datatype, *condition):
    '''

    :param data:Iterative random data type
    :param condition:
    if type of the values in data is 'int' or 'float':
        condition[0] uses '[]','()','(]' and '[)' to represent the opening or closing condition of the section
        condition[1] is a tuple which represents the upper and lower boundaries of data
    if type of the values in data is 'str':
        conditions means substrings of string
    :return:Filter results
    '''
    try:
        if ie('Iter', data).ErrorSelection():
            raise DatarangeError(data)
        result = set()
        if datatype is int or datatype is float:
            section = condition[0]
            datarange = condition[1]
            for value in data:
                if section == '[]' and value >= datarange[0] and value <= datarange[1]:
                    result.add(value)
                if section == '()' and value > datarange[0] and value < datarange[1]:
                    result.add(value)
                if section == '(]' and value > datarange[0] and value <= datarange[1]:
                    result.add(value)
                if section == '[)' and value >= datarange[0] and value < datarange[1]:
                    result.add(value)
        if datatype is str:
            substrings = condition
            for value in data:
                for substring in substrings:
                    if substring in value:
                        result.add(value)
        return result
    except DatarangeError as e:
        print("Type", e.datatype, "is not include")
    except ValueError as e:
        print(e)
    except MemoryError as e:
        print(e)
    except TypeError as e:
        print(e)
    except Exception as e:
        print(e)
        traceback.print_exc()

#对生成的浮点型数据进行可视化：
# 生成500个1~100内的随机浮点数，并筛选其中大于20小于等于60的数，用散点图表示出来
result = dataSampling(float, (1, 100), 500)
result_2 = dataScreening(result, float, '(]', (20, 60))
#对生成的浮点数进行可视化
x1 = range(1, 501, 1)
y1 = list(result)
color = np.random.random(1500).reshape(500, 3)
size = np.random.randint(0, 100, 500)
plt.scatter(x1, y1, color=color, s=size, alpha=0.5)
plt.xlabel('500个随机浮点数散点分布')
plt.show()
#对筛选后的数据进行可视化
x2 = range(1, len(result_2)+1, 1)
y2 = list(result_2)
color = np.random.random(3*len(result_2)).reshape(len(result_2), 3)
size = np.random.randint(0, 100, len(result_2))
plt.scatter(x2, y2, color=color, s=size, alpha=0.5)
plt.xlabel('筛选后的浮点数散点分布')
plt.show()

