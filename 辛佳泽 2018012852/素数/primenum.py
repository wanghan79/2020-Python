class primenum:
    def __init__(self,start,end):
        self.start = start
        self.end = end
    def isPrimeNum(self,k):
        if k<2:
            return False
        for i in range(2,k):
            if k %i ==0:
                return False
        return True
    def __iter__(self):
        for k in range(self.start,self.end):
            if self.isPrimeNum(k):
                yield k
for x in primenum(1,100):
    print(x)
