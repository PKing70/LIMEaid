from codebase.controller import fitsklearnmodels as fkm


def test_multiclasslogisticregression():
	"""
	This is a test for multiclass logistic regression on college dataset
	"""
	model = fkm.fitmulticlasslogisticregression(True)
	assert("<class 'sklearn.linear_model.logistic.LogisticRegressionCV'>"==type(model))

def test_randomforest():
	"""
	This is a test for random forest on college dataset
	"""
	model = fkm.fitrandomforest(True)
	assert("<class 'sklearn.ensemble.forest.RandomForestClassifier'>"==type(model))

def test_decisiontree():
	"""
	This is a test for decision tree on college dataset
	"""
	model = fkm.fitdecisiontree(True)
	assert("<class 'sklearn.tree.tree.DecisionTreeClassifier'>"==type(model))