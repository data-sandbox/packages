"""One approach to managing package imports"""

# In this case __init__.py in sound directory can be empty
from sound.effects import *
from sound.filters import *

# Alternative approach (and usually preferred) to using * is:
# from sound.effects import echo
# from sound.filters import equalizer

# Call package functions
print(echo.func1(1, 2))
print(equalizer.func1(1, 2))
