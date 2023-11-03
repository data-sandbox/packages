# In this case __init__.py in sound directory must contain additional
# import info for the subpackages
import sound

# Alternative approach if specific modules are called frequently
# from sound.effects.echo import ClassName1

# Inspect
print(sound)
print(sound.effects)

# Call functions
print(sound.effects.echo.func1(1, 2))
print(sound.filters.equalizer.func1(1, 2))

# Call package class
class_test = sound.effects.echo.ClassName1(3, 4)
# Alternative approach if using `from sound.effects.echo import ClassName1`
# class_test = ClassName1(3, 4)

class_test.func1()
print(f'class func1 result: {class_test.total}')
