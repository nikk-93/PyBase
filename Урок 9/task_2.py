'''
реализовать метакласс. позволяющий создавать
всегда один и тот же объект класса (см. урок)
'''


class TypedMeta(type):

    _instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance


class MyClass(metaclass=TypedMeta):
    pass


mc1 = MyClass()
mc2 = MyClass()

if id(mc1) == id(mc2):
    print("Переменные одной инстанции")
else:
    print("Переменные разных инстанций")
