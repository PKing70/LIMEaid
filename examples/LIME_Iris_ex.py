import sys, os
sys.path.append(os.getcwd())
import numpy as np
import LIMEaid as la
from sklearn import preprocessing
from sklearn import datasets
from sklearn import tree
from sklearn.naive_bayes import GaussianNB

#####################################################################
# This example uses the functions in the LIMEaid.py package to
# explain classification of instances from a machine learning model.
# Example uses either a Naive Bayes or a Decision Tree classifier.
#####################################################################

# Read Iris dataset
data_set = datasets.load_iris()
# Number of perturbed samples to be generated.
n = 10000
# Number of bins for the histograms of continous attributes.
num_bins = 25
# Normalizing Iris attributes.
data_norm = preprocessing.scale(data_set.data)

# Choose one of the machine learning models below:

# Fitting a decision tree model to the iris dataset.
# clf = tree.DecisionTreeClassifier()
# clf = clf.fit(data_norm, data_set.target)

# Fitting a Naive Bayes model.
clf = GaussianNB()
clf = clf.fit(data_norm, data_set.target)

# Now we generate the random samples.
# Note that because all four attributes are floats (continuous),
# we do not call the discrete random generator.
perturbed_samples = np.zeros(n)
# The for loop calls the random sample generator four times,
# once for each attribute in the Iris dataset.
for j in range(0, data_set.data.shape[1]):
    array = data_set.data[:, j]
    output = la.lime_sample(n, True, array, num_bins)
    perturbed_samples = np.vstack((perturbed_samples, output))
perturbed_samples = np.transpose(perturbed_samples[1:, ])

# Label the samples using the model we fitted before.
class_perturb_samples = clf.predict(perturbed_samples)

# From the original data we select an instance at random.
# This is the instance we will interpret using LIME.
inst_num = np.round(np.random.uniform(0, data_set.data.shape[0], 1))
inst_num = inst_num[0].astype(int)
# x is the instance we are selecting and x_class is its
# classification. If you don't want to use a randomly selected
# instance, use one of your choice.
x = data_norm[inst_num, :]
x_class = data_set.target[inst_num]

# Call LIME.
lime_beta, lime_int, lime_weigh = la.lime_fit(x,
                                              x_class,
                                              perturbed_samples,
                                              class_perturb_samples)

# Print output of LIME results.
print("Instance to be interpreted:")
for j in range(0, len(lime_beta)):
    print("Feature: ", data_set.feature_names[j], "\tvalue: ",
          data_set.data[inst_num, j], "\tnormalized value: ",
          data_norm[inst_num, j])
print("Classification: ",
      data_set.target_names[data_set.target[inst_num]],
      data_set.target[inst_num])
print("\nSignificant coefficients from LIME adjusted"
      " linear model:")
for j in range(0, len(lime_beta)):
    if(lime_beta[j] != 0):
        print("Feature: ", data_set.feature_names[j],
              "\tCoefficient: ", lime_beta[j])
print("Intercept: ", lime_int)
