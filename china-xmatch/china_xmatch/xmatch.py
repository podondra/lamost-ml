import pandas as pd


def xmatch(left, right, left_on, right_on):
    """Cross-match data from left and right pandas.DataFrame on right_on
    and left_on columns.

    Use pd.merge's inner join.
    """
    return pd.merge(left, right, left_on=left_on, right_on=right_on)


def split_according_to_profile(data):
    emission_index = data['profile'] == 'emission'
    return data[emission_index], data[~emission_index]
