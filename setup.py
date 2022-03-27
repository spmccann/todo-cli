from setuptools import setup

setup(
    name='TodoFries',
    version='0.01',
    py_modules=['TodoFries'],
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'TodoFries = TodoFries:cli',
        ],
    },
)
