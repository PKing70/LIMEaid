import numpy as np
from sklearn import datasets
from sklearn import preprocessing
from sklearn import tree
from sklearn import linear_model
from sklearn.naive_bayes import GaussianNB


def lime_sample(n, continuous, np_vector, num_bins):
    """
    Generates n random values with distribution provided as input.

    Inputs are:
    - Desired number random samples, n.
    - A boolean value indicating whether the input vector contains
      continous values (True) or discrete values (False), continuous.
    - The vector of values that describes the distribution of the
      random samples that are to be generated, np_vector.
    - Desired number of bins for the histogram, num_bins. If
      continuous=True, this value is ignored.

    If continuous, the domain of values in np_vector is broken down
    into num_bins buckets, and the frequency of samples for each bin
    is computed. The frequency determines the number of random
    samples to be generated for each bucket, and each random sample
    generated is chosen from a uniform probability distribution with
    end values equal to those of the corresponding bucket.

    If discrete, the frequencies of each class are computed and used
    to generate random values with the corresponding multinomial
    distribution.

    Output is the vector rand that contains n random samples with the
    appropriate distribution.
    """

    if continuous:
        # Normalize data to mean zero and std. dev of one
        np_vector = preprocessing.scale(np_vector)

        # Compute frequency of instances in each of num_bins buckets.
        freqs, h_bins = np.histogramdd(np_vector, bins=num_bins)
        freqs = freqs/np.sum(freqs)

        # h_bins lists the bin edges in the distribution.
        h_bins = np.asarray(h_bins[0])
        rand = np.zeros(1)

        # samples_bins dictates how many random instances have
        # to be generated in each bin.
        samples_bins = np.random.multinomial(n, freqs, 1)

        # The for loop uses a uniform distribution to generate
        # the desired number of instances in each bucket of the
        # distribution.
        for j in range(0, len(freqs)):
            samples = np.random.uniform(h_bins[j], h_bins[j+1],
                                        samples_bins[0][j])
            rand = np.hstack((rand, samples))
        rand = rand[1:, ]
    else:
        # Extract the list of unique values in np_vector, and the
        # frequency of each value.
        values, freqs = np.unique(np_vector, return_counts=True)
        freqs = freqs/np.sum(freqs)
        values = values.astype(float)

        # Normalize values to mean zero and unit variance.
        values = preprocessing.scale(values)

        # Using a multinomial distribution, determine the number
        # of instances of each class that are to be generated.
        multinom_rand = np.random.multinomial(n, freqs, 1)[0]

        # rand will contain the list of instances that are generated
        # based on the numbers in multinom_rand.
        rand = np.zeros(n)
        k = 0
        for j in range(0, len(values)):
            rand[k:k+multinom_rand[j]] = values[j]
            k = k + multinom_rand[j]
    return(rand)


def lime_fit(x, x_class, perturbed_samples, class_perturb_samples):
    """
    Computes LIME linear model coefficients.

    Inputs are:
    - x, the instance from the original ML model we are trying to
      explain.
    - x_class, the classification assigned to x by the original ML
      model.
    - perturbed_samples which are the random perturbations of inputs
      that were generated.
    - class_perturb_samples which are the classifications assigned to
      each of the perturbations by the original ML model.

    Outputs are:
    - Coefficients for the LIME linear model.
    - The intercept for the LIME linear model.
    - List of LIME weights that were computed for each instance
      in perturbed_samples.
    """

    # Compute LIME weights.
    sigma = np.var(np.sum((perturbed_samples - x)**2, axis=1))
    l_weights = np.exp(-np.sum((perturbed_samples - x)**2, axis=1) /
                       sigma)

    # We identify the correct class for the instance we wish to
    # interpret, make that class one and all others become
    # class zero.
    lime_class = class_perturb_samples == x_class
    lime_class = lime_class.astype(int)

    # Multiply the LIME weights by the perturbed samples and the
    # original ML model's output.
    perturb_weighted = (perturbed_samples.T * l_weights).T
    class_weighted = class_perturb_samples * l_weights

    # Using the perturbed samples and the above classification, we
    # fit the LIME linear model using LASSO.
    # reg = linear_model.LassoCV(eps=0.001, n_alphas=100, cv=5)
    reg = linear_model.Lasso(alpha=0.01)
    reg.fit(perturb_weighted, class_weighted)
    return(reg.coef_, reg.intercept_, l_weights)

#####################################################################
# EXAMPLE: How to use the functions.
#####################################################################

# Read Iris dataset
data_set = datasets.load_iris()
# Number of perturbed samples to be generated.
n = 10000
# Number of bins for the histograms of continous attributes.
num_bins = 25
# Normalizing Iris attributes.
data_norm = preprocessing.scale(data_set.data)

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
    output = lime_sample(n, True, array, num_bins)
    perturbed_samples = np.vstack((perturbed_samples, output))
perturbed_samples = np.transpose(perturbed_samples[1:, ])

# Label the samples using the model we fitted before.
class_perturb_samples = clf.predict(perturbed_samples)

# From the original data we select an instance at random.
# This is the instance we will interpret using LIME.
inst_num = np.round(np.random.uniform(0, data_set.data.shape[0], 1))
inst_num = inst_num[0].astype(int)
x = data_norm[inst_num, :]
x_class = data_set.target[inst_num]

# Call LIME.
lime_beta, lime_intercept, lime_weights = lime_fit(x,
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
print("\nSignificant coefficients from LIME adjusted linear model:")
for j in range(0, len(lime_beta)):
    if(lime_beta[j] != 0):
        print("Feature: ", data_set.feature_names[j],
              "\tCoefficient: ", lime_beta[j])
print("Intercept: ", lime_intercept)
