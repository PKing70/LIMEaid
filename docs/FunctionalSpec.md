# Data 515 LIME

Spring 2019

__Instructors:__

Joseph L. Hellerstein (jlheller@uw.edu)

David Beck (dacb@uw.edu)

Bernease Herman (bernease@uw.edu)

Sam Gao (gaoz6@cs.washington.edu)

## Functional Specification

This functional specification covers the proposed final project for the LIME team:

Francisco Javier Salido Magos (javiers@uw.edu)

Patrick King (pking70@uw.edu)

Suman Bhagavathula (sumanbh@uw.edu)

### Background

Machine Learning models are proliferating throughout business, science, and government while becoming more complex than ever before. One of the problems data scientists and users of Machine Learning (ML) face is _interpretability_; how can people explain and comprehend a decision made by complex ML models too complex to be understood in human terms? Interpretability can be critical to those implementing ML models, who need to determine why and how classifiers are working in order to evaluate whether they are effective or flawed. "Customers" of applied ML models, such as an applicant's denied loans, or travelers flagged as security risks, should be given reasonable explanations of the decisions made by otherwise opaque systems.

LIME (Local Interpretable Model-Agnostic Explanations) can be used to provide explanations of specific decisions made by "black box" ML models, and thus alleviate such concerns. With a LIME tool, scientists can identify how a specific output variable (decision) was reached given an instance of input variables, at least a set scoped to be _local_ to a specific output. LIME then is used to produce a simpler-to-explain model, typically linear, in the immediate vicinity of that output (for example, a linear regression line with only a few, most-relevant coefficients rather than many.) Easy to plot and discuss communication can then be produced to "break down" a complex model into _interpretable explanations_. Finally, to count as LIME, the tool really works to produce these explanations regardless of original, complex ML model type, so that only variations of input data local to a specific output variable are needed to work, whether the opaque model itself uses random forests, support vector machines (SVM), and neural networks, or more in an ensemble. Thus, _model-agnostic_.

### User profile

The user of our LIME tool is expected to be a data scientist with Python programming experience. They will want to analyze decisions made by their own ML model, presumably a complex one that demands explanation and insight into its classifications. The user should be able to programmatically input predictors and corresponding output of their ML model into a LIME function via a Python call, and the user should want meaningful information reported from the LIME tool, likely in the form of clear linear plots of a decision function.

For our implementation, the user is specifically interested in evaluating a dataset of college statistics and corresponding salary information, which predicts income depending upon school, major, perhaps other factors. They will specifically want to learn why the model (which we will implement as the ML model component of our project) predicts more or less salary for a given school...whether school type or location etc. are most relevant to a given income prediction.

### Data sources

For this project the following datasets will be used.


#### Salaries by college

Data sourced from the Wall Street Journal has been used on Kaggle to analyze Salaries by college, region, and academic major. (https://www.kaggle.com/wsj/college-salaries). The data is released under (CC0 Public Domain license) [https://creativecommons.org/publicdomain/zero/1.0/].

Additional, related data containing more potentially meaningful variables has been compiled and shared (here)[https://www.kaggle.com/smithashivakumar/college] under (CC0 Public Domain license) [https://creativecommons.org/publicdomain/zero/1.0/].

#### College Scorecard

The United States Department of Education has shared the raw data from its College Scorecard page under (CC0 Public Domain license) [https://creativecommons.org/publicdomain/zero/1.0/]. This data includes annual rating data from years 2017-1996 and includes additional features not available in the Kaggle sets, such as demographic data about cohorts, race and gender statistics of students, and more.

## Use cases

### Case 1: Model verification

After training competing ML models, data scientist will input a set of predictors and their corresponding output variable into our LIME function. In response, our function will deliver a ranking of which predictors have been determined to be the most relevant to this local output of each model, in such a way that the scientist can intuit whether expected or reasonable predictors are being used. For example, if the output was that the given message was spam, LIME should produce the specific weighted list/rank of the words the model used to make such a determination. 

#### Scenario

A data scientist develops a neural network model that separates spam from real e-mail messages, with high accuracy on the training set. Nevertheless, the classifier performs poorly in the field. The data scientist employs a LIME tool to analyze which inputs are the most influential on the model's decisions and discovers that a poorly engineered feature causes the model to miss important cues. The problem with the feature is addressed and model accuracy improves quickly.

#### Objective

Discover how models classify and be able to choose whether methods used seem more trustworthy or appropriate than others, by comparing two models using the same data.

#### Interactions

1. The scientist will enter selected predictors and an output that were classified independently by two ML models. This will be as arguments to the lime_sampler function of our LIME module.

2. The LIME tools outputs a csv file containing coefficients of a linear regression and MatPlotLib plot of the best fit linear regression using the most-weighted predictors for the instance.

3. The scientist can compare the predictors and the nature of the fit line and see if one model is better. By doing this with a variety of local inputs from competing models, a scientist should be able to debug and improve their model to improve results.

### Case 2: Decision explanation

A data scientist has already decided/proven that their ML model works effectively. For the output of the model, the data scientist needs a simplified, visualizable interpretation that can be used to cogently communicate the logic of an ML-decision to others, particularly others who demand layperson reports.

#### Scenario

A bank in Germany uses a complex ML model for credit scoring in its mortgage origination process. The European Union's General Data Protection Regulation specifies that EU citizens have a "right to an explanation on automated decision making" that is made about them. The ML model is too complex to be explained in human terms, but data scientists use the LIME tool that can provide local explanations to the model's decisions. That is, given a specific customer and a specific result, the tool can identify which specific input variables out of the many, played a determinant role in the system's output.

#### Objective

Show how a model has made a specific classification in an easy-to-interpret form.

#### Interactions

1. The scientist will enter selected predictors and an output that were classified by an ML model. This will be as arguments to the lime_sampler function of our LIME module.

2. The LIME tools outputs a MatPlotLib plot of the best fit linear regression line local to the input sample.

3. This enables the scientist to be able to show and speak to a simple, visualizable, "two-dimensional" interpretation of the given decision as effective communication and transparency to others about the trustworthiness (or lack thereof) of the system.
