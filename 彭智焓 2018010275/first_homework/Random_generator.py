#!/usr/bin/env python
'''
@name    :   Random_generator
@Contact :   pengzhihan666@gmail.com
@Created Time      @Author    @Sno
------------      -------    ----------
2020/6/19         ZH.Peng    2018010275
'''
import random
from functools import wraps
class Random_generator(object):
    '''
    This class is a decorated class
    '''
    def __init__(self, datatype, datarange, num, strlen=8, *args):
        '''
        To initialize this class, you need to enter the data type,
        data range, number of data, data length (note that the
        default length is 8), and the data filter criteria
        
        Areas for improvement: self.dict = {int: tuple, float: tuple, str: str}
        '''
        self.datatype = datatype
        self.datarange = datarange
        self.num = num
        self.strlen = strlen
        self.args = args
        self.dict = {int: tuple, float: tuple, str: str} # To quickly return the type of container that stores various data

    def __call__(self, func, *args, **kwargs):
        '''
        Rewrite this function to make it a decorative class
        And then use @wraps # to keep function's own namespace
        '''
        @wraps(func)
        def wrapper(*args, **kwargs):
            res = self.Screening(self.generate(self.datatype, self.datarange, self.num, self.strlen), self.args)
            return func(res, *args, **kwargs)
        return wrapper

    def range_test(self, dtype, drange, kw, n=-1):
        '''
        'dtype' ———— datatype,the type of the data range should be

        The the type of 'drange' should be tuple or string

        'kw' means the type of container the data range should use

        'n' is just a flag, to distinguish between string and other types of data judgment

        This function uses three variables to determine whether
        the input data type and range conform to the input
        specification. If not, an exception is thrown.
        '''
        if isinstance(drange, kw) == False:
            raise Exception("Range's type should be tuple or str!", type(drange))
        if kw is not str:
            #print(len(drange))
            if len(drange) != 2 or drange[1] - drange[0] < 0:
                raise Exception("Range false!")
            if n != -1:
                if dtype is int and drange[1] - drange[0] < n:
                    raise Exception("Num is bigger than range!")

    def Fun_checker(self):
        '''
         Check whether the input data is standard
        '''
        if self.num <= 0:
            raise Exception("num is under 0!")
        if self.strlen <= 0:
            raise Exception("length is under 0!")
        self.range_test(self.datatype, self.datarange, self.dict[self.datatype], self.num)

    def generate(self, datatype, datarange, num, strlen):
        '''
        Generate 'num' int or float data in the range of 'datarange',
        or generate num substring of strlen datarange.
        The generated data is returned in the form of set
        By the way,
        the type of data generated is determined by the 'datatype'

        attention: The generate 'int' or 'float' number is from datarange.
                   If datarange is (a, b), a <= num <= b,so use (a, a),
                   you can specify num = a.
        '''
        try:
            self.Fun_checker()
            ans = set()
            if datatype is int:
                while len(ans) < num:
                    it = iter(datarange)
                    ans.add(random.randint(next(it), next(it)))
            elif datatype is float:
                while len(ans) < num:
                    it = iter(datarange)
                    ans.add(random.uniform(next(it), next(it)))
            elif datatype is str:
                while len(ans) < num:
                    ans.add(''.join(random.sample(datarange, strlen)))
            return ans
        except TypeError:
            print("There is TypeError occurred in dataSampling")
        except MemoryError:
            print("There is MemoryError occurred in dataSampling")
        except Exception as e:
            print(e)
            print('This Error occured in gennerating!')
        finally:
            print("The generated data is:")
            print(ans)

    def Screening(self, ans, condition):
        '''
        'condition' will be a datarange or a series of strings.

        If 'condition' is a range,the function will chose the
        number of 'ans' in range to return.

        If 'condition' is series of strings,it will select
        string from 'ans' that contains these strings from 'condition'.

        At the end of the function, it will return the processing result in the form of set
        '''
        try:
            self.range_test(self.datatype, condition[0], self.dict[self.datatype])
            result = set()
            if self.datatype is int or self.datatype is float:
                for item in ans:
                    fliter = iter(condition[0])
                    if next(fliter) <= item <= next(fliter):
                        result.add(item)
            elif self.datatype is str:
                strcdit = iter(condition)
                for fliter in strcdit:
                    for item in ans:
                        if fliter in item:
                            result.add(item)
            return result

        except TypeError:
            print("There is TypeError occurred in dataScreening")
        except MemoryError:
            print("There is MemoryError occurred in dataScreening")
        except Exception as e:
            print(e)
            print("This Error occurred in dataScreening")
        finally:
            print("The data has been screened!")
