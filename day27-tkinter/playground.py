# def add(*args):
#     sum = 0
#     for n in args:
#         sum += n
#     print(sum)
    
    
# add(1,2,2,3,3,4)

def calculate(n,**kwargs):
    print(kwargs)
    # for key,value in kwargs.items():
    #     print(key)
    #     print(value)
    
    
calculate(3,add = 4,multiply = 2)


class car:
    def __init__(self,**kw):
        self.make = kw["make"]
        self.model = kw["model"]
        
my_car = car(make = "Nissan",model = "GT-R-R35")
print(my_car.make)


# def all_aboard(a, *args, **kw):
#     print(a, args, kw)
    
# all_aboard(4, 7, 3, 0, x=10, y=64)
