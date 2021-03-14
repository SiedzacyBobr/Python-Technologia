# Built-in modules
import os
import sys

# Modules requiring pip3-install
import dill
import pandas as pd
import numpy as np

# User created modules
from Database.program import test_func as funkcja
from Database.program2 import test_func2, test_func3

funkcja()
test_func2()
tst = test_func3(word1='test1', word2='test2')

df = pd.DataFrame({'kolumna1': [1, 2, 3], 'kolumna2': [4, 5, 6]})
with open('dataframe.dill', 'wb') as file:
    dill.dump(obj=df, file=file)

with open('dataframe.dill', 'rb') as file:
    df2 = dill.load(file=file)

