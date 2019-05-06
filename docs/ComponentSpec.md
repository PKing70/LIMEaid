# Data 515 LIME

Spring 2019

__Instructors:__
Joseph L. Hellerstein (jlheller@uw.edu)

David Beck (dacb@uw.edu)

Bernease Herman (bernease@uw.edu)

Sam Gao (gaoz6@cs.washington.edu)

## Component Specification

This component specification covers the proposed final project for the LIME team:

Francisco Javier Salido Magos (javiers@uw.edu)

Patrick King (pking70@uw.edu)

Suman Bhagavathula (sumanbh@uw.edu)

### Software components

Our project has two major modules, each of which can be broken down into multiple components. The two modules are:

- Machine Learning (ML) model that takes a number of predictors as input, including college name, student major, type of school and other, and outputs a likely graduating salary bracket for students from that college/major combination.
- A LIME module that can help a data scientist understand which predictors played a major role in defining the ML model's output for a particular set of inputs.

#### _Machine Learning Model_

For the ML model we will first need to merge, cleanse and prepare our datasets, which will likely require some amount of manual work to identify potential limitations in the datasets themselves, what the best way to encode the data is, and whether value imputation is necessary in some cases. Once the above decisions have been made, we will have to build a component we'll call data_cleanse that automates as many of these decisions as possible.

A set of components will follow the above, that will enable us to train and test various ML models. For this step we plan to leverage functions available in SciKit and other Python packages that enable us to fit various types of potentially complex models, such as boosted trees, random forests, support vector machines with various kernels, and others.

The final component for this first module will be employed to present results from the various approaches we will test, as well as visualizing them. To do this we plan to level components from Python packages such as Matplotlib.

#### _LIME Module_

For the second module we will write three components that will provide the desired LIME functionality.

The first component, lime_sampler, will take the predictors and corresponding output of one test instance to the ML model and generate randomized samples of the ML model's behavior, using only a randomly selected subset of its inputs. These randomized samples will provide insight on the ML model's behavior in the immediate vicinity of the model's output for the test instance.

For each test instance selected by the first component above, the second componen, lime_fit, will take the randomly selected subset of predictors and randomized samples, and fit a linear model to them. So, for each test instance we'll end up with a set of linear models.

Our third component, lime_optim, will identify the linear model from component number two that minimizes the error with respect to the output for the selected test instance and generate a human-readable output that will facilitate interpretation of the complex ML model's behavior. For this third component we will most likely leverage ML functions from SciKit, such as LASSO, and graphics functions from Matplotlib.

### Interactions to accomplish use cases

The interaction is quite simple. The first module is the ML model whose output the data scientist needs to understand. Since the model is complex, direct interpretation of it's output would require too much effort or is simply not possible in human terms.

In order to gain insight, the data scientist needs to develop intuition on how the predictors at the input of the model affect its output classification, for each test instance. Given that we are dealing with a complex ML model, we use LIME to provide local explanations that will enable the data scientist to acquire intution of what drive's the model's decisions in the vicinity of each specific test instance that are to be interpreted.

### Preliminary plan

Our preliminary plan consists of a two-pronged approach:

For module one, the Machine Learning model:

- Inspection of the datasets we plan to employ.
- Implementation of the data_cleanse component.
- Fitting of a number of ML models to classify colleges and majors into potential salary brackets.

For the LIME module:

- Do additional research on some of the mathematical and logistic subtleties of sampling and optimization for LIME.
- Build and test the lime_sampler.
- Build and test the lime_fit.
- Build and test the lime_optim.
- Do end-to-end testing of the components.

Once the above steps have been completed, we will evaluate the outputs of the ML model(s) using LIME and produce the final report.