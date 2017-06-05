from distutils.core import setup

setup(
    name='pipd',
    version='0.2',
    description='Extension of pip with built-in dependency tracking',
    packages=['pipd', 'pipd.utils'],
    scripts=['bin/pipd'],
    author='Ryan Smick',
    url='https://github.com/ryansmick/pipd',
    install_requires=['termcolor'],
)
