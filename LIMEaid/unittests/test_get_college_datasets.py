import sys
sys.path.insert(0, '../LIMEaid/LIMEaid')
from model import get_college_datasets as gcd


def test_get_most_recent_cohorts():
    """
    This is a test to get most recent cohorts dataset
    The test simply checks for atleast one row in the dataset and seems simple
    This test will be useful when we switch to acquire the dataset using APIs
    """
    scorecard = gcd.get_most_recent_cohorts()
    assert(1 <= scorecard.shape[0])


def test_get_salaries_by_region():
    """
    This is a test to get most recent cohorts dataset
    The test simply checks for atleast one row in the dataset and seems simple
    This test will be useful when we switch to acquire the dataset using APIs
    """
    salaries = gcd.get_salaries_by_region()
    assert(1 <= salaries.shape[0])
