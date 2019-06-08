from LIMEaid.LIMEaid.controller import fit_sklearn_models as fkm


def test_multiclass_logistic_regression():
    """
    This is a test for multiclass logistic regression on college dataset
    """
    model = fkm.fit_multiclass_logistic_regression(True)
    assert("<class 'sklearn.linear_model.logistic.LogisticRegressionCV'>"
           in str(type(model)))


def test_random_forest():
    """
    This is a test for random forest on college dataset
    """
    model = fkm.fit_random_forest(True)
    assert("<class 'sklearn.ensemble.forest.RandomForestClassifier'>"
           in str(type(model)))


def test_decision_tree():
    """
    This is a test for decision tree on college dataset
    """
    model = fkm.fit_decision_tree(True)
    assert("<class 'sklearn.tree.tree.DecisionTreeClassifier'>"
           in str(type(model)))
