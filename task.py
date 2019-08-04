"""
Написать три класса:

Human:

-перегрузить конструктор, чтоб объект принимал на вход значения age(типа int)
и ‘name’ (типа str)

-добавить метод say_hello(), который бдует возвращать сообщение ‘hello,
my name is (входящий аргумент name)’.


Отнаследовать от этого класса новый – Builder, пусть он принимает, в дополнение,
не тольо имя и возраст ,но и должность.

-перегрузить у Builder’a метод say_hello(), сделав так ,чтоб после имения шла
еще и должность Строителя.


Отнаследовать от Human еще один класс – Writer.

Добавить ему метод my_books() – этот метод должен принимать неименованные
аргументы типа str,(названия книг Писателя) и возвращать строку «I write
(колличество аргументов(книг))»
"""

class Human:
    def __init__(self, name, age):
        self.name=name
        self.age=age

    def say_hello(self):
        return "hello my name is {}".format(self.name)

class Builder(Human):
    def __init__(self,name, age, position):
        super().__init__(name, age)
        self.pos=position

    def say_hello(self):
        super().say_hello()
        return "my name {} my position {}".format(self.name,self.pos)

class Writer(Human):
    def __init__(self,name,age, *books):
        super().__init__(name, age)
        self.books=books

    def my_books(self):
        return "I write {}".format(self.books)




b=Builder("tom",12,"work")
print(b.say_hello())
w=Writer("Tom",18,"witcher","master and margarita")
print(w.my_books())
print(w.say_hello())

