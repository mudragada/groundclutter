

class BaseClass():
    def method1(self):
        print("myBaseClass method1", type(self))
    def method2(self, str):
        print("myBaseClass method2", str, type(self))

# Inheritance
class DerivedClass(BaseClass):
    def method1(self):
        print("myDerivedClass method1", type(self))

    def method2(self, str):
        if (str == "Mudragada"):
            BaseClass.method2(self, str)
        else:
            print("myDerivedClass method2", type(self))

def main():
    c = BaseClass()
    c.method1()
    c.method2("Krishna")
    d = DerivedClass()
    d.method1()
    d.method2("Krishna")
    d.method2("Mudragada")

if __name__ == "__main__":
    main()
