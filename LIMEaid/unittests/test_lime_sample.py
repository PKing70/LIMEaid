from LIMEaid.LIMEaid.controller import LIMEaid as la
import pytest

from sklearn import datasets
from sklearn import preprocessing


def test_lime_fit():
    # Read Iris dataset
    data_set = datasets.load_iris()
    # Number of perturbed samples to be generated.
    n = 10000
    # Number of bins for the histograms of continous attributes.
    num_bins = 25
    # Normalizing Iris attributes.
    data_norm = preprocessing.scale(data_set.data)

    # Generate n random samples with the same probability distribution
    # as the classifications of the 150 instances in the Iris dataset.
    # Random samples and original values are normalized for the
    # comparison.
    output = lime_sample(n, False, data_set.target, 0)
    values = preprocessing.scale(data_set.target.astype(float))
    assert(len(values) == n)
