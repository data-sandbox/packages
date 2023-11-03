# One approach to managing package imports
from sound.effects import echo
from sound.filters import equalizer

# Alternative approach (not recommended for production):
# from sound.effects import *
# from sound.filters import *

# Yet another alternative:
# from sound.effects.echo import func1

# Call package functions
print(echo.func1(1, 2))
print(echo.func2(1, 2))
print(equalizer.func1(1, 2))

# Call package class
class_test = echo.ClassName1(3, 4)
class_test.func1()
print(f'class func1 result: {class_test.total}')
