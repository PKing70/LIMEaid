import sys
sys.path.insert(0, '../LIMEaid/LIMEaid/controller')
sys.path.insert(0, '../LIMEaid/LIMEaid/model')
sys.path.insert(0, '../LIMEaid/LIMEaid/view')
import fit_sklearn_models as fsm
import LIMEaid as la
import LIMEdisplay as ld
import load_college_dataset as gcd
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn import tree

# Number of perturbed samples to be generated.
n = 100000
# Number of bins for the histograms of continous attributes.
num_bins = 25

# The functions below merge and prepare the data, after uploading it,
# and leave it ready for us to fit the logistic regression model.
college = gcd.load_college_dataset()
features = list(college)[1:]
salary_class = np.array(college.iloc[:, 0])
college = np.array(college.iloc[:, 1:])

# Next, we fit the logistic regression model.
clf = fsm.fit_multiclass_logistic_regression()

# Interpreting the output of the Logistic Regression model
# using LIME.
# We now take the dataset, attributes only, and form them we generate
# n random samples with similar distributions in the values of each
# attribute.

# Note that, unlike the Iris example where all attributes had continuous
# values, in this dataset the first attribute has discrete values.
# So, we call lime_sample setting the "continuous" parameter, second one
# in the call, to False.
perturbed_samples = la.lime_sample(n, False, college[:, 0], num_bins)
# The for loop calls lime_sample for each of the remaining attributes,
# setting the "continuous" parameter to True.
for j in range(1, college.shape[1]):
    array = college[:, j]
    output = la.lime_sample(n, True, array, num_bins)
    perturbed_samples = np.vstack((perturbed_samples, output))
perturbed_samples = np.transpose(perturbed_samples)

# Once random samples with the right distributions for each attribute
# have been generated, we provide them as input to the Logistic
# Regression model we fitted earlier, and obtain the classification
# for each.
class_perturb_samples = clf.predict(perturbed_samples)

# We select a single instance from the dataset. This is the instance
# we will try to interpret using LIME.

# Normalizing the data.
college_norm = preprocessing.scale(college)
# Selecting the instance to interpret.
inst_num = np.round(np.random.uniform(0, college_norm.shape[0], 1))
inst_num = inst_num[0].astype(int)
# x is the selected instance, and x_class is the class assigned
# by the decision tree.
x = college_norm[inst_num, :]
x_class = salary_class[inst_num]

# Calling LIME to get interpretation.
# We now fit the LIME linear model to get the coefficients and
# intercept, as well as the weight of each random sample,
# based on its L2 distance to the instance that is being
# interpreted.
lime_beta, lime_int, lime_weight = la.lime_fit(x,
                                               x_class,
                                               perturbed_samples,
                                               class_perturb_samples)

# Interpreting the results.
# Below we present the results obtained from the LIME linear
# regression model, and identify those attributes that played a
# significant role in the classification that was assigned to each
# instance by the Logistic Regression classifier.

# Print output of LIME results.
# First list the attributes and values for the instance
# we are looking at.
print("Instance to be interpreted:")
for j in range(0, len(lime_beta)):
    print("Feature: ", features[j], "\tvalue: ",
          college[inst_num, j], "\tnormalized value: ",
          college_norm[inst_num, j])
print("Classification: ", x_class)
# Second we list the attributes that LIME has identified as
# significant in this case, along with the corresponding LIME
# coefficients and the LIME intercept.
print("\nSignificant coefficients from LIME adjusted"
      " linear model:")
significant_attributes = 0
for j in range(0, len(lime_beta)):
    if(lime_beta[j] != 0):
        significant_attributes = np.append(significant_attributes, j)
        print("Feature: ", features[j],
              "\tCoefficient: ", lime_beta[j])
significant_attributes = significant_attributes[1:]
print("Intercept: ", lime_int)

# If the number of significant attributes in the interpretation of a
# particular instance is equal to two, we plot the random samples and
# the instance that is being interpreted on a cathesian plane. In
# some cases, classes can be separated for the most part by looking
# at the two selected attributes. Note that those random samples that
# were classified differently from the instance we are interpreting
# are merged into a single out-of-class representation.
# Finally, we plot the output of the fitted LIME Linear Regression
# model for each sample, against its class, as yielded by the
# Logistic Regression model and see that, in most cases, the classes
# can be differentiated using this model only.
full_data = np.column_stack((perturbed_samples,
                             class_perturb_samples))
ld.lime_display(full_data, lime_beta, lime_int, x, x_class, features,
                [1, 2, 3])
