import matplotlib.pyplot as plt
import numpy as np


def lime_display(data, lime_beta, lime_int, x, x_class, features):
    """
    Displays results from the lime_fit() function.

    Inputs are:
    - A numpy array containing the random samples for which LIME fit
      the linear model, data.
    - A numpy array containing the coefficients of the linear model
      fitted by LIME, lime_beta
    - The intercept of the linear model fitted by LIME, lime_int.
    - The attribute values for the feature we are looking to explain, x.
    - The class assigned to the instance we are looking to explain,
      x_class.
    - A vector containing the names of the attributes in data, features.

    The function displays the right graph or graphs showing the LIME
    algorithm's output.
    OUTPUT IS LIMITED TO SIX CLASSES.
    """

    # Vector of colors that will be assigned to each class in the
    # output.
    colors = ['k', 'b', 'm', 'c', 'g', 'y']
    # Identifying the unique classes in the output data.
    classes = np.unique(data[:, -1])

    # Identifying the significant attributes as selected by LIME.
    significant_attributes = 0
    for j in range(0, len(lime_beta)):
        if(lime_beta[j] != 0):
            significant_attributes = np.append(significant_attributes,
                                               j)
    significant_attributes = significant_attributes[1:]

    if (len(significant_attributes) == 2):
        # For visualization we separate perturbed samples classified
        # by the ML model as in-class, from those classified
        # out-of-class.
        in_class_data = data[data[:, -1] == x_class]
        out_class_data = data[data[:, -1] != x_class]
        # Displaying the output.
        plt.rcParams['figure.figsize'] = [10.0, 10.0]
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        ax.scatter(out_class_data[:, significant_attributes[0]],
                   out_class_data[:, significant_attributes[1]],
                   marker='+', c='c', label='Out of class')
        ax.scatter(in_class_data[:, significant_attributes[0]],
                   in_class_data[:, significant_attributes[1]],
                   marker='x', c='b', label='In class')
        ax.scatter(x[significant_attributes[0]],
                   x[significant_attributes[1]], marker='o',
                   c='r', label='Instance')
        plt.grid(b=True, which='both', color='0.85', linestyle='-')
        ax.set_xlabel(features[significant_attributes[0]])
        ax.set_ylabel(features[significant_attributes[1]])
        plt.legend(loc='upper left')

    # Displaying regression values for perturbed samples.
    plt.rcParams['figure.figsize'] = [5.0, 10.0]
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    # Compute all LIME regression values for all perturbed samples
    # and for the instance to be explained, and plot them.
    for j in range(0, len(classes)):
        class_reg = data[data[:, -1] == classes[j]]
        class_reg = lime_int + np.sum(class_reg[:, :-1] * lime_beta,
                                      axis=1)
        ax.scatter(np.zeros(len(class_reg)) + j, class_reg,
                   marker='o', c=colors[j])
    instance = sum(x * lime_beta) + lime_int
    ax.scatter(x_class, instance, marker='o', c='r')
    ax.set_ylabel('LIME Regression')
    plt.grid(b=True, which='both', color='0.85', linestyle='-')
    plt.show()
