"""One approach to managing package imports"""

# In this case __init__.py in sound directory must contain additional
# import information
import sound

# Inspect
print(sound)
print(sound.effects)

# Call functions
print(sound.effects.echo.func1(1, 2))
print(sound.filters.equalizer.func1(1, 2))
