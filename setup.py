from setuptools import setup, find_packages

VERSION = '1.0' 
DESCRIPTION = 'A really simple Python library to do some math operations'
LONG_DESCRIPTION = 'A really simple Python library to do some math operations'

# Setting up
setup(
    name="pymathtools", 
    version=VERSION,
    author="Sean-e",
    author_email="<seane410@gmail.com>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    py_modules=['pymathtools'],  # Include pythonryd.py directly as a module
    install_requires=[],  # Add any additional packages that need to be installed along with your package. Eg: 'requests'
    keywords=['python', 'api'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
