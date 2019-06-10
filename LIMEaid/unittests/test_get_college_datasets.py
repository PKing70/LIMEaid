import os
import sys
sys.path.insert(0,'../LIMEaid/LIMEaid')
from model import get_college_datasets as gcd


def test_basic_pass():
    """
    This is a basic pass test case scenario to make sure coverage banner works
    """
    assert(1 == 1)


def test_get_most_recent_cohorts():
    """
    This is a test to get most recent cohorts dataset
    """
    scorecard = gcd.get_most_recent_cohorts()
    assert(1 <= scorecard.shape[0])


def test_get_salaries_by_region():
    """
    This is a test to get most recent cohorts dataset
    """
    salaries = gcd.get_salaries_by_region()
    assert(1 <= salaries.shape[0])
