class parent:
    def func(self):
        print("Parent class function")
    

class child1(parent):
    def func(self):
        print("Child 1 class function")

class child2(parent):
    def func(self):
        print("Child 2 class function")

class cj(child1,child2):
    pass

obj1 = parent()
obj1.func()

obj2 = child1()
obj2.func()

obj3 = child2()
obj3.func()

obj4 = cj()
obj4.func()



