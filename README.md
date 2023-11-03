# Packages

Sandbox for experimenting with the structure of packages and subpackages, and how to properly import and call functions from particular modules.

Resources:

- (https://docs.python.org/3/tutorial/modules.html#packages)
- (https://python-course.eu/python-tutorial/packages.php)

The example in this repo contains a package called `sound`. The package structure is as follows:

```
sound/                  Top level package
    __init__.py         Initializes the package
    effects/            Subpackage
        __init__.py
        echo.py
        reverse.py
    filters/            Subpackage
        __init__.py
        equalizer.py
        karaoke.py
```
