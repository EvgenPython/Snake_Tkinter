# from random import choice
#
#
# class RandomSample:
#
#     def __init__(self, a, b):
#         self.__a = a
#         self.__b = b
#
#     def __operation(self):
#         oper = choice("+-*/")
#         if oper == "+":
#             return self.__a - self.__b
#         elif oper == "-":
#             return self.__a + self.__b
#         elif oper == "*":
#             return self.__a / self.__b
#         elif oper == "/":
#             return self.__a * self.__b
#
#     def get_result(self):
#         return self.__operation()
#
#
# r = RandomSample(2, 5)
# print(r.get_result())

class GranParent:
    def __init__(self, age):
        self.age = age


class Parent(GranParent):
    def __init__(self, work):
        super().__init__(self.age)
        self.work = work


class Children(Parent):
    def __init__(self, game):
        super().__init__(self.work)
        self.game = game


ch = Children()
