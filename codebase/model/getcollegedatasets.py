import pandas as pd
import os.path as op


def getmostrecentcohorts():
    """
    This is a placeholder to get the most recent cohorts dataset
    """
    dataset = pd.read_csv(op.join(".\\data", 'Most-_Recent-_Cohorts-_Scorecard-_Elements.csv'))
    return dataset

def getsalariesbyregion():
    """
    This is a placeholder to get the salaries by region dataset
    """
    dataset = pd.read_csv(op.join(".\\data", 'salaries-by-region.csv'))
    return dataset