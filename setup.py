from setuptools import setup

setup(
    name='BetterClicker',
    version='0.1',
    description='A autoclicker script with more options',
    url='https://github.com/IceDah/Better-AutoClicker',
    author='IceDah',
    author_email='',
    license='',
    py_modules=['autoclicker'],
    install_requires=[
        'pyautogui',
        'pynput'
    ],
    entry_points={
        'console_scripts': [
            'autoclicker=autoclicker:main'
        ]
    }
)
