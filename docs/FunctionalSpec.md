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

Machine Learning models are proliferating throughout business, science, and government while becoming more complex than ever before. The problem is _interpretability_; can people explain and comprehend a decision made by any given ML model? Data as scientists and engineers implementing models want to determine why and how classifiers are working, to evaluate whether they are effective or flawed. "Customers" of applied ML models, such as an applicants denied loans or traveler flagged security risks should be given reasonable explanations of decisions made by otherwise opaque systems.

LIME (Local Interpretable Model-Agnostic Explanations) can be used to provide explanations to "black box" ML models to alleviate such concerns. With a LIME tool, scientists can identify how a specific output variable (decision) was reached given set of input variables, at least a set scoped to be _local_ to a specific output. LIME then is used to produce a simpler-to-explain model in the immediate vicinity of that output (for example, a linear regression line with only a few, most-relevant coefficients rather than many.) Easy to plot and discuss communication can then be produced to "break down" a complex model into _interpretable explanations_. Finally, to count as LIME, the tool really works to produce these explanations regardless of original, complex ML model type, so that only variations of input data local to a specific output variable are needed to work, whether the opaque model itself uses random forests, support vector machines (SVM), and neural networks, or more in an ensemble. Thus, _model-agnostic_.

### User profile

The user of our LIME tool is expected to be a data scientist with Python programming experience. They are expected to be able to provide their own ML model, presumably a complex one that demands explanation and insight into its classifications. The user should be able to programmatically input predictors and corresponding output of their ML model into a LIME function via a Python call, and the user should want meaningful information reported from the LIME tool, likely in the form of clear linear plots of a decision function.

For our implementation, the user is specifically interested in evaluating a dataset of college statistics and corresponding salary information, which predicts income depending upon school, major, perhaps other factors. They will specifically want to learn why the model (which we will implement as the ML model component of our project) predicts more or less salary for a given school...whether school type or location etc. are most relevant to a given income prediction.

### Data sources

For this project the following datasets will be used.


#### Salaries by college

Data sourced from the Wall Street Journal has been used on Kaggle to analyze Salaries by college, region, and academic major. (https://www.kaggle.com/wsj/college-salaries). The data is released under (CC0 Public Domain license) [https://creativecommons.org/publicdomain/zero/1.0/].

Additional, related data containing more potentially meaningful variables has been compliled and shared (here)[https://www.kaggle.com/smithashivakumar/college] under (CC0 Public Domain license) [https://creativecommons.org/publicdomain/zero/1.0/].

#### College Scorecard

The United States Department of Education has shared the raw data from its College Scorecard page under (CC0 Public Domain license) [https://creativecommons.org/publicdomain/zero/1.0/]. This data includes annual rating data from years 2017-1996, and includes additional features not available in the Kaggle sets, such as demographic data about cohorts, race and gender statistics of students, and more.

### Use cases

Describing at least two use cases. For each, describe: (a) the objective of the user interaction (e.g., withdraw money from an ATM); and (b) the expected interactions between the user and your system.

#### Objective

#### Interactions
