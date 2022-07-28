'''
Find out what files are missing
Anna @ Pardee
July 28, 2022
'''

import pandas as pd
import re
import numpy as np

def read_file(filename):
    try:
        db = pd.read_excel(filename)
    except:
        print('No such file, make sure you got the right file name.')
    return db

if __name__ == '__main__':

    db_scores = read_file('GFP_highbrightness_SPscores.xlsx')
    s = db_scores['ID'].to_numpy()
    all_numbers = np.arange(0, 110)
    not_in = [x for x in all_numbers if x not in s]

    print(not_in)
    print(len(not_in))