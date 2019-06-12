import pandas as pd
import os

COHORTSDATASET = "../data/Most-_Recent-_Cohorts-_Scorecard-_Elements.csv"
SALARIESDATASET = "../data/salaries-by-region.csv"


def get_most_recent_cohorts():
    """
    This function returns the most recent cohorts dataset
    The dataset is currently pulled from the data directory
    which contains the most recent available dataset(2017)
    In future, this will use APIs to pull the dataset from source
    """
    my_path = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(my_path, COHORTSDATASET)
    with open(path) as f:
        print(f)
        dataset = pd.read_csv(f)
    return dataset


def get_salaries_by_region():
    """
    This function returns the salaries by region dataset
    The dataset is currently pulled from the data directory
    which contains the most recent available dataset(2017)
    In future, this will use APIs to pull the dataset from source
    """
    my_path = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(my_path, SALARIESDATASET)
    with open(path) as f:
        dataset = pd.read_csv(f)
    return dataset
