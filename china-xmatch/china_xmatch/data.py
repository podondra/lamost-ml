import numpy as np
import pandas as pd


def remove_duplicities(data, column):
    """Remove rows from data which has same values in a column.
    
    Keep the first entry and remove all others from data.

    data is a pandas.DataFrame and
    column is the column whete to look for duplicities.
    """
    return data[~data[column].duplicated()]


def read_candidates(filename):
    """Read CSV file with candidates and return it as a pandas.DataFrame."""
    candidates = remove_duplicities(pd.read_csv(filename), 'designation')
    # remove 'LAMOST ' from designation
    candidates['designation'] =  candidates['designation'].map(
            lambda x: x.split()[-1]
            )
    return candidates


def read_lin_catalogue(filename):
    """Read Lin's catalogue:
    http://paperdata.china-vo.org/vac/dr1/lin2015tab23.xlsx.
    """
    # read the excel file
    lin_excel = pd.read_excel(
        filename, header=[0, 1], skiprows=[2],
        converters={('Table 2', 'DR1'): np.int}
    )
    # there are 2 tables next to each other
    table_2 = lin_excel['Table 2']
    table_3 = lin_excel['Table 3'].reset_index(drop=True)
    # drop null entries caused by tables next to each other
    table_2 = table_2[table_2.index.notnull()]
    # save index
    table_2['ID'] = table_2.index
    # remove column which separates the 2 tables and remove index
    table_2 = table_2.drop(['Remark.1'], axis=1).reset_index(drop=True)
    # concatenate the 2 tables
    return pd.concat([table_2, table_3], sort=False)


def read_hou_catalogue(filename):
    """Read Hou's catalogue:
    http://paperdata.china-vo.org/vac/dr2/HouEmission2016.tar.gz.
    """
    return remove_duplicities(pd.read_csv(filename, sep='\t'), '#designation')
