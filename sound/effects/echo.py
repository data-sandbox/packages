def func1(a, b):
    return f'echo func1 result: {a + b}'


def func2(a, b):
    return f'echo func2 result: {a - b}'


class ClassName1:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def func1(self):
        self.total = self.a + self.b


if __name__ == "__main__":
    """
    This will run when echo.py is excecuted as script,
    but not when it is imported as a module by other code.
    """
    print("Echo module executed as a script!")
