# my_python_class.py
class MyClass:
    def __init__(self, value=0):
        self.value = value

    def increment(self):
        self.value += 1
        return self.value
