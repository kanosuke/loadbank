from distutils.core import setup


setup(
    name='loadbank',
    version='0.0.1',
    install_requires=[
        "pandas",
    ],
    packages=[
        "loadbank", 
    ],
    package_data={'loadbank': ['bank/bank.csv']},
)
