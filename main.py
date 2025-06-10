class Base:
    def __new__(cls, *args, **kwargs):
        print("[Base] 🟡 __new__ called")
        instance = super().__new__(cls)
        instance.CONSTANT = "I am constant"
        return instance

    def __init__(self, name):
        print("[Base] 🔵 __init__ called")
        self.name = name

    def __del__(self):
        print(f"[Base] 🔴 __del__ called for {self.name}")

class Child(Base):
    def __new__(cls, *args, **kwargs):
        print("[Child] 🟡 __new__ called")
        instance = super().__new__(cls, *args, **kwargs)
        return instance

    def __init__(self, name, age):
        print("[Child] 🔵 __init__ called")
        super().__init__(name)  # Вызываем родительский __init__ но это не обязательно
        self.age = age

    def __del__(self):
        print(f"[Child] 🔴 __del__ called for {self.name}")
        super().__del__()

print("Создаём объект:")
obj = Child("Buddy", 5)

print("\nДоступ к атрибутам:")
print("obj.name =", obj.name)
print("obj.age =", obj.age)
print("obj.CONSTANT =", obj.CONSTANT)

print("\nУдаляем объект:")
del obj
