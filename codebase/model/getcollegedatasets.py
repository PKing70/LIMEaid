import pandas as pd
import os


def getmostrecentcohorts():
    """
    This function returns the most recent cohorts dataset
    """
    my_path = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(my_path, "../data/Most-_Recent-_Cohorts-_Scorecard-_Elements.csv")
    with open(path) as f:
        print(f)
        dataset = pd.read_csv(f)
    return dataset

def getsalariesbyregion():
    """
    This function returns the salaries by region dataset
    """ 
    my_path = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(my_path, "../data/salaries-by-region.csv")
    with open(path) as f:
        dataset = pd.read_csv(f)
    return dataset