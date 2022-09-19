#권진한 2018125005
from select import select


class Person:
    def __init__(self, name,sex,age):
        self.name=name
        self.sex=sex
        self.age=age
    def set_name(self,name):
        self.name=name
    def set_sex(self,sex):
        self.sex=sex
    def set_age(self,age):
        self.age=age
    def print_info(self):
        print(self.name)
        print(self.sex)
        print(self.age)

a=Person('Jinhan',"M",25)
a.set_age(26)
a.print_info()