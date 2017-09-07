class MathDojo(object):
    def __init__(self):
        # self.number1 = number1
        # self.number2 = number2

        self.sum = 0

    def add(self, *number):
        for num in number:
            if isinstance(num, list):
                for n in num:
                    self.sum += n
            else:
                self.sum += num

        # print "--------------added",self.number1,"+",self.number2,"-------------"
        return self


    def subtract(self, *number):
        for num in number:
            if isinstance(num, list):
                for n in num:
                    self.sum -= n
            else:
                self.sum -= num
        # print "--------------Subtracting -",self.number1,"-",self.number2,"-------------"
        return self

    def result(self):
        # print "number1: ",self.number1
        # print " number2:",self.number2
        print "Sum:",self.sum

md = MathDojo()
md.add(1,2)
md.result()
md.add([1,2,2,3,2,1],1).result()
# md.subtract([2,3]).result()
# md.subtract()

# md.result()
