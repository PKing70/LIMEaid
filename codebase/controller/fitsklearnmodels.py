from codebase.model import loadcollegedataset as lcd
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegressionCV
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier


def fitmulticlasslogisticregression(printscore = False):
    """
    This function fits sklearn's multiclass logistic regression
    on the college dataset and returns the model
    """
    dataset = lcd.loadcollegedataset()
    x = dataset.drop('SalaryClass',1)
    y = dataset['SalaryClass']
    xTrain, xTest, yTrain, yTest = train_test_split(x, y, \
        test_size = 0.2, random_state = 0)
    clf = LogisticRegressionCV(cv=10, random_state=0, \
        multi_class='multinomial').fit(xTrain, yTrain)
    
    #print the accuracy score if the print flag is true
    if printscore == True:
        print(clf.score(xTest,yTest))

    return clf

def fitrandomforest(printscore = False):
    """
    This function fits sklearn's random forest classifier
    on the college dataset and returns the model
    """
    dataset = lcd.loadcollegedataset()
    x = dataset.drop('SalaryClass',1)
    y = dataset['SalaryClass']
    xTrain, xTest, yTrain, yTest = train_test_split(x, y, \
        test_size = 0.2, random_state = 0)

    rfc = RandomForestClassifier(n_estimators=20, random_state=0)  
    rfc.fit(xTrain, yTrain)  
    
    #print the accuracy score if the print flag is true
    if printscore == True:
        print(rfc.score(xTest,yTest))

    return rfc

def fitdecisiontree(printscore = False):
    """
    This function fits sklearn's decision tree classifier
    on the college dataset and returns the model
    """
    dataset = lcd.loadcollegedataset()
    x = dataset.drop('SalaryClass',1)
    y = dataset['SalaryClass']
    xTrain, xTest, yTrain, yTest = train_test_split(x, y, \
        test_size = 0.2, random_state = 0)

    dtc = DecisionTreeClassifier(random_state=0)  
    dtc.fit(xTrain, yTrain)  
    
    #print the accuracy score if the print flag is true
    if printscore == True:
        print(dtc.score(xTest,yTest))

    return dtc