import sys
sys.path.insert(0, '../LIMEaid/LIMEaid')
from view import LIMEdisplay as ld
import numpy as np


def test_lime_display():
    # Input some dummy data so that lime_display has something to
    # display.
    data = np.array([[1, 2, 3, 0], [4, 5, 6, 1], [7, 8, 9, 2]],
                    np.int32)
    lime_beta = np.array([1, 1, 0])
    lime_int = 0.5
    x = [1.5, 1.5, 1.5]
    x_class = 0
    features = ["A", "B", "C"]
    class_names = ["ClassA", "ClassB"]
    # Plot dummy data. If plot throws an error, test fails.
    ld.lime_display(data, lime_beta, lime_int, x, x_class, features,
                    class_names)
