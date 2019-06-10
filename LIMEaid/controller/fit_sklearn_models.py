import sys
sys.path.insert(0, '../LIMEaid/LIMEaid')
sys.path.insert(0, '../LIMEaid/LIMEaid/model')
import load_college_dataset as lcd
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegressionCV
from sklearn.model_selection import train_test_split
from sklearn.exceptions import ConvergenceWarning
from sklearn.tree import DecisionTreeClassifier
from sklearn import preprocessing
import warnings


def fit_multiclass_logistic_regression(printscore=False):
    """
    This function fits sklearn's multiclass logistic regression
    on the college dataset and returns the model
    """
    dataset = lcd.load_college_dataset()
    x = dataset.drop('SalaryClass', 1)
    pre_scale_data = x.values
    min_max_scaler = preprocessing.MinMaxScaler()
    scaled = min_max_scaler.fit_transform(pre_scale_data)
    x = pd.DataFrame(scaled)

    y = dataset['SalaryClass']
    x_train, x_test, y_train, y_test = train_test_split(x,
                                                        y,
                                                        test_size=0.2,
                                                        random_state=0)
    warnings.filterwarnings("ignore", category=ConvergenceWarning)
    clf = LogisticRegressionCV(cv=10, random_state=0,
                               multi_class='multinomial').fit(x_train, y_train)

    # print the accuracy score if the print flag is true
    if printscore is True:
        print(clf.score(x_test, y_test))

    return clf


def fit_random_forest(printscore=False):
    """
    This function fits sklearn's random forest classifier
    on the college dataset and returns the model
    """
    dataset = lcd.load_college_dataset()
    x = dataset.drop('SalaryClass', 1)
    pre_scale_data = x.values
    min_max_scaler = preprocessing.MinMaxScaler()
    scaled = min_max_scaler.fit_transform(pre_scale_data)
    x = pd.DataFrame(scaled)

    y = dataset['SalaryClass']
    x_train, x_test, y_train, y_test = train_test_split(x,
                                                        y,
                                                        test_size=0.2,
                                                        random_state=0)

    warnings.filterwarnings("ignore", category=ConvergenceWarning)
    rfc = RandomForestClassifier(n_estimators=20, random_state=0)
    rfc.fit(x_train, y_train)

    # print the accuracy score if the print flag is true
    if printscore is True:
        print(rfc.score(x_test, y_test))

    return rfc


def fit_decision_tree(printscore=False):
    """
    This function fits sklearn's decision tree classifier
    on the college dataset and returns the model
    """
    dataset = lcd.load_college_dataset()
    x = dataset.drop('SalaryClass', 1)
    pre_scale_data = x.values
    min_max_scaler = preprocessing.MinMaxScaler()
    scaled = min_max_scaler.fit_transform(pre_scale_data)
    x = pd.DataFrame(scaled)

    y = dataset['SalaryClass']
    x_train, x_test, y_train, y_test = train_test_split(x,
                                                        y,
                                                        test_size=0.2,
                                                        random_state=0)

    warnings.filterwarnings("ignore", category=ConvergenceWarning)
    dtc = DecisionTreeClassifier(random_state=0)
    dtc.fit(x_train, y_train)

    # print the accuracy score if the print flag is true
    if printscore is True:
        print(dtc.score(x_test, y_test))

    return dtc
