from setuptools import setup, find_packages

setup(
    name='mdict',
    version='0.0.1',
    packages=find_packages(),
    #include_package_data=True,
    install_requires=[
        'click',
        'requests',
        'termcolor'
    ],
    entry_points='''
    [console_scripts]
    mdict=mdict:mdict
    '''
)