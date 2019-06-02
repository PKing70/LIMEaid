from LIMEaid.LIMEaid.controller import LIMEaid as la
import pytest

from sklearn import datasets
from sklearn import preprocessing


def test_lime_fit_discrete():
    # Read Iris dataset
    data_set = datasets.load_iris()
    # Number of perturbed samples to be generated.
    n = 10000

    # Generate n random samples with the same probability
    # distribution as the classifications of the 150 instances in the
    # Iris dataset.
    output = la.lime_sample(n, False, data_set.target, 0)
    assert(len(output) == n)
