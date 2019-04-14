import pandas as pd
import pkgutil
from io import BytesIO


def load_bank(classifier=True):
    bank = pd.read_csv(
        BytesIO(
            pkgutil.get_data('loadbank', 'bank/bank.csv')
        ),
        sep=';',
    )
    bank_category = (
        bank.select_dtypes(
            include=object
        ).apply(
            lambda x: x.astype('category'),
            axis=0
        )
    )
    bank_numeric = bank.select_dtypes(
        include=int
    )
    if classifier:
        y = bank_category.y
        X = pd.concat(
            [bank_category, bank_numeric],
            axis=1
        ).drop(
            ['y'], axis=1
        )
    else:
        y = bank_numeric.balance
        X = pd.concat(
            [bank_category, bank_numeric],
            axis=1
        ).drop(
            ['balance'], axis=1
        )
    return X, y

def load_bank_classifier():
    return load_bank(classifier=True)

def load_bank_regressor():
    return load_bank(classifier=False)
