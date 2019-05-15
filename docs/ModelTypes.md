## Random Forest

https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html

### Fit parameters:

X : array-like or sparse matrix of shape = [n_samples, n_features]

The training input samples. Internally, its dtype will be converted to dtype=np.float32. If a sparse matrix is provided, it will be converted into a sparse csc_matrix.

y : array-like, shape = [n_samples] or [n_samples, n_outputs]

The target values (class labels in classification, real numbers in regression).

sample_weight : array-like, shape = [n_samples] or None

Sample weights. If None, then samples are equally weighted. Splits that would create child nodes with net zero or negative weight are ignored while searching for a split in each node. In the case of classification, splits are also ignored if they would result in any single class carrying a negative weight in either child node.

### Random forest pros:

* difficult to interpret results; could benefit from LIME

### Random forest cons?

* Already returns gini index for feature importance...does not benefit from LIME? (Could one just sort by feature importance and produce the same simplified explanation that we/LIME can produce?)

feature_importances_ : array of shape = [n_features]

Return the feature importances (the higher, the more important the feature).

## Decision Tree

https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier

### Fit Parameters:	

X : array-like or sparse matrix, shape = [n_samples, n_features]

The training input samples. Internally, it will be converted to dtype=np.float32 and if a sparse matrix is provided to a sparse csc_matrix.

y : array-like, shape = [n_samples] or [n_samples, n_outputs]

The target values (class labels) as integers or strings.

sample_weight : array-like, shape = [n_samples] or None

Sample weights. If None, then samples are equally weighted. Splits that would create child nodes with net zero or negative weight are ignored while searching for a split in each node. Splits are also ignored if they would result in any single class carrying a negative weight in either child node.

check_input : boolean, (default=True)

Allow to bypass several input checking. Don’t use this parameter unless you know what you do.

X_idx_sorted : array-like, shape = [n_samples, n_features], optional

The indexes of the sorted training input samples. If many tree are grown on the same dataset, this allows the ordering to be cached between trees. If None, the data will be sorted here. Don’t use this parameter unless you know what to do.

### Decision tree pros:

* difficult to interpret results; could benefit from LIME

### Decision tree cons?

*  Should produce a fairly-easy-to-explain decision already (no need for LIME) as decision tree decisions can be explained by tracing the decision path. Might want to do our classification model using a more tricky method (random forest)

## Neural Network

https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html#sklearn.neural_network.MLPClassifier

### Fit Parameters:

X : array-like or sparse matrix, shape (n_samples, n_features)

The input data.

y : array-like, shape (n_samples,) or (n_samples, n_outputs)

The target values (class labels in classification, real numbers in regression).

### NN pros:

* "black box" should benefit from LIME

### NN cons?

* I don't know; then again I don't understand much about them yet
