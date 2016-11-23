from setuptools import setup

setup(
    name='braker',
    version='0.1',
    py_modules=['braker'],
    install_requires=['Click',],
    entry_points='''
        [console_scripts]
        braker=braker:cli
    '''
)
